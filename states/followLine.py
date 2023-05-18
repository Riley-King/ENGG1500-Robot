# TODO:
#  - Increase the correction factor
#       - Turns too slow on a roundabout
#  - Prevent it from entering into an orbit around a path
#       - Occurs when entering near perpendicularly to a line
import math
import time
from libs.US import dist_mm

# Params for handling IR readings
avg_weight = -0.1       # How much should the average affect this iteration
avg_acc_weight = 1      # How much of the current average be present in the future average
avg_num_samples = 20    # How large of a window does the moving average have
prev_vals_weight = -0.6 # How much of the previous IR values should be used if all IRs are white
ignore_vals = [         # Below what threshold should IR readings be rounded to zero
    1728, 152, 1608     # ^^^
]                       # ^^^
x_factor = [-15, 0, 15] # Distance from the center IR sensor
line_err_offset = 0     # Offset for line_error variable
line_err_max_mag = 10   # Maximum magnitude for the line error value

# Motor power settings
avg_pwm = 30            # Base PWM for the motors
min_pwm = 26            # Lowest possible PWM
max_pwm = 48            # Highest possible PWM
pwm_scale = (1, 1.13)   # Scales each wheels PWM outside of range checks
correction_factor = 4   # How hard/fast should responses be to line_error

# State globals - Please Ignore
avg_last_vals = [0, 0, 0]
prev_vals = [0, 0, 0]

def state_followLine(env: dict, *args: any) -> str:
    # Compute the current IR reading by mixing raw readings with a weighted average reading
    ir_l = (env["ir_adc"][0] + avg_last_vals[0]*avg_weight)/2
    ir_c = (env["ir_adc"][1] + avg_last_vals[1]*avg_weight)/2
    ir_r = (env["ir_adc"][2] + avg_last_vals[2]*avg_weight)/2

    # If the values are below a certain threshold, set them to zero
    if ir_l < ignore_vals[0]: ir_l = 0
    if ir_c < ignore_vals[1]: ir_c = 0
    if ir_r < ignore_vals[2]: ir_r = 0

    # Compute future average
    avg_last_vals[0] += (env["ir_adc"][0] - avg_last_vals[0]*avg_acc_weight) / avg_num_samples
    avg_last_vals[1] += (env["ir_adc"][1] - avg_last_vals[1]*avg_acc_weight) / avg_num_samples
    avg_last_vals[2] += (env["ir_adc"][2] - avg_last_vals[2]*avg_acc_weight) / avg_num_samples

    # If ALL IR sensors are below their thresholds,
    #   set IR readings to a previous value and prevent updating the previous value
    block_prev_update = False
    if ir_l == 0 and ir_c == 0 and ir_r == 0:
        ir_l = prev_vals[0]*prev_vals_weight
        ir_c = prev_vals[1]*prev_vals_weight
        ir_r = prev_vals[2]*prev_vals_weight
        block_prev_update = True

    print(f"IR: {ir_l} | {ir_c} | {ir_r}")

    # Compute the numerator of a weighted average
    num = x_factor[0]*ir_l + \
          x_factor[1]*ir_c + \
          x_factor[2]*ir_r

    # Compute the denominator of the weighted average
    den = ir_l + ir_c + ir_r
    # Ensure the denominator is not zero
    if den == 0: den = 999999

    # Compute the line error
    line_err = int(num / den) + line_err_offset

    # Bound the line error value
    if line_err > line_err_max_mag:
        line_err = line_err_max_mag
    elif line_err < -line_err_max_mag:
        line_err = -line_err_max_mag

    # Compute the Left and Right motor PWMs
    pwm_l = avg_pwm - correction_factor*line_err
    pwm_r = avg_pwm + correction_factor*line_err

    # Ensure that PWMs are greater or equal to the min
    pwm_l = min(max(pwm_l, min_pwm), max_pwm) * pwm_scale[0]
    pwm_r = min(max(pwm_r, min_pwm), max_pwm) * pwm_scale[1]


    # Apply the PWMs
    env["motors"].duty(pwm_l=pwm_l, pwm_r=pwm_r)

    # Update the display with some values
    env["display"].text(f"PWM: {pwm_l}|{pwm_r}")
    env["display"].text(f"ERR: {line_err}")
    env["display"].show()

    if not block_prev_update:
        prev_vals[0] = ir_l
        prev_vals[1] = ir_c
        prev_vals[2] = ir_r

    return "readSensor"
