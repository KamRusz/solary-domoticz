import time
import serial
import requests

ser = serial.Serial(
        port='/dev/ttyUSB0',    #moze trzeba zmienic
        baudrate = 9600,            #ustawic ten sam co w sterowniku
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
znakodczyt = bytearray(b'\x01\x01\x02\x03\x0a\x0b\x0c')
data = bytearray(b'\x8A\x54\x0A\x5A\x78\x78\x01\x78\x78\x78\x23')

#data[6] = znakodczyt[1]
print(data[6])
print(data)
ser.write(data)
x=ser.read(11)
#for i in x:
#    print(i)
temp = (100*x[8]+x[9])/10
print("temp =",temp,"st C")