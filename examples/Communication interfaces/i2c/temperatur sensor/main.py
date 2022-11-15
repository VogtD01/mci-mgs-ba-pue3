# Verbinden den i2c Temperatursensor mit dem ESP32 board
# Verwende dazu die Pins 18 (SCL) und 19 (SDA)
# Die Kommunikationsbefehle zum Lesen und Schreiben der Register des Temperatur Sensors sind im Datenblatt ersichtlich:
# NXP SE95: https://www.nxp.com/docs/en/data-sheet/SE95.pdf

import time
from machine import I2C

# Erstellung von i2c Objekt aus der I2C Klasse
i2c = I2C(0)

# Dieser Befehl scannt den i2c-Bus und gibt eine Liste der Adressen aller verbundenen Geräten aus
print(f'Available devices: {i2c.scan()}')

# Adresse des Temperatursensors
sensor_addr = 79 #0x4F
tmp_reg = 0 #0x00

# Initialisiert 2 Byte großen Buffer zum Speichern der Temp. Daten

if __name__ == "__main__":
    while True:
        # Liest 2 Bytes aus dem Register 0 (tmp_reg) aus und speichert diese in den 2 Byte Buffer tmp_buf.
        # Die Adresse des Registers lautet 0x00 und ist somit 16 bit groß.
        tmp_buf = i2c.readfrom_mem(sensor_addr, tmp_reg, addrsize=16)
        print(tmp_buf)
        #LSByte, MSByte = tmp_buf[1], tmp_buf[0]

        #print(f'LSB: {LSByte}, MSB: {MSByte}')
        #print(MSByte[7])
        #tmp = int.from_bytes(tmp_buf, 'big')
        #tmp = tmp * 0.03125
         
        #print(tmp)
        time.sleep(1)
        