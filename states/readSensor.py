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


    # Consider calculating angle as angle where radius is 0.11 using theta = (360*C)/(2pi*r)
    # TODO: Verify Heading Result
    # From Aircraft turn angles: R = v^2 / (11.26 * tan(theta))
    # And; omega = (1091 * tan(theta)) / v
    #   Expression is in imperial; velocity is in knots, R is in feet
    #   Should velocity be average, difference, distance, max, min?

    # Constant in parentheses is unit conversions from one encoder click to meters
    #_enc_vel = math.sqrt(env.encL[1]**2 + env.encR[1]**2)*0.5*(0.010209875)

    # Calculate tan result, should the right motor be zero set tan to zero
    #_tan_val = 0
    #if env.encR[0] == env.encL[0]:
    #    _tan_val = 0
    #elif env.encR[0] > 0 and env.encL[0] == 0:
    #    # TODO
    #    # 0.11
    #
    #elif env.encL[0] > 0 and env.encR[0] == 0:
    #    # TODO
    #    pass
    #else:
    #    _tan_val = (env.encL[0]/env.encR[0])
#
    #env.turn_radius = _enc_vel**2 / (3.432 * _tan_val)
    #env.heading += (1091 * _tan_val) / _enc_vel
    _enc_dist = (env["encL"][0] - env["encR"][0])*0.010209875
    env["heading"] = (153.84*_enc_dist)/(2*3.1415*0.11) % 360 - 180

    vel = min(env["encL"][1], env["encR"][1])
    env["displacement"][0] += math.cos(env["heading"]*(3.1415/360))*vel
    env["displacement"][1] += math.sin(env["heading"]*(3.1415/360))*vel

    env["display"].clear()
    env["display"].text(env["state"])
    env["display"].text(f"Ang:{str(env['heading'])}")
    env["display"].show()

    return "updateMap"
