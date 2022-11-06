# Verbinde einen Pushbutton mit Pin 4 des ESP boards
from machine import Pin

# Callback-Funktion wird ausgeführt sobald an GPIO4 eine steigende Flanke erkannt wird
def callback_function(pin):
    print("Button pressed")

interrupt_pin = Pin(4, Pin.IN)
interrupt_pin.irq(trigger=Pin.IRQ_RISING, handler=callback_function)

if __name__ == "__main__":
    while True:
    # Hier passiert nichts
        pass
