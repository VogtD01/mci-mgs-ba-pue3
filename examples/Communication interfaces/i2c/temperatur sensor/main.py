# Verbinden den i2c Temperatursensor mit dem ESP32 board
# Verwende dazu die Pins 25 (SCL) und 26 (SDA)
# Die Kommunikationsbefehle zum Lesen und Schreiben der Register des Temperatur Sensors sind im Datenblatt ersichtlich:
# NXP SE95: https://www.nxp.com/docs/en/data-sheet/SE95.pdf

import time
from machine import I2C

# Erstellung von i2c Objekt aus der I2C Klasse
i2c = I2C(1)

# Dieser Befehl scannt den i2c-Bus und gibt eine Liste der Adressen aller verbundenen Geräten aus
print(f'Available devices: {i2c.scan()}')

# Adresse des Temperatursensors
sensor_addr = 0x4F # 79 decimal
id_reg = 0x05
tmp_reg = 0x00

# Initialisiert 2 Byte großen Buffer zum Speichern der Temp. Daten
tmp_buf = bytearray(2)
id_buf = bytearray(1)

# 13 Bit Auflösung, auf 0.03125 °C genau
resolution =  0.03125

# Initialisierung Vorzeichen
n_temp = 1

# Liest das ID register aus. Kann zur überprüfung der i2c Verbindung verwendet werden
# Sollwert: 0xA1
i2c.readfrom_mem_into(sensor_addr, id_reg, id_buf, addrsize=8)
print(f'Manufacturer ID: {id_buf}')

if __name__ == "__main__":
    while True:

        # Initialize 16 bit
        temperature = 0     
        # Liest 2 Bytes aus dem Register 0 (tmp_reg) aus und speichert diese in den 2 Byte Buffer tmp_buf.
        i2c.readfrom_mem_into(sensor_addr, tmp_reg, tmp_buf, addrsize=8)
         
        # Kommentiere die nächste Zeile aus um eine negative temperatur zu simulieren (MSB = High)
        # tmp_buf[0] = tmp_buf[0] | 0b10000000

        MSByte, LSByte = bin(tmp_buf[0]), bin(tmp_buf[1])
        print(MSByte, LSByte)


        if(tmp_buf[0] > 0b10000000):
            # Ist das MSBit des MSBytes high, ist die Temperatur negativ
            # Mit der XOR Verknüpfung wird das MSBit auf 0 gesetzt, die restlichen Bits werden nicht verändert
            tmp_buf[0] = tmp_buf[0] ^ 0b10000000
            n_temp = -1

        else:
            n_temp = 1
            
        temperature = (temperature | tmp_buf[0]) << 5
        tmp_buf[1] = (tmp_buf[1] >> 3)
        temperature = (temperature | tmp_buf[1]) 
        print(f'Temperatur: {float(temperature) * resolution * n_temp}°C')
        time.sleep(1)
        