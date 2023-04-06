# Import pre-existing libs
from machine import Pin, I2C
import time


# Import custom libs/wrappers
from libs.MotorPair import MotorPair
from libs.EncoderPair import EncoderPair
from libs.displayLib import Display
from libs.US import dist_mm
from libs.APDS9960LITE import APDS9960LITE

import libs.Webserver as web
from libs.Webserver import log, clear_log, killWeb
print("Loading webpages...")
web.loadHTMLRecurse("web", noConcatPath=True)
web.web_pages["/"] = web.web_pages["/index.html"]

# Pins for IR sensors
IR_l = Pin(27, Pin.IN)
IR_r = Pin(26, Pin.IN)
IR_c = Pin(28, Pin.IN)

# Create instance of motor and encoder wrappers
motors = MotorPair()
encoder = EncoderPair()
# Create a display
display = Display()


# Calibrate Sensor(s)
apdsi2c = I2C(0, scl=Pin(21), sda=Pin(20))
time.sleep_ms(100)
apds9960=APDS9960LITE(apdsi2c)
apds9960.prox.enableSensor()
time.sleep_ms(100)

print(f"Prox, Sonic")
for i in range(25):
    display.rows = 0
    display.text("Calibrating...")
    display.show()
    prox = apds9960.prox.proximityLevel
    sonic_dist = dist_mm()
    print(f"{prox:3d}, {sonic_dist:4.2f}")
    time.sleep_ms(200)

display.clear()

# Main Loop
lastUpdateTime = time.ticks_ms()
lastDisplayTime = 0

try:
    while True:
        dt = (time.ticks_ms() - lastUpdateTime) / 1000.0
        lastUpdateTime = time.ticks_ms()
        motors.duty(0, 0)
        # Read Sensor Values

        # Ultrasonic
        US_dist = dist_mm()

        # IR sensors
        ir = [IR_l.value(), IR_c.value(), IR_r.value()]
        log(f"IR Sensor (L/C/R): {ir[0]} | {ir[1]} | {ir[2]}")
        # RGB Sensor
        prox_dist = apds9960.prox.proximityLevel

        # Display Sensor Readings
        if lastDisplayTime > 1:
            display.clear()
            display.text(f"Motor: {motors.pwm_l} | {motors.pwm_r}")
            display.text(f"IR: L:{ir[0]} C:{ir[1]} R:{ir[2]}")
            display.text(f"Dist: {US_dist:.1f}mm")
            display.text(f"ProxDist: {prox_dist:.1f}")
            display.text(f"MDist: {encoder.getLeft()} | {encoder.getRight()}")
            display.text(f"IP: {web.wlan.ifconfig()[0]}")
            display.rows = 0
            display.show()
            lastDisplayTime = 0
        else:
            lastDisplayTime += dt
        encoder.reset()

        web.update_webserver()
except Exception as e:
    print(f"Error in main loop: {e}")

killWeb()
