# TODO:
#  - Increase the correction factor
#       - Turns too slow on a roundabout
#  - Prevent it from entering into an orbit around a path
#       - Occurs when entering near perpendicularly to a line
import math
import time
from libs.US import dist_mm

# Params for handling IR readings
x_factor = [-15, 0, 15] # Distance from the center IR sensor

# Motor power settings
base_pwm = 30           # Base PWM for the motors
pwm_scale = (1, 1.13)   # Scales each wheels PWM outside of range checks
correction_factor = 4   # How hard/fast should responses be to line_error


def state_followLine(env: dict, *args: any) -> str:
    ir_l = env["ir_adc"][0]
    ir_c = env["ir_adc"][1]
    ir_r = env["ir_adc"][2]

    # Compute the numerator of a weighted average
    num = x_factor[0]*ir_l + \
          x_factor[1]*ir_c + \
          x_factor[2]*ir_r

    # Compute the denominator of the weighted average
    den = ir_l + ir_c + ir_r

    # Compute the line error
    line_err = num / den

    # Compute the Left and Right motor PWMs
    pwm_l = base_pwm - correction_factor * line_err
    pwm_r = base_pwm + correction_factor * line_err

    # Apply the PWMs
    env["motors"].duty(pwm_l=pwm_l, pwm_r=pwm_r)

    # Update the display with some values
    env["display"].text(f"PWM: {int(pwm_l)}|{int(pwm_r)}")
    env["display"].text(f"ERR: {int(line_err)}")
    env["display"].show()

    return "readSensor"
