class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several parameters)
        """
        print ("Creating a motor driver")
            
           in1pin = pyb.Pin(pyb.Pin.board.IN1A, pyb.Pin.OUT_PP)
           in2pin = pyb.Pin(pyb.Pin.board.IN2A, pyb.Pin.OUT_PP)

           tim2 = pyb.Timer(2, freq=10000)
           ch1 = tim2.channel(1, pyb.Timer.PWM, pin=in1pin) # control motor direction
           ch2 = tim2.channel(2, pyb.Timer.PWM, pin=in2pin)


    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        print (f"Setting duty cycle to {level}")
        ch1.pulse_width_percent(0)
        
    if __name__ == '__main__'
        moe = MotorDriver (a_pin, another_pin, a_timer)
        moe.set_duty_cycle (-42)
    
        
        
        