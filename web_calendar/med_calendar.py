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


def generate_html_bottom(patient_name, patient_age, patient_gender, img, patients, patient_id):
    patient_select = ""
    for p in patients:
        if p['name'] is None:
            continue
        sel = ""
        if patient_id == p['patient_id']:
            sel = "selected"
        patient_select += "<option value='{0}' {2}>{1}</option>".format(p['patient_id'], p['name'], sel)


    result = """    calendar.render();
        }});

        </script>
        <style>

        body {{
            margin: 40px 10px;
            padding: 0;
            font-family: Arial, Helvetica Neue, Helvetica, sans-serif;
            font-size: 14px;
        }}

        #calendar {{
            max-width: 1100px;
            margin: 0 auto;
        }}

        </style>
        </head>
        <body bgcolor="#ffffff" style="margin-top: 0px; margin-left: 0px; margin-right: 0px;">
        <div style="width:100%; text-align:right; font-size:22px; font-weight-bold; background-color: #e0e0eb;">
            <form method='GET'>
            <select name='patient_id'>
                {4}
            </select>
            <input type='submit' value='open'>
            </form>
        </div>
        <div style="width:100%; text-align:center; font-size:22px; font-weight-bold; background-color: #e0e0eb;">
            <img src="static/{3}" height="75" style="vertical-align: text-top;"> <span style="color: #cc0000;"><b>{0} {1} {2}</b></span> <br> <span style="color: #009933;">Medication Administration Record</span>
        </div>

        <div id='calendar'></div>

        </body>
        </html>""".format(patient_name, patient_age, patient_gender, img, patient_select)

    return result


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
    if patient_id is not None and patient_id != "":
        patient_filter = "WHERE patient_id = '{0}'".format(patient_id)

    # Connect to DB and cache data.
    with closing(sqlite3.connect("../memory_pill.db")) as connection:
        connection.row_factory = sqlite3.Row
        with closing(connection.cursor()) as cursor:
            # All patients.
            cursor.execute("SELECT patient_id, name, age, gender, img FROM patients")
            patients = format_sqlite_results(cursor, ['patient_id', 'name', 'age', 'gender', 'img'])

            # Selected patient.
            cursor.execute("SELECT patient_id, name, age, gender, img FROM patients {0}".format(patient_filter))
            patient = format_sqlite_results(cursor, ['patient_id', 'name', 'age', 'gender', 'img'])

            cursor.execute("SELECT medication_id, medication_name FROM medication_lookup")
            med_lookup = format_sqlite_results(cursor, ['medication_id', 'medication_name'])

            cursor.execute("SELECT patient_id, medication_id, time, m, t, w, r, f, s, u FROM medication_schedule {0}".format(patient_filter))
            med_schedule = format_sqlite_results(cursor, ['patient_id', 'medication_id', 'time', 'm', 't', 'w', 'r', 'f', 's', 'u'])

            cursor.execute("SELECT patient_id, medication_id, bottle_opened_at FROM medication_administrations {0}".format(patient_filter))
            med_admins = format_sqlite_results(cursor, ['patient_id', 'medication_id', 'bottle_opened_at'])

    if patient_id is not None and patient_id != "":
        html_bottom = generate_html_bottom(patient[0]['name'] + ",", patient[0]['age'], patient[0]['gender'], patient[0]['img'], patients, patient_id)
    else:
        html_bottom = generate_html_bottom('', '', '', '', patients, '')

    return html_top + startDate + html_events + html_bottom


###
# Start server.
###

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
