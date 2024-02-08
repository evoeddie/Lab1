"""! @Control A Physical Thing.py
     Script for controlling the brightness of an LED
     using PWM on a microcontroller. By also haveing
     the ability to change the frequwncy
 
    @author Alia Wolken, Eduardo Santos, Andrew Jwaideh
    
"""

def led_setup():
    """! Doxygen style docstring for this function 
    Setup PWM for controlling LED brightness."""
    # Function code here
    tim = pyb.Timer(2, freq=1000)  # Timer 2, frequency 1kHz
    ch = tim.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.PA0, pulse_width=0)  # Channel 1 on PA0
    ch.pulse_width_percent(0)  # Set duty cycle to 0%

def led_brightness():
    """! Doxygen style docstring for this function 
    Set LED brightness using PWM duty cycle."""
    # More function code here
    tim = pyb.Timer(2)  # Use Timer 2
    ch = tim.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.PA0, pulse_width=0)  # Channel 1 on PA0
    for duty_cycle in range(101): 
        ch.pulse_width_percent(duty_cycle)  # Set duty cycle
        time.sleep(0.05)  # Wait for some time for brightness change

if __name__ == "__main__":
    # Script code goes here
    led_setup()  # Initialize LED setup
    while True:
        led_brightness()  # Increase brightness
