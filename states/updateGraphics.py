import time

def state_updateGraphics(env:dict, *args:any) -> str:

    if float(time.ticks_ms()) > (env.lastDisplayed + 1):
        env.display.clear()

        env.display.text("updateGraphics")

        env.display.show()
        env.display.rows = 0

        env.lastDisplayed = float(time.ticks_ms())

    return "readSensor"
