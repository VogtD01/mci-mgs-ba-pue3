# main.py -- put your code here!
import time
from machine import Pin, I2C
from ADXL345 import ADXL345_I2C

i2c = I2C(0)
imu = ADXL345_I2C(i2c)

if __name__ == "__main__":

    while(True):

        print(f'X Value: {imu.xValue}, Y Value: {imu.yValue}, Z Value: {imu.zValue}')
        time.sleep(0.1)
