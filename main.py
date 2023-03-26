# Import pre-existing libs
from machine import Pin
import time

# Import custom libs/wrappers
from libs.MotorPair import MotorPair
from libs.EncoderPair import EncoderPair
from libs.displayLib import Display
from libs.US import dist_mm
import libs.APDS9960LITE

# Pins for IR sensors
IR_l = Pin(27, Pin.IN)
IR_r = Pin(26, Pin.IN)
IR_c = Pin(28, Pin.IN)

# Create instance of motor and encoder wrappers
motors = MotorPair()
encoder = EncoderPair()
# Create a display
display = Display()


lastUpdateTime = time.ticks_ms()
while True:
    dt = (time.ticks_ms() - lastUpdateTime) / 1000.0
    motors.duty(100, 100)
    # Read Sensor Values

    # Ultrasonic
    US_dist = dist_mm()

    # IR sensors
    ir = [IR_l.value(), IR_c.value(), IR_r.value()]

    # RGB Sensor

    # Display Sensor Readings
    display.text(f"Motor: {motors.pwm_l} | {motors.pwm_r}")
    display.text(f"IR: L:{ir[0]} C:{ir[1]} R:{ir[2]}")
    display.text(f"Dist: {US_dist:.1f}mm")
    display.text(f"MDist: {encoder.getLeft()} | {encoder.getRight()}")
    display.text(f"MVel: {(encoder.getLeft()*dt):.1f} | {(encoder.getRight()*dt):.1f}")
    display.rows = 0
    display.show()

    encoder.reset()

