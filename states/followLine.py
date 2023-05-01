import time
from libs.US import dist_mm

avg_pwm = 40
x_factor = [-15, 0, 15]
correction_factor = 3

def state_followLine(env: dict, *args: any) -> str:

    num = x_factor[0]*env.ir_adc[0] + x_factor[1]*env.ir_adc[1] + x_factor[2]*env.ir_adc[2]
    den = env.ir_adc[0] + env.ir_adc[1] + env.ir_adc[2]

    line_err = - (num // den)
    env.motors.duty(avg_pwm + correction_factor*line_err,
                    avg_pwm - correction_factor*line_err)



    return "updateGraphics"
