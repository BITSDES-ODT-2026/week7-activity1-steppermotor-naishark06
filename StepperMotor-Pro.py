from machine import Pin
import time

lists = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
in1 = Pin(5, Pin.OUT)
in2 = Pin(18, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(21, Pin.OUT)
t = 2

while True:
    for x in range(0,501,1):
        for x in lists:
            in1.value(x[3])
            in2.value(x[2])
            in3.value(x[1])
            in4.value(x[0])
            time.sleep_ms(t)
    time.sleep(1)
    for y in range(0,501,1):
        for y in lists:
            in1.value(y[0])
            in2.value(y[1])
            in3.value(y[2])
            in4.value(y[3])
            time.sleep_ms(t)
    time.sleep(1)
