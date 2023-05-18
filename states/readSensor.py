import time
import math

from libs.US import dist_mm

def state_readSensor(env:dict, *args:any) -> str:
    env["dt"] = (float(time.ticks_ms()) - env["lastUpdated"])/1000.0
    if env["dt"] == 0: env["dt"] = 0.01 # Prevent divide by zero
    env["lastUpdated"] = float(time.ticks_ms())

    # Read all IR Sensor values in accordance to how they were initialised in states/initialise.py
    env["ir"] = []
    for i in env["ir_pins"]:
        env["ir"].append(i.value())

    env["ir_adc"] = []
    for i in env["_ir_adc_pins"]:
        env["ir_adc"].append(i.read_u16())

    env["us_dist"] = dist_mm()
    # WARN: Not currently plugged in
    #env["prox_dist"] = env["apds9960"].prox.proximityLevel
    env["prox_dist"] = env["us_dist"]

    L,R = env["motors"].duty()
    env["dutyL"] = L
    env["dutyR"] = R


    # encoder state in tuple (pos, vel)
    env["encL"] = (env["encoder"].getLeft(), (env["encoder"].getLeft() - env["encL"][1])/env["dt"])
    env["encR"] = (env["encoder"].getRight(), (env["encoder"].getRight() - env["encR"][1])/env["dt"])


    _enc_dist = (env["encL"][0] - env["encR"][0])*0.010209875
    env["heading"] = (153.84*_enc_dist)/(2*3.1415*0.11) % 360 - 180

    vel = min(env["encL"][1], env["encR"][1])
    env["displacement"][0] += math.cos(env["heading"]*(3.1415/360))*vel
    env["displacement"][1] += math.sin(env["heading"]*(3.1415/360))*vel

    env["display"].clear()

    env["display"].text(env["state"])
    env["display"].text(f"Ang:{str(env['heading'])}")

    return "updateMap"
