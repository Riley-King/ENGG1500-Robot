# Import pre-existing libs
from machine import Pin
import time

# Import custom libs/wrappers
from libs.MotorPair import MotorPair
from libs.EncoderPair import EncoderPair
import libs.US
import libs.APDS9960LITE
import libs.ssd1306

# Pins for IR sensors
IR_l = Pin(27, Pin.IN)
IR_r = Pin(26, Pin.IN)
IR_c = Pin(28, Pin.IN)

# Create instance of motor and encoder wrappers
motors = MotorPair()
encoder = EncoderPair()


while True:
    motors.duty(50, 50)
    encoder.reset()

# This is code
