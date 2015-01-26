#bioprinter_host

Software for controlling a two-axis bioprinter, designed at the Boston
Science Hack Day 2015.


## Dependencies ##

*   `numpy` for representing the input internally.
*   `pyserial` for communication with the Arduino.
*   `scipy` for image imports
*   `pillow` for image imports (`scipy.misc` uses Pillow)
*   `matplotlib` for printing heatmaps. Not required for basic functionality.


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


## TO DO ##

*   Use the `logging` module to keep track of the responses sent by the 
    Arduino.
*   Add more tests, including dependecy tests.
*   Clean up the source: keep tests
*   `HEIGHT`, `WIDTH` in config should be max values, not only accepted sizes.
*   Finish `test_recover_csv_from_gcode.py`.
*   Document the heatmap feature, make it optional (command line input).


[bioprinter_arduino]: https://github.com/tpudlik/bioprinter_arduino