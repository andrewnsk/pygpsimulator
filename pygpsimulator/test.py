from pygpsimulator.simulator import PositionData
import serial
import time
from pygpsimulator import simutime
import sys
import os
from pygpsimulator import constants

serial_parity = serial.PARITY_NONE
serial_stopbits = serial.STOPBITS_ONE
serial_databits = serial.EIGHTBITS


serial_instance = serial.serial_for_url(constants.SERIAL_PORT,
                                        constants.SERIAL_BAUDRATE,
                                        bytesize=serial_databits,
                                        parity=serial_parity,
                                        stopbits=serial_stopbits,
                                        xonxoff=0,
                                        rtscts=0,
                                        do_not_open=True)
serial_instance.dtr = False
if os.path.exists(constants.SERIAL_PORT):
    serial_instance.open()
else:
    print("No USB serial device found")
    sys.exit(1)

time.sleep(2)  #

while True:

    data = bytes(PositionData().checksum(), encoding="ascii")
    print(PositionData().checksum())
    serial_instance.write(data)
    time.sleep(1)

    data = bytes(PositionData(sentence_id='GGA').checksum(), encoding="ascii")
    print(PositionData(sentence_id='GGA').checksum())
    serial_instance.write(data)
    time.sleep(1)

    print(simutime.TimeDate().get_time())
