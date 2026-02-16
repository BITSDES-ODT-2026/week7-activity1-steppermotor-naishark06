
 from machine import Pin
  import time
    
  in1 = Pin(5, Pin.OUT)
  in2 = Pin(18, Pin.OUT)
  in3 = Pin(19, Pin.OUT)
  in4 = Pin(21, Pin.OUT)
  t = 2
    
  while True:
      #Step1
      in1.value(1)
      in2.value(1)
      in3.value(0)
      in4.value(0)
      time.sleep_ms(t)
      #Step2 
      in1.value(0)
      in2.value(1)
      in3.value(0)
      in4.value(0)
      time.sleep_ms(t)
      #Step3
      in1.value(0)
      in2.value(1)
      in3.value(1)
      in4.value(0)
      time.sleep_ms(t)
      #Step4
      in1.value(0)
      in2.value(0)
      in3.value(1)
      in4.value(0)
      time.sleep_ms(t)
      #Step5
      in1.value(0)
      in2.value(0)
      in3.value(1)
      in4.value(1)
      time.sleep_ms(t)
      #Step6
      in1.value(0)
      in2.value(0)
      in3.value(0)
      in4.value(1)
      time.sleep_ms(t)
      #Step7
      in1.value(1)
      in2.value(0)
      in3.value(0)
      in4.value(1)
      time.sleep_ms(t)
      #Step8
      in1.value(1)
      in2.value(0)
      in3.value(0)
      in4.value(0)
      time.sleep_ms(t)
