# Einlesen des Wertes eines Potentiometers oder Lichtsenors (LDR) und Ausgabe im Terminal

import time
from machine import Pin, ADC

# Erstellen eines Pin Objekts für GPIO4
adc_pin = Pin(32, Pin.IN)

# Erstellen eines ADC Objekts aus der Klasse "ADC" und zuweisen des Pin Objekts
adc = ADC(adc_pin)

def normalisation(val_in):

    # Der Messwert wird als 16 Bit Integer mit Weren von 0 bis 65535 ausgegeben
    val_min_in = 0
    val_max_in = 65535

    # Für eine bessere Darstellung wird der Sensorwert in Zahlen von 0 bis 100 ausgegeben
    val_min_out = 0
    val_max_out = 100

    # Diese Funktion kann auch für negative Werte genutzt werden
    val_out = val_min_out + (val_max_out - val_min_out) * (val_in - val_min_in) / (val_max_in - val_min_in)
    
    return val_out


if __name__ == "__main__":
    while True:
        # Einlesen des Sensorwerts
        val_raw = adc.read_u16()

        # Normalisierung des Messwerts in Werte von 0 bis 100
        val_norm = normalisation(val_raw)

        #Ausgabe des normalisierten Werts im Terminal
        print(f'Sensor reading: {val_norm}')
        
        # Eine Sekunde warten
        time.sleep(0.2)
