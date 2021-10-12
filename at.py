import serial
import time 

phone = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1.0)

phone.write('AT\r\n')
result=phone.read(100)
print result

#phone.write('AT+CMGF=1\r\n')
#result=phone.read(100)
#print result

#phone.write('AT+CMGS="+336xxxxxxxx"\r\n')
#result=phone.read(100)
#print result
