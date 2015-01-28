#bioprinter_host

Software for controlling a two-axis bioprinter, designed at the Boston
Science Hack Day 2015.  This repository contains the code to be run on the
host machine (the computer controlling the Arduino).  For the complementary
code that must be uploaded to the Arduino, see [bioprinter_arduino].


## Dependencies ##

*   `numpy` for representing the input internally.
*   `pyserial` for communication with the Arduino.
*   `scipy` for image imports
*   `pillow` for image imports (`scipy.misc` uses Pillow)
*   `matplotlib` for printing heatmaps. Not required for basic functionality.
    See the Debugging Aids section, below.


## Installation ##

1.  Install the dependencies listed above if they are not already on your
    system.  You can do this via `pip install`.

2.  Clone this repository on the machine connected to the Arduino running the
    [Arduino code][bioprinter_arduino]:

        git clone https://github.com/tpudlik/bioprinter_host.git

3.  Edit the `config.py` file in the cloned repository.  In particular, you
    will want to set the `SERIAL_PORT` value to the name of the Arduino's
    serial port.  The most likely choices, depending on your operating system,
    are,

    *   OSX: something like `/dev/tty.usbmodem621` (for the Uno or Mega
        2560) or `/dev/tty.usbserial-A02f8e` (for older, FTDI-based
        boards).

    *   Linux: `/dev/ttyACM0` or similar (for the Uno or Mega 2560), or
        `/dev/ttyUSB0` or similar (for older boards).

    *   Windows: a COM port, but you'll need to check in the Device
        Manager (under Ports) to see which one.

    You will also want to set the value of `MAX_INTENSITY`, which determines 
    the maximum number of times ink will be released into the same spot.

4.  If you have `nose` installed, you can run the tests via `nosetests`.


## Usage ##

The software lets you control the printer in two ways.

1.  *Image file.*  You can instruct the printer to print out a _greyscale_ 
    PNG image.  The image must have `HEIGHT` by `WIDTH` pixels (these values
    can be set in the `config.py` file, but must not exceed the maximum
    number of steps the motors can take, currently unknown). White pixels 
    correspond to `MAX_INTENSITY` depositions from the printer head, while 
    black pixels correspond to nothing being printed.  Some example images are
    provided in the `example_files` folder.
2.  *CSV file.*  For maximum control, you can opt to pass the printer a CSV
    file with `HEIGHT` rows of `WIDTH` entries each.  The entries should be 
    integers, and will be rescaled by the program to lie between 0 and
    `MAX_INTENSITY`.

In either case, each pixel represents an area of approximately 0.30 mm by
0.26 mm. The resolution is slightly higher in the `Y` or `HEIGHT` direction,
along the line of the printer nozzles.

When you have an input file ready, you can send it to the printer using the
command,
    
    python main.py [-t] [-c CODES_FILE] [-r RESPONSE_FILE] input_file

The `-t` flag indicates you're using a CSV file as input (as opposed to a
PNG file).  The `-c` flag allows you to save the G-CODEs (machine instructions
that would be sent to the Arduino) to a file instead of actually transmitting
them.  The `-r` flag will direct the program to save the Arduino's responses
to a file.  (The Arduino acknowledges all commands and describes its
actions.)


### Debugging Aids ###

By default, if you provide a PNG file `filename.png` as an input to `main.py`,
the program will generate two files that will help with debugging potential
problems:

1.  `filename.arrayplot.png`, which compares the input PNG file to the
    version normalized to `MAX_INTENSITY`.  The image on the right is a more
    accurate representation of what will actually be printed.
2.  `filename.csv`, a CSV representation of the image that will be printed.
    The CSV file will have `HEIGHT` rows and `WIDTH` columns.  Its entries are
    the number of depositions from the inkhead that will take place for a
    given pixel.

If you do not wish the software to generate these files, edit `config.py`
and set `HEATMAP_OUTPUT` or `CSV_OUTPUT`, respectively, to `False`.  If you
set `HEATMAP_OUTPUT` to `False`, `matplotlib` is no longer required to
run the program.


### Example Files ###

To test the printer you may wish to print one of the test images, `heart.png`
or `own_img_cross.png`.  To do so, run

    python main.py ./example_files/heart.png

or,
    
    python main.py ./example_files/own_img_cross.png



## TO DO ##

*   Use the `logging` module to keep track of the G-CODES sent and Arduino
    responses received.
*   Redo the command line interface.  The `-t` option should be scrapped,
    replaced by autorecognition.  The `-r` option should also be scrapped:
    the communication on the serial port should always be recorded in a log
    file.  A `--quiet` option should be introduced to suppress the printing of
    the serial port chatter to STDOUT.  (The two latter changes will be much
    easier once the `logging` module is put to use.)
*   Add more tests, including dependecy tests.
*   Clean up the source: some of the files in `example_files` should probably
    be moved to `tests`.
*   `HEIGHT`, `WIDTH` in config should be max values, not only accepted sizes.
*   Finish `test_recover_csv_from_gcode.py`.


[bioprinter_arduino]: https://github.com/tpudlik/bioprinter_arduino