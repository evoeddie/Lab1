from MotorDriver import motordriver
import pyb


if __name__ == '__main__':
    
     moe = motordriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
     moe.set_duty_cycle (50)
    