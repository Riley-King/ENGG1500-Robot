import time
from libs.US import dist_mm

# Params for averaging IR readings
avg_weight = 0
avg_num_samples = 20

# Motor power settings
avg_pwm = 30
correction_factor = avg_pwm*0.1

# Constants / 'globals'
x_factor = [-15, 0, 15]
avg_last_vals = [0, 0, 0]

def state_followLine(env: dict, *args: any) -> str:

    ir_l = (env["ir_adc"][0] + avg_last_vals[0]*avg_weight)/2
    ir_c = (env["ir_adc"][1] + avg_last_vals[1]*avg_weight)/2
    ir_r = (env["ir_adc"][2] + avg_last_vals[2]*avg_weight)/2

    avg_last_vals[0] += (env["ir_adc"][0] - avg_last_vals[0]) / avg_num_samples
    avg_last_vals[1] += (env["ir_adc"][1] - avg_last_vals[1]) / avg_num_samples
    avg_last_vals[2] += (env["ir_adc"][2] - avg_last_vals[2]) / avg_num_samples

    num = x_factor[0]*ir_l + \
          x_factor[1]*ir_c + \
          x_factor[2]*ir_r

    den = ir_l + ir_c + ir_r

    line_err = int(num / den)

    pwm_l = avg_pwm - correction_factor*line_err
    pwm_r = avg_pwm + correction_factor*line_err
    env["motors"].duty(pwm_l=pwm_l, pwm_r=pwm_r)

    env["display"].text(f"PWM: {pwm_l}|{pwm_r}")
    env["display"].text(f"ERR: {line_err}")
    env["display"].show()

    return "readSensor"
