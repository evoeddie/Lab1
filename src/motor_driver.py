import MotorDriver


if __name__ == '__main__':
    print(MotorDriver)
    moe = MotorDriver.motordriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    moe.set_duty_cycle (42)
    