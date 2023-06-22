# arduino-video-player
A tool displaying videos on an 8x8 led matrix that is hooked up to an Arduino. Also includes a python script for taking gif-files and conveniently loading them into the Arduino's memory.

TODO description again because apparently i overwrote it at some point

## Hardware
- An Arduino board
  - so far only been tested with Arduino UNO R3 but any board should do.
- An 8x8 led matrix display
  - 16 pins, with a pin for each of the 8 rows and 8 columns
    - row pins should all be the same polarity and column pins the opposite polarity
