import time
from libs.US import dist_mm

def state_readSensor(env:dict, *args:any) -> str:
    env.dt = (float(time.ticks_ms()) - env.lastUpdated)/1000.0
    if env.dt == 0: env.dt = 0.01 # Prevent divide by zero
    env.lastUpdated = float(time.ticks_ms())

    # Read all IR Sensor values in accordance to how they were initialised in states/initialise.py
    env.ir = []
    for i in env._ir_pins:
        env.ir.append(i.value())

    env.us_dist = dist_mm()
    env.prox_dist = env.apds9960.prox.proximityLevel

    L,R = env.motors.duty()
    env.dutyL = L
    env.dutyR = R

    # encoder state in tuple (pos, vel)
    env.encL = (env.encoder.get_left(), (env.encoder.get_left() - env.encL)/env.dt)
    env.encR = (env.encoder.get_left(), (env.encoder.get_left() - env.encR)/env.dt)


    return env.robot_state
