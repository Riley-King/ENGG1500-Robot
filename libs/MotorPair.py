import time

from libs.motorLib import Motor
from libs.encoderLib import Encoder

MAX_STALL_PREVENT = 30

# WARNING: left and right motor pins are hard-coded in the class!!!
class MotorPair:
    def __init__(self, encoderPair):
        # Hold a local value for our targeted PWM for L+R
        #   as to enable fast and efficient changes of its value
        self.pwm_l = 50
        self.pwm_r = 50
        self.left_motor = Motor("left", 8, 9, 6)
        self.right_motor = Motor("right", 11, 10, 7)
        self.left_motor.set_forwards()
        self.right_motor.set_forwards()

        self.enc = encoderPair
        self.last_pos = (0,0)
        self.stall_pwm = [0, 0]
        self.last_check = 0

    # Sets/Gets the pwm class variables.
    # If not arguments are provided, returns pwm_l, pwm_r
    # If pwm_l is not none, set it to provided value
    # If pwm_r is not none, set it to provided value
    def duty(self, pwm_l=None, pwm_r=None):
        if pwm_l is None and pwm_r is None: return self.pwm_l, self.pwm_r
        if pwm_l is not None: self.pwm_l = pwm_l
        if pwm_r is not None: self.pwm_r = pwm_r

    # Sets the underlying motor drivers PWM to the classes values
    def applyDuty(self):
        self.left_motor.duty(int(max(min(self.pwm_l + self.stall_pwm[0], 100), 0)))
        self.right_motor.duty(int(max(min(self.pwm_r + self.stall_pwm[1], 100), 0)))
        self._checkStall()

    def _checkStall(self):
        return "Not Implemented"

        cur_pos = self.enc.get()
        dt = time.ticks_ms() - self.last_check
        if dt < 250: return

        l_vel = cur_pos[0] - self.last_pos[0]
        r_vel = cur_pos[1] - self.last_pos[1]

        if l_vel < 1 and self.pwm_l != 0: self.stall_pwm[0] += 5
        else: self.stall_pwm[0] = 0
        if r_vel < 1 and self.pwm_r != 0: self.stall_pwm[1] += 5
        else: self.stall_pwm[1] = 0

        self.last_pos = cur_pos
        self.last_check = time.ticks_ms()
