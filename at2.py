#!/usr/bin/env python

import serial

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

print "Serial is open: " + str(ser.isOpen())

print "Now Writing"
ser.write("AT\r\n")

print "Did write, now read"
x = ser.readline()
print "got '" + x + "'"

ser.close()
