import time
from machine import Pin, PWM

# Erstellen eines PWM objektes
pwm_0 = PWM(Pin(2))

# Auslesen von aktueller Frequenz und Duty cycles
# Ranges:
# Dutycycle: 0-1023  (0-100%)
# Frequenz: 1Hz-40MHz

# Initialisiere Frequenz mit 0
duty = pwm_0.duty(0)

# Initialisiere Frequenz mit 100KHz
freq = pwm_0.freq(100000)

min_value = 0
max_value = 1023


# Die Helligkeit der LED auf dem ESP32 board nimmt nun zu und wird wieder gedimmt 
if __name__ == "__main__":
    while True:

        for value in range(max_value):
            pwm_0.duty(value)
            time.sleep(0.001)
            
        for value in range(max_value):
            pwm_0.duty(max_value-value)
            time.sleep(0.001)
