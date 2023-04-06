# This code can be used to control a Brushless DC Motor (BLDC) using a Potmeter on a Raspberry Pi 4 or NVIDIA Jetson 
# with the Infineon IFX007T BLDC ESC Driver
# NOTE: This code works for both the Raspberry Pi 4 as well as the NVIDIA Jetson

import RPi.GPIO as GPIO
import time

# Potentiometer on GPIO 11
POTMETER_PIN = 11

# Driver PWM_IN and INHIBIT for sleep mode on 20/21
DRIVER_IN = 20
DRIVER_INHIBIT = 21

def InitSystem():
    # set to BCM mode
    GPIO.setmode(GPIO.BCM)

    # potmeter => Input
    GPIO.setup(POTMETER_PIN, GPIO.IN)

    # driver inputs => Output
    GPIO.setup(DRIVER_IN, GPIO.OUT)
    GPIO.setup(DRIVER_INHIBIT, GPIO.OUT)

def ReadPotmeter(potmeter_pin):
    return GPIO.input(potmeter_pin)

def SetBLDC(bldc_pwm, potmeter_value):
    bldc_pwm.ChangeDutyCycle((potmeter_value / 1024) * 100)

def main():
    # init system and driver PWM
    InitSystem()
    bldc_pwm = GPIO.PWM(DRIVER_IN, 50)
    bldc_pwm.start(0)

    while True:
        # read from pot and control BLDC
        potmeter_value = ReadPotmeter(POTMETER_PIN)
        SetBLDC(bldc_pwm, potmeter_value)
        time.sleep(0.01)

if __name__ == "__main__":
    main()

