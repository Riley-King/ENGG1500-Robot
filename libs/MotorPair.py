import motorLib

# WARNING: left and right motor pins are hard-coded in the class!!!
class MotorPair:
    def __init__(self):
        # Hold a local value for our targeted PWM for L+R
        #   as to enable fast and efficient changes of its value
        self.pwm_l = 50
        self.pwm_r = 50
        self.left_motor = motorLib.Motor(8, 9, 6)
        self.right_motor = motorLib.Motor(11, 10, 7)

    # Sets/Gets the pwm class variables.
    # If not arguments are provided, returns pwm_l, pwm_r
    # If pwm_l is not none, set it to provided value
    # If pwm_r is not none, set it to provided value
    def duty(self, pwm_l, pwm_r):
        if pwm_l is None and pwm_r is None: return self.pwm_l, self.pwm_r
        if pwm_l is not None: self.pwm_l = pwm_l
        if pwm_r is not None: self.pwm_r = pwm_r

    # Sets the underlying motor drivers PWM to the classes values
    def applyDuty(self):
        self.left_motor.duty(self.pwm_l)
        self.right_motor.duty(self.pwm_r)