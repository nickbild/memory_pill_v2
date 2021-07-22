from flask import Flask, request
from datetime import datetime
import sqlite3
from contextlib import closing


app = Flask(__name__)
now = datetime.now()


def populate_calendar(patient_id):
    html_events = ""
    html_events += populate_calendar_future_days(patient_id)
    html_events += populate_calendar_past_days(patient_id)
    html_events += populate_calendar_today(patient_id)

    return html_events


# Show actual medication administration times.
# - If each admin doesn't correspond with a scheduled time +/- X hours, highlight cell in red.
# - If more/less admins occur than scheduled, highlight cell in red.
def populate_calendar_past_days(patient_id):
    html_events = ""

    with closing(sqlite3.connect("../memory_pill.db")) as connection:
        connection.row_factory = sqlite3.Row
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT patient_id, medication_id, time FROM medication_schedule WHERE patient_id = '{0}'".format(patient_id))
            med_schedule = format_sqlite_results(cursor, ['patient_id', 'medication_id', 'time'])

            for day in range(1, now.day):
                day_flagged = False # Prevent a day from being flagged >1 time.
                # Determine number of times each medication *should* be taken each day.
                med_count = {}
                for sched in med_schedule:
                    if sched['medication_id'] not in med_count:
                        med_count[sched['medication_id']] = 1
                    else:
                        med_count[sched['medication_id']] += 1

                # Retrieve *actual* adminstrations.
                med_date = "{0}-{1:02d}-{2:02d}".format(now.year, now.month, day)
                cursor.execute("SELECT patient_id, medication_id, bottle_opened_at FROM medication_administrations WHERE patient_id = '{0}' AND bottle_opened_at LIKE '{1} %'".format(patient_id, med_date))
                med_admins = format_sqlite_results(cursor, ['patient_id', 'medication_id', 'bottle_opened_at'])

                for ma in med_admins:
                    cursor.execute("SELECT medication_name FROM medication_lookup WHERE medication_id = '{0}'".format(ma['medication_id']))
                    m = format_sqlite_results(cursor, ['medication_name'])

                    html_events += """
                    {{
                        title: '{0}',
                        start: '{1}'
                    }},""".format(m[0]['medication_name'], ma['bottle_opened_at'])

                    # For each medication taken, did it happen at the correct time?
                    for sched in med_schedule:
                        if ma['medication_id'] == sched['medication_id']:
                            bottle_open = ma['bottle_opened_at']
                            scheduled = bottle_open.split(" ")[0] + " " + sched['time'] + ":00.000000"
                            
                            date_format = "%Y-%m-%d %H:%M:%S.%f"
                            bottle_open_dt  = datetime.strptime(bottle_open, date_format)
                            scheduled_dt  = datetime.strptime(scheduled, date_format)
                            diff = abs(scheduled_dt - bottle_open_dt)
                            
                            # If difference in scheduled time and admin time is greater
                            # than 7200 seconds (2 hours), flag the cell.
                            if diff.seconds > 7200:
                                if not day_flagged:
                                    day_flagged = True
                                    html_events += """
                                    {{
                                        overlap: false,
                                        display: 'background',
                                        color: 'red',
                                        start: '{0}',
                                        end: '{0}'
                                    }},""".format(bottle_open.split(" ")[0])

                    # Track number of administrations of each medication.
                    if ma['medication_id'] in med_count:
                        med_count[ma['medication_id']] = med_count[ma['medication_id']] - 1

                # Did the correct number of administrations occur?
                alarm = False
                for c in med_count:
                    if med_count[c] != 0:
                        alarm = True

                if alarm:
                    if not day_flagged:
                        day_flagged = True
                        html_events += """
                        {{
                            overlap: false,
                            display: 'background',
                            color: 'red',
                            start: '{0}',
                            end: '{0}'
                        }},""".format(med_date)

    return html_events


