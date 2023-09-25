from time import sleep
from machine import Pin, ADC, PWM

# Setup:
# Verbinde eine LED mit GPIO25
# Verbinde einen Lichtsensor mit GPIO32
# Plaziere LED relativ nah an Lichtsensor (ca. 1cm Abstand)
# Verdunkle den Sensor mit den Händen
# Die LED soll nun heller leuchten

class PID:

    def __init__(self, Kp=0, Ki=0, Kd=0, st=1, sp=50):

        self.Kp = Kp                # Proportional
        self.Ki = Ki                # Integral
        self.Kd = Kd                # Derivative
        self.st = st                # Sampletime
        self.sp = sp                # Setpoint

        self.inpt = [1,0,0]         # Input array mit Anregeimpuls
        self.output = [0,0]         # Output array

    def control(self, inpt):

        self.inpt[0] = self.sp - inpt
        self.output[0] = self.output[1]+self.inpt[0]*(self.Kp+self.Kd+self.Ki)-self.inpt[1]*(2*self.Kd+self.Kp)+self.inpt[2]*self.Kd

        if self.output[0] <= -100:
            self.output[0] = -100

        print(f'PID Input: {self.inpt[0]} PID Output: {self.output[0]}')

        self.output[1] = self.output[0]
        self.inpt[2] = self.inpt[1]
        self.inpt[1] = self.inpt[0]

        sleep(self.st)

        return self.output[0]

def mapping(val_in, min_in, min_out, max_in, max_out):

    val_out = min_out + (max_out - min_out) * (val_in - min_in) / (max_in - min_in)
    return int(val_out)


if __name__ == "__main__":

    print("Main started")

    # ADC init
    adc_pin = Pin(32, Pin.IN)
    adc0 = ADC(adc_pin)

    # PWM Init
    pwm0 = PWM(Pin(25))
    pwm0.freq(10000)
    pwm0.duty(0)

    # PID Init
    pid = PID(Kp=0.1, Ki=0.1, Kd=0.1, st=0.1, sp=50)
    pid_out = 0

    while True:

        # Liest den aktuellen Helligkeitswert
        sensor_val_raw = adc0.read()
        print(f'raw: {sensor_val_raw}')

        # Normalisiert den Messwert auf einen Wert von 0 bis 100
        sensor_val_norm = mapping(sensor_val_raw, 0, 0, 4095, 100)
        print(f'mapped: {sensor_val_norm}')

        # Regelung durch PID controller
        pid_out = pid.control(inpt=sensor_val_norm)
        print(f'PID output: {pid_out}')

        led_value = mapping(pid_out, -100, 0, 100, 1023)

        # Duty Cycle kann minimal 0 sein
        if led_value < 0:
            led_value = 0

        pwm0.duty(led_value)
        print(f'LED PWM input: {led_value}\n')

        
