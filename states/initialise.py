# Import pre-existing libs
from machine import Pin, I2C, ADC
import time

from libs.Mapper import Mapper
# Import custom libs/wrappers
from libs.MotorPair import MotorPair
from libs.EncoderPair import EncoderPair
from libs.displayLib import Display
from libs.APDS9960LITE import APDS9960LITE
def state_initialise(env: dict, *args) -> str:
    # Used in delta-time calculations
    env["lastUpdated"] = float(time.ticks_ms())
    # Define the robots logical state
    env["robot_state"] = "followLine"

    # Create I/O devices such as sensors and motors
    env["ir_pins"] = [Pin(22), Pin(19)]
    env["_ir_adc_pins"] = [ADC(Pin(27)), ADC(Pin(28)), ADC(Pin(26))]
    env["encoder"] = EncoderPair()
    env["motors"] = MotorPair(env["encoder"])
    env["encL"] = (0,0)
    env["encR"] = (0,0)

    env["display"] = Display()
    env["display"].clear()
    env["lastDisplayed"] = 0

    # WARN: not currently plugged in
    #apdsi2c = I2C(0, scl=Pin(21), sda=Pin(20))
    #env["apds9960"] = APDS9960LITE(apdsi2c)
    #env["apds9960"].prox.enableSensor()

    env["map"] = Mapper()

    env["heading"] = 0
    env["displacement"] = [0, 0]

    return "readSensor"

