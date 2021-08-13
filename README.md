# Memory Pill v2

Memory Pill passively records the last time a medication bottle was opened to prevent over- and underdosing of medications.  A companion web application receives this data, and compares it with the individual's presecribed medication schedule.  Any errors in self-administration will be flagged for review.

Using Memory Pill, it is possible to centrally monitor a large number of individuals, for example in an assisted living facitilty, to identify problems with medication administrations.  It is also possible to use on a small scale, such as in monitoring an elderly, yet still independent, relative across town, or across the world.

This is an upgraded version of [Memory Pill](https://github.com/nickbild/memory_pill).

# How It Works

The rim of a medication bottle has been lined with a conductive ring.  For the prototype, conductive nylon was chosen.  No other instrumentation is present in the bottle.

![bottle rim](https://raw.githubusercontent.com/nickbild/memory_pill_v2/main/media/bottle_rim_sm.jpg)

The top of the bottle cap has an Adafruit HUZZAH32 ESP32 development board affixed.  Underneath this board is a 400 mAh LiPo battery pack.  The HUZZAH board contains the circuitry to recharge the battery.  For convenience of testing, the prototype has a switch to turn the device on and off.

![cap top](https://raw.githubusercontent.com/nickbild/memory_pill_v2/main/media/cap_top_sm.jpg)

A small hole was drilled in the bottle cap to allow two wires from the HUZZAH's GPIO pins to reach the bottom of the cap.  These wires are soldered to two large copper pads made from copper tape.  These pads are not in contact with one another.  When the lids is put on the bottle, an electrical circuit is completed between the pads by the conductive ring on the bottle.

![cap bottom](https://raw.githubusercontent.com/nickbild/memory_pill_v2/main/media/cap_bottom_sm.jpg)
