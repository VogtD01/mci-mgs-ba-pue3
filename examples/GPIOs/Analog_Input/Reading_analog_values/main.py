# Einlesen des Wertes eines Potentiometers oder Lichtsenors (LDR) und Ausgabe im Terminal

import time
from machine import Pin, ADC

# Erstellen eines Pin Objekts für GPIO4
adc_pin = Pin(32, Pin.IN)

# Erstellen eines ADC Objekts aus der Klasse "ADC" und zuweisen des Pin Objekts
adc = ADC(adc_pin)


if __name__ == "__main__":
    while True:
        # Einlesen des Sensorwerts
        val = adc.read_u16()

        #Ausgabe des normalisierten Werts im Terminal
        print(f'Sensor reading: {val}')
   
        # Eine Sekunde warten
        time.sleep(0.2)
