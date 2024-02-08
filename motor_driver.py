from MotorDriver1 import motordriver
import pyb


if __name__ == '__main__':
    
    moe = motordriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
 
    moe.set_duty_cycle (-20)
    # Wait for a certain duration (e.g., 5 seconds)
    pyb.delay(5000)  # 5000 milliseconds = 5 seconds
      
    # Stop the motor by setting the duty cycle to 0
    moe.set_duty_cycle(0)
      
    # Wait for a certain duration (e.g., 5 seconds)
    pyb.delay(1000)  # 5000 milliseconds = 5 seconds
      
    moe.set_duty_cycle(3000)
      
    # Wait for a certain duration (e.g., 5 seconds)
    pyb.delay(5000)  # 5000 milliseconds = 5 seconds
      
    # Stop the motor by setting the duty cycle to 0
    moe.set_duty_cycle(0)