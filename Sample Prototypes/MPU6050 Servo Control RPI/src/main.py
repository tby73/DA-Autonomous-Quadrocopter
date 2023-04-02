# Code to read gyroscope data from the MPU6050 Gyroscope/Accelerometer and control a servo motor proportional to the x-Axis movement of the Gyroscope
# Gyroscope values in dps (degree per sec) are displayed on a SSD1306 I2C OLED display

import RPi.GPIO as GPIO
import smbus2
import busio
import time
import adafruit_ssd1306 as ssd1306

# MPU6050 device address
MPU6050_DEVICE_ADDRESS = 0x68

# MPU6050 Gyroscope axis registers
GYRO_XOUT_H = 0x43
GYRO_XOUT_L = 0x44
GYRO_YOUT_H = 0x45
GYRO_YOUT_L = 0x46
GYRO_ZOUT_H = 0x47
GYRO_ZOUT_L = 0x48

# Servo Motor Signal Pin
SERVO_PIN = 11

# OLED width and height
OLED_WIDTH = 128
OLED_HEIGHT = 64

# MPU6050 I2C bus
i2c_bus = smbus2.SMBus(1)

# SSD1306 init
ssd_i2c = busio.I2C(0, 1)
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, ssd_i2c)

def InitSystem():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)

def InitMPU():
    i2c_bus.write_byte_data(MPU6050_DEVICE_ADDRESS, 0x6B, 0)

def ReadMPU(addr_high, addr_low):
    # read high and low bytes
    high_byte = i2c_bus.read_byte_data(MPU6050_DEVICE_ADDRESS, addr_high)
    low_byte = i2c_bus.read_byte_data(MPU6050_DEVICE_ADDRESS, addr_low)

    # get full data
    return (high_byte << 8) | low_byte

def SetServo(gyro_dps):
    # init PWM
    servo_pwm = GPIO.PWM(SERVO_PIN, 50)
    servo_pwm.start(0)

    # calculate angle from gyro dps
    servo_angle = (gyro_dps + 250) / 5.0

    # update duty cycle
    servo_pwm.ChangeDutyCycle(2 + servo_angle / 18)

def DisplayOLED(gyro_x, gyro_y, gyro_z):
    oled.fill(0)

    oled.text("X: {:.2f} dps".format(gyro_x), 0, 0, 1)
    oled.text("Y: {:.2f} dps".format(gyro_y), 0, 20, 1)
    oled.text("Z: {:.2f} dps".format(gyro_z), 0, 40, 1)

    oled.show()

def main():
    InitSystem()
    InitMPU()

    while True:
        # read raw data from MPU (Gyroscope data)
        gyro_xout = ReadMPU(GYRO_XOUT_H, GYRO_XOUT_L)
        gyro_yout = ReadMPU(GYRO_YOUT_H, GYRO_YOUT_L)
        gyro_zout = ReadMPU(GYRO_ZOUT_H, GYRO_ZOUT_L)

        # convert to dps (degree per sec)
        gyro_dps_x = gyro_xout * 131.0 / 32768.0
        gyro_dps_y = gyro_yout * 131.0 / 32768.0
        gyro_dps_z = gyro_zout * 131.0 / 32768.0

        # control servo from gyro dps
        SetServo(gyro_dps_x)

        # Display [X Y Z]-DPS on SSD1306
        DisplayOLED(gyro_dps_x, gyro_dps_y, gyro_dps_z)

        time.sleep(0.01)


if __name__ == "__main__":
    main()