# Show actual medication administration times.
# If too many administrations have happened, highlight cell in red.
def populate_calendar_today(patient_id):
    html_events = ""

    with closing(sqlite3.connect("../memory_pill.db")) as connection:
        connection.row_factory = sqlite3.Row
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT patient_id, medication_id, time FROM medication_schedule WHERE patient_id = '{0}'".format(patient_id))
            med_schedule = format_sqlite_results(cursor, ['patient_id', 'medication_id', 'time'])

            day = now.day
            # Determine number of times each medication *should* be taken each day.
            med_count = {}
            for sched in med_schedule:
                if sched['medication_id'] not in med_count:
                    med_count[sched['medication_id']] = 1
                else:
                    med_count[sched['medication_id']] += 1

            # Retrieve *actual* adminstrations.
            med_date = "{0}-{1:02d}-{2:02d}".format(now.year, now.month, day)
            cursor.execute("SELECT patient_id, medication_id, bottle_opened_at FROM medication_administrations WHERE patient_id = '{0}' AND bottle_opened_at LIKE '{1} %'".format(patient_id, med_date))
            med_admins = format_sqlite_results(cursor, ['patient_id', 'medication_id', 'bottle_opened_at'])

            for ma in med_admins:
                cursor.execute("SELECT medication_name FROM medication_lookup WHERE medication_id = '{0}'".format(ma['medication_id']))
                m = format_sqlite_results(cursor, ['medication_name'])

                html_events += """
                {{
                    title: '{0}',
                    start: '{1}'
                }},""".format(m[0]['medication_name'], ma['bottle_opened_at'])

                # Track number of administration of each medication.
                if ma['medication_id'] in med_count:
                    med_count[ma['medication_id']] = med_count[ma['medication_id']] - 1

            # Did an excessive number of administrations occur?
            alarm = False
            for c in med_count:
                if med_count[c] < 0:
                    alarm = True
            
            if alarm:
                html_events += """
                {{
                    overlap: false,
                    display: 'background',
                    color: 'red',
                    start: '{0}',
                    end: '{0}'
                }},""".format(med_date)

    return html_events


# Showed greyed-out medications, as scheduled to be taken.
def populate_calendar_future_days(patient_id):
    html_events = ""

    with closing(sqlite3.connect("../memory_pill.db")) as connection:
        connection.row_factory = sqlite3.Row
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT patient_id, medication_id, time FROM medication_schedule WHERE patient_id = '{0}'".format(patient_id))
            med_schedule = format_sqlite_results(cursor, ['patient_id', 'medication_id', 'time'])

            for s in med_schedule:
                cursor.execute("SELECT medication_name FROM medication_lookup WHERE medication_id = '{0}'".format(s['medication_id']))
                m = format_sqlite_results(cursor, ['medication_name'])

                for day in range(now.day+1, 32):
                    # Text label.
                    med_date = "{0}-{1:02d}-{2:02d}T{3}".format(now.year, now.month, day, s['time'])
                    html_events += """
                    {{
                        id: 'a{1}',
                        title: '{0}',
                        start: '{1}',
                        color: '#b8b8b8'
                    }},""".format(m[0]['medication_name'], med_date)

                    # Background color.
                    med_date_no_time = "{0}-{1:02d}-{2:02d}".format(now.year, now.month, day)
                    html_events += """
                    {{
                        overlap: false,
                        display: 'background',
                        color: '#e6e6e6',
                        start: '{0}',
                        end: '{0}'
                    }},""".format(med_date_no_time)

    return html_events


def generate_html_bottom(patient_name, patient_age, patient_gender, img, patients, patient_id):
    patient_select = ""
    for p in patients:
        if p['name'] is None:
            continue
        sel = ""
        if patient_id == p['patient_id']:
            sel = "selected"
        patient_select += "<option value='{0}' {2}>{1}</option>".format(p['patient_id'], p['name'], sel)

    result = """
        calendar.render();
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
            <img src="static/{3}" height="75" style="vertical-align: text-top;"> <span style="color: #cc0000;"><b>{0} {1} {2}</b></span> <br> <span style="color: #009933;">Medication Self-Administration Record</span>
        </div>

        <div id='calendar'></div>

        </body>
        </html>""".format(patient_name, patient_age, patient_gender, img, patient_select)

    return result


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


@app.route("/")
def home():
    patient_id = request.args.get('patient_id')
    patient_filter = ""
    if patient_id is not None and patient_id != "":
        patient_filter = "WHERE patient_id = '{0}'".format(patient_id)

    # Connect to DB and cache patient data.
    with closing(sqlite3.connect("../memory_pill.db")) as connection:
        connection.row_factory = sqlite3.Row
        with closing(connection.cursor()) as cursor:
            # All patients.
            cursor.execute("SELECT patient_id, name, age, gender, img FROM patients")
            patients = format_sqlite_results(cursor, ['patient_id', 'name', 'age', 'gender', 'img'])

            # Selected patient.
            cursor.execute("SELECT patient_id, name, age, gender, img FROM patients {0}".format(patient_filter))
            patient = format_sqlite_results(cursor, ['patient_id', 'name', 'age', 'gender', 'img'])

    if patient_id is not None and patient_id != "":
        html_events = populate_calendar(patient_id)
        html_bottom = generate_html_bottom(patient[0]['name'] + ",", patient[0]['age'], patient[0]['gender'], patient[0]['img'], patients, patient_id)
    else:
        html_events = ""
        html_bottom = generate_html_bottom('', '', '', '', patients, '')

    startDate = "initialDate: '{}',".format(now.strftime("%Y-%m-%d"))
    html_events = "\nevents: [" + html_events + "]});"
    html_top = open('calendar_top.html', 'r').read()

    return html_top + startDate + html_events + html_bottom


###
# Start server.
###

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
