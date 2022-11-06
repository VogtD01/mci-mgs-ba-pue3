from machine import Timer

# Callback-Funktionen werden ausgeführt sobald der dazugehörige Timer einen Zeitwert überschreitet
def callback_function(t):
    print("Hello again")

def callback_function2(t):
    print("Hello and goodbye")


# Das ESP32 board verfügt über vier Hardware timer (0-3)

# Timer 0 ruft nach jeder Sekunde die Callback Funktion
timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=callback_function)

# Timer 1 ruft einmalig nach 3 Sekunden die Callback Funktion Nr 2 auf
timer_1 = Timer(1)
timer_1.init(period=1000, mode=Timer.ONESHOT, callback=callback_function2)


if __name__ == "__main__":
    while True:
        # Hier passiert nichts
        pass
