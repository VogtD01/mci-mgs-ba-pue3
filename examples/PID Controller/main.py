from machine import Pin, ADC, Timer, PWM

start_pin = Pin(34, Pin.PULL_DOWN)

# Init adc
adc_pin = Pin(32, Pin.IN)
adc0 = ADC(adc_pin)
adc_read = 1

# PWM Init
pwm0 = PWM(Pin(25))
pwm0.freq(100000)
pwm0.duty(0)

# PID Values
Kp = 1
Ki = 0.1
Kd = 100

# Inputs zu den Zeitpunkten t0, t-1 und t-2
inpt = [0,0,0]
inpt[0] = 1
# Outputs zu den Zeitpunkten t0 und t-1
output = [0,0]

setpoint = 50


def mapping(val_in, min_in, min_out, max_in, max_out):
    return min_out + (max_out - min_out) * (val_in - min_in) / (max_in - min_in)

def ISR(t):

    raw_input = adc0.read_u16()
    measured = mapping(raw_input, 0, 0, 65535, 100)

    print(f'raw measured: {raw_input}, mapped measured: {measured}')

    inpt[0] = setpoint - measured

    output[0] = output[1]+inpt[0]*(Kp+Kd+Ki)-inpt[1]*(2*Kd+Kp)+inpt[2]*Kd

    print(f'Input: {inpt[0]} Output: {output[0]}')


    led_duty = int(mapping(output[0], 0, 0, 100, 1023))

    print(f'dc: {led_duty}')
    pwm0.duty(led_duty)

    output[1] = output[0]
    inpt[2] = inpt[1]
    inpt[1] = inpt[0]



tim0 = Timer(1)
tim0.init(period=200, mode=Timer.PERIODIC, callback=ISR)

if __name__ == "__main__":
    while True:

        # Um die ISR Funktion des Timers bei Bedarf zu unterbrechen,
        # überprüft das Programm ob Pin 34 einen HIGH Zustand hat.
        # Ist der Zustand LOW, wird der Timer deinitialisiert.
        if not start_pin.value():
            tim0.deinit()
