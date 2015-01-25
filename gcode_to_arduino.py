
import serial
from config import SERIAL_BAUD, SERIAL_PORT

def gcode_to_arduino(gcode):
    """Send the gcode to the Arduino via the serial port."""
    # TO DO: test that the gcodes are correct
    complete_response = ''
    commands = gcode.split('\n')
    with serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=0.5) as ser:
        for command in commands:
            response = ser.read(500)
            while '>' not in response:
                response = ser.read(500)
            ser.write(command)
            print response
            complete_response += response

    return complete_response
