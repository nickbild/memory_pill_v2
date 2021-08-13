# Memory Pill

Memory Pill passively records the last time a medication bottle was opened to prevent over- and underdosing of medications.  A companion web application receives this data, and compares it with the individual's presecribed medication schedule.  Any errors in self-administration will be flagged for review.

Using Memory Pill, it is possible to centrally monitor a large number of individuals, for example in an assisted living facitilty, to identify problems with medication administrations.  It is also possible to use on a small scale, such as in monitoring an elderly, yet still independent, relative across town, or across the world.

![cap and bottle](https://raw.githubusercontent.com/nickbild/memory_pill_v2/main/media/cap_and_bottle_sm.jpg)

This is an upgraded version of [Memory Pill](https://github.com/nickbild/memory_pill).

## How It Works

The rim of a medication bottle has been lined with a conductive ring.  For the prototype, conductive nylon was chosen.  No other instrumentation is present in the bottle.

![bottle rim](https://raw.githubusercontent.com/nickbild/memory_pill_v2/main/media/bottle_rim_sm.jpg)

The top of the bottle cap has an Adafruit HUZZAH32 ESP32 development board affixed.  Underneath this board is a 400 mAh LiPo battery pack.  The HUZZAH board contains the circuitry to recharge the battery.  For convenience of testing, the prototype has a switch to turn the device on and off.

![cap top](https://raw.githubusercontent.com/nickbild/memory_pill_v2/main/media/cap_top_sm.jpg)

A small hole was drilled in the bottle cap to allow two wires from the HUZZAH's GPIO pins to reach the bottom of the cap.  These wires are soldered to two large copper pads made from copper tape.  These pads are not in contact with one another.  When the lids is put on the bottle, an electrical circuit is completed between the pads by the conductive ring on the bottle.

![cap bottom](https://raw.githubusercontent.com/nickbild/memory_pill_v2/main/media/cap_bottom_sm.jpg)

The code running on the HUZZAH32 [is available here](https://github.com/nickbild/memory_pill_v2/tree/main/memory_pill_arduino).  When the lid is on, the ESP32 is put into an ultra-low power deep sleep mode to conserve battery, such that it can last between medication refills without needing to be charged.  On opening the bottle, the ESP32 is awoken, starts up its WiFi radio, and sends an HTTP POST request to [a custom API](https://github.com/nickbild/memory_pill_v2/blob/main/memory_pill_api.py) that contains unique identifiers representing the type of medication, and the patient that it has been prescribed to.  These bottle open events are stored in an SQLite3 database.

The SQLite3 database also contains information about patients and their prescribed medication schedules.  This data is used to drive [a web application](https://github.com/nickbild/memory_pill_v2/tree/main/web_calendar).  The application present a user with a calendar, and the ability to select a patient.

![web app](https://raw.githubusercontent.com/nickbild/memory_pill_v2/main/media/web_app_sm.jpg)

For past data, any exceptions to the expected medication schedule (missed doses, extra doses) will cause the day to be highlighted in red so that problems can be seen with a quick glance.  For dates in the future, the days will be greyed-out and display only the expected schedules of medications to be taken.

## Future Direction

Purpose-designed hardware would allow the device to be miniaturized further such that the electronics could all be concealed within the cap.  Reducing the size would allow for the addition of an inductive charging unit within the cap, which would allow pharmacists to simply set the caps on pads to recharge them before giving them to the next patient.  Also towards the goal of making Memory Pill more practical, the medication ID and patient ID will need to be reprogrammable by the pharmacist—as the ESP32 is WiFi-enabled, there are many possible ways to accomplish this.

## Bill of Materials

- Adafruit HUZZAH32
- 400 mAh LiPo battery
- Conductive nylon
- Copper tape
- Switch (optional)
- 10K ohm resistor
- 100K ohm resistor
- Miscellaneous wires

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
