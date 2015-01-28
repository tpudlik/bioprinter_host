
import serial
from config import SERIAL_BAUD, SERIAL_PORT, SERIAL_TIMEOUT

def gcode_to_arduino(gcodes):
    """Send the gcodes to the Arduino via the serial port.

    The input must be a string, with the individual G-CODES separated by 
    newline characters.  The string may, but doesn't have to, end with a 
    newline.  Examples of valid input are,

        "G1X0Y0;"
        "G1X0Y0;\nM400;"
        "G1X0.45Y3.0;\nM700 P0 S543;\nM700 P0 S543;\nG1X0.45Y3.3;\n"

    """
    # TO DO: test that the gcodes are correct
    log = ''
    commands = gcodes.split('\n')
    with serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=SERIAL_TIMEOUT) as ser:
        for command in commands:
            response, log = listen(ser, log)
            while '>' not in response:
                response, log = listen(ser, log)
            log = write(ser, command, log)
        response, log = listen(ser, log)
    return log

def listen(ser, log):
    """Listen to serial port ser, return what you hear, append it to log."""
    response = ser.read(500)
    summary = "I received: " + repr(response)
    log += summary + "\n"
    print summary
    return response, log

def write(ser, command, log):
    """Write command to serial port, append what you write to log."""
    ser.write(command)
    summary = "   I wrote: " + repr(command)
    log += summary + "\n"
    print summary
    return log
