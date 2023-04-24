# Import pre-existing libs
from machine import Pin, I2C
import time


# Import custom libs/wrappers
from libs.MotorPair import MotorPair
from libs.EncoderPair import EncoderPair
from libs.displayLib import Display
from libs.APDS9960LITE import APDS9960LITE

import libs.Webserver as web
import libs.stateManager as sm

def state_initialise(env: dict, *args) -> str:
    # Used in delta-time calculations
    env.lastUpdated = float(time.ticks_ms())
    # Define the robots logical state
    env.robot_state = "followLine"
    # Should the webserver be started?
    env.doWeb = True

    # Start web server if enabled
    if env.doWeb:
        web.loadHTMLRecurse("web", noConcatPath=True)
        web.web_pages["/"] = web.web_pages["/index.html"]
        env.web = web

    # Create I/O devices such as sensors and motors
    env._ir_pins = [Pin(27), Pin(28), Pin(26)]
    env.motors = MotorPair()
    env.encoder = EncoderPair()

    env.display = Display()
    env.display.clear()
    env.lastDisplayed = 0

    apdsi2c = I2C(0, scl=Pin(21), sda=Pin(20))
    env.apds9960 = APDS9960LITE(apdsi2c)
    env.apds9960.prox.enableSensor()

    return "readSensor"

sm.registerState("initialise", state_initialise)