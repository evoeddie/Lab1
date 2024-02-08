"""! @file motor_driver.py
This script demonstrates the control of a motor using the MotorDriver class.
"""

from MotorDriver1 import motordriver
import pyb

if __name__ == '__main__':
    # Initialize motor driver
    moe = motordriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    
    # Set duty cycle to -20
    moe.set_duty_cycle(-20)
    
    # Wait for a certain duration (e.g., 5 seconds)
    pyb.delay(5000)  # 5000 milliseconds = 5 seconds
      
    # Stop the motor by setting the duty cycle to 0
    moe.set_duty_cycle(0)
      
    # Wait for a certain duration (e.g., 1 second)
    pyb.delay(1000)  # 1000 milliseconds = 1 second
      
    # Set duty cycle to 3000
    moe.set_duty_cycle(3000)
      
    # Wait for a certain duration (e.g., 5 seconds)
    pyb.delay(5000)  # 5000 milliseconds = 5 seconds
      
    # Stop the motor by setting the duty cycle to 0
    moe.set_duty_cycle(0)
