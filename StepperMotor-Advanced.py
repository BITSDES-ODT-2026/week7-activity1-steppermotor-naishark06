
from machine import Pin
import time

lists = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
in1 = Pin(5, Pin.OUT)
in2 = Pin(18, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(21, Pin.OUT)
t = 2

while True:
    for a in lists:
        in1.value(a[3])
        in2.value(a[2])
        in3.value(a[1])
        in4.value(a[0])
        time.sleep_ms(t)
