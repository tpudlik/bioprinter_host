#bioprinter_host

Software for controlling a two-axis bioprinter, designed at the Boston
Science Hack Day 2015.


## Usage ##

Edit `config.py` and set the parameters to the desired values.  In particular,
set `SERIAL_PORT` to an appropriate value for your operating system (the
default works with Linux), and set `MAX_INTENSITY`.

Run,
    
    python main.py [-t] [-c CODES_FILE] [-r RESPONSE_FILE] input_file

If you wish to use a CSV file as input (as opposed to an image file), use
the `-t` command line flag.  If you wish to save the G-CODEs to a file, rather
than send them to the Arduino, provide a file name with the `-c` flag.  If
you wish to save the Arduino's responses (it will acknowledge all commands and
describe its actions), provide a file name with the `-r` flag.

The input file should be a greyscale PNG, with dimensions `WIDTH` x `HEIGHT`
(as defined in `config.py`).  Some example images are provided in the
`example_files` folder.


## Dependencies ##

*   `numpy` for representing the input internally.
*   `pyserial` for communication with the Arduino.
*   `scipy` for image imports
*   `pillow` for image imports (scipy .misc uses pillow)
*   `matplotlib` for printing heatmaps. THIS IS NOT VITAL FOR OUR BioPrinting PACKAGE


## Testing ##

To run the unit tests, run `nosetests` from the main directory.


## TO DO ##

*   Use the `logging` module to keep track of the responses sent by the 
    Arduino.
*   Add more tests, including dependecy tests.
*   Clean up the source: keep tests
*   `HEIGHT`, `WIDTH` in config should be max values, not only accepted sizes.
*   Finish `test_recover_csv_from_gcode.py`.
*   Document the heatmap feature, make it optional (command line input).