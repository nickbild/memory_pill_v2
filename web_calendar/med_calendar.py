from flask import Flask, request
from datetime import datetime
import sqlite3
from contextlib import closing


now = datetime.now()
dates_meds_taken = {}
html_events = "events: ["


def med_not_taken_warnings(dates_meds_taken):
    global html_events
    for i in range(1, now.day+1):
        check_date = "{0}-{1}-{2:02d}".format(now.year, now.month, i)
        if check_date not in dates_meds_taken:
            # Color day red (to indicate med not taken).
            html_events += """{{
                overlap: false,
                display: 'background',
                color: '#ff9f89',
                start: '{0}',
                end: '{0}'
            }},""".format(check_date)

            html_events += """{{
                title: 'Missed dose - Amlodipine',
                start: '{}'
            }},""".format(check_date)


def format_sqlite_results(cursor, columns):
    l = []
    while True:
        d = {}
        row = cursor.fetchone()
        if row == None:
            break
        for column in columns:
            d[column] = row[column]
        l.append(d)
    return l


app = Flask(__name__)
# Get page templates.
html_top = open('calendar_top.html', 'r').read()
html_bottom = open('calendar_bottom.html', 'r').read()

# Set current date in calendar.
startDate = "initialDate: '{}',".format(now.strftime("%Y-%m-%d"))

# for item in items:
#     j = str(item).replace("'", "\"")
#     j = json.loads(j)
#     time_split = j["Time"].split(" ") # Tue Oct 20 12:32:35 2020

#     # Show time med taken.
#     html_events += """{{
#         title: 'Amlodipine',
#         start: '{0}-{1}-{2}T{3}'
#     }},""".format(time_split[4], month_to_number(time_split[1]), time_split[2], time_split[3])

#     # Color day green (to indicate med taken).
#     html_events += """{{
#         overlap: false,
#         display: 'background',
#         color: '#89FF89',
#         start: '{0}-{1}-{2}',
#         end: '{0}-{1}-{2}'
#     }},""".format(time_split[4], month_to_number(time_split[1]), time_split[2], time_split[3])

#     date = "{0}-{1}-{2}".format(time_split[4], month_to_number(time_split[1]), time_split[2])
#     dates_meds_taken[date] = True

# med_not_taken_warnings(dates_meds_taken)

html_events += "]});"

@app.route("/")
def home():
    patient_id = request.args.get('patient_id')
    patient_filter = ""
    if patient_id is not None:
        patient_filter = "WHERE patient_id = '{0}'".format(patient_id)

    # Connect to DB and cache data.
    with closing(sqlite3.connect("../memory_pill.db")) as connection:
        connection.row_factory = sqlite3.Row
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT patient_id, name, age, gender FROM patients")
            patients = format_sqlite_results(cursor, ['patient_id', 'name', 'age', 'gender'])

            cursor.execute("SELECT medication_id, medication_name FROM medication_lookup")
            med_lookup = format_sqlite_results(cursor, ['medication_id', 'medication_name'])

            cursor.execute("SELECT patient_id, medication_id, time, m, t, w, r, f, s, u FROM medication_schedule {0}".format(patient_filter))
            med_schedule = format_sqlite_results(cursor, ['patient_id', 'medication_id', 'time', 'm', 't', 'w', 'r', 'f', 's', 'u'])
            print(med_schedule)

            cursor.execute("SELECT patient_id, medication_id, bottle_opened_at FROM medication_administrations {0}".format(patient_filter))
            med_admins = format_sqlite_results(cursor, ['patient_id', 'medication_id', 'bottle_opened_at'])

    return html_top + startDate + html_events + html_bottom


###
# Start server.
###

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
