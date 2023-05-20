import math
import time
from libs.US import dist_mm

# ===============
#  Desired Logic
# ===============

# If all sensors are 'on',
#   then we are perpendicular to a piece of track such as an intersection, or
#   we overcorrected on a turn

# If all sensors are 'off';
#   Check if we are in the garage, if so
#       enter garage mode
#   Check if we are in a hallway, if so
#       enter hallway mode
#   Otherwise we lost the track,
#       slow down and shuffle left and right

# If only the left sensor is 'on', then we need to
#   turn left
# If only the right sensor is 'on', then we need to
#   turn right
# If only the center sensor is 'on', then we should
#   try to stay straight

# If the far_right sensor is on, and we are at a roundabout, then
#   Convert the noisy pulses to a single pulse, and
#   use this single pulse to increment exit counter
# Else if we are not at a roundabout, then
#   stop and turn right until heading is aligned to a 90 deg increment
# If the far_left sensor is on, then
#   stop and turn left until the heading is aligned to a 90 deg increment


# Params for handling IR readings
x_factor = [-25, 0, 25] # Distance from the center IR sensor

# Motor power settings
base_pwm = 30           # Base PWM for the motors
min_pwm = 24            # Minimum PWM for the motors
max_pwm = 60            # Maximum PWM for the motors
pwm_scale = (1, 1.13)   # Scales each wheels PWM outside of range checks
correction_factor = 3   # How hard/fast should responses be to line_error

prev_pwms = [base_pwm, base_pwm]

def state_followLine(env: dict, *args: any) -> str:
    ir_l = env["ir_adc"][0]
    ir_c = env["ir_adc"][1]
    ir_r = env["ir_adc"][2]

    num = x_factor[0]*ir_l + \
        x_factor[1]*ir_c + \
        x_factor[2] * ir_r

    dem = ir_l + ir_c + ir_r

    line_error = -int(num / dem)

    pwm_l = base_pwm + correction_factor * line_error
    pwm_r = base_pwm - correction_factor * line_error

    pwm_l = min(max(min_pwm, pwm_l), max_pwm)
    pwm_r = min(max(min_pwm, pwm_r), max_pwm)

    # If the center sees the line, but the left and right do not, we are likely perfectly on the line
    if (ir_l < 2000) and (ir_c > 2000) and (ir_r < 2000):
        pwm_l = base_pwm
        pwm_r = base_pwm

    doNotUpdatePrevPWM = False
    if (ir_l < 2000) and (ir_c < 2000) and (ir_r < 2000):
        pwm_l = prev_pwms[0]
        pwm_r = prev_pwms[1]
        doNotUpdatePrevPWM = True
    elif (ir_l > 2000) and (ir_c > 2000) and (ir_r > 2000):
        pwm_l = base_pwm
        pwm_r = base_pwm + correction_factor*10

    # Apply the PWMs
    env["motors"].duty(pwm_l=pwm_l*pwm_scale[0], pwm_r=pwm_r*pwm_scale[1])

    # Update the display with some values
    env["display"].text(f"PWM: {int(pwm_l)}|{int(pwm_r)}")
    env["display"].text(f"ERR: {int(line_error)}")
    env["display"].show()

    if not doNotUpdatePrevPWM:
        prev_pwms[0] = pwm_l
        prev_pwms[1] = pwm_r

    return "readSensor"
