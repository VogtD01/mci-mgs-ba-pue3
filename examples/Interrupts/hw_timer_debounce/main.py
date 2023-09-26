from machine import Pin, Timer

counter = 0

def on_pressed(timer):

	global counter
	counter += 1
	print(f'pressed! {counter}')

def debounce(pin):
	# Timer wird mit einer Verzögerung von 200ms gestartet. 
	# Nach Ablauf wird die callback Funktion "on_pressed aufgerufen"
	timer.init(mode=Timer.ONE_SHOT, period=200, callback=on_pressed)

# Hardware timer init.
timer = Timer(0)

# Init von button input pin in a pull-up Konfiguration.
btn = Pin(4, Pin.IN, Pin.PULL_UP)

# Registrierung von Interrupt bei steigender Flanke.
btn.irq(debounce, Pin.IRQ_RISING)

while True:

	pass