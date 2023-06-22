# arduino-video-player
A tool displaying videos on an 8x8 led matrix that is connected directly to an Arduino board. Also includes a python script for taking gif-files and conveniently loading them into the Arduino's memory.

TODO description again because apparently i overwrote it at some point
## Requirements

### Hardware
- An Arduino board
  - so far only been tested with Arduino UNO R3 but any board should do.
- An 8x8 led matrix display
  - 16 pins, with a pin for each of the 8 rows and 8 columns
    - row pins should all be the same polarity and column pins the opposite polarity
  - proven to work with a "788BS" model led matrix
- cables
  - for connecting the board to the display
- resistors
  - so you won't burn out your display

for more help with setting up your hardware, I recommend reading through this blog: https://www.hackster.io/shahbaz75sb/8x8-led-matrix-interfacing-with-arduino-daec65


### Software:
some way to upload the project files to your arduino
- I personally use the Arduino IDE: https://www.arduino.cc/en/software

for the python script you will need:
- python 3.10 or newer: https://www.python.org/downloads/
- Pillow 9.5.0 (Python Image Library fork): https://pillow.readthedocs.io/en/stable/index.html


## How to use

1. make sure your hardware and software are set up correctly
2. (optional) use the included python script to convert a gif of your choice
    - the output will be written to data.h in the project folder
4. upload the Arduino project to your Arduino board
    - the video data will be read from the data.h file
5. profit
