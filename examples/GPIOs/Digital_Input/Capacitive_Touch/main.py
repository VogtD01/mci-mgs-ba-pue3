import time
from machine import Pin, TouchPad


#----Original code---------------------------------------------------------------
#LED = Pin(2, Pin.OUT, drive=Pin.DRIVE_3)     # auskommentiert, weil fehler mit .drive
LED = Pin(2, Pin.OUT) # selsbt ergänz weil ging nicht
Capacitive_Touch = TouchPad(Pin(33))


while 1:
  print(Capacitive_Touch.read())
  if Capacitive_Touch.read()<400:
    LED.value( not LED.value())
  time.sleep(0.5)
 #-------------------------------------------------------------
 # eigenener Testcode von AI 
"""
from machine import Pin, TouchPad
import time

# LED an GPIO 2 konfigurieren
LED = Pin(2, Pin.OUT)

# Kapazitiver Touch-Sensor an GPIO 33
capacitive_touch = TouchPad(Pin(33))

while True:
    # Lese den Touch-Wert
    touch_value = capacitive_touch.read()
    print(touch_value)

    # Schalte die LED um, wenn der Touch-Wert unter einem Schwellenwert liegt
    if touch_value < 400:
        LED.value(not LED.value())

    time.sleep(0.2)
    print("works")
"""