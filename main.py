from libs.stateManager import StateManager

## Just some code that is not included in state_readSensor or state_initialise
#print(f"Prox, Sonic")
#for i in range(25):
#    display.rows = 0
#    display.text("Calibrating...")
#    display.show()
#    prox = apds9960.prox.proximityLevel
#    sonic_dist = dist_mm()
#    print(f"{prox:3d}, {sonic_dist:4.2f}")
#    time.sleep_ms(200)

sm = StateManager()

from states.initialise import state_initialise
sm.state = "initialise"
sm.registerState("initialise", state_initialise)

from states.followLine import state_followLine
sm.registerState("followLine", state_followLine)

from states.readSensor import state_readSensor
sm.registerState("readSensor", state_readSensor)

from states.updateMap import state_updateMap
sm.registerState("updateMap", state_updateMap)


while True:
    sm.updateState()

print("Exited state machine")
