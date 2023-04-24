import time
from libs.US import dist_mm
import libs.stateManager as sm

def state_updateGraphics(env:dict, *args:any) -> str:

    if float(time.ticks_ms()) > (env.lastDisplayed + 1):
        if env.doWeb: env.web.update_webserver()


        env.display.clear()

        env.display.text("updateGraphics")

        env.display.show()
        env.display.rows = 0

        env.lastDisplayed = float(time.ticks_ms())

    return "readSensor"

sm.registerState("updateGraphics", state_updateGraphics)
