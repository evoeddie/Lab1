#ME 405 Lab 1 Week 5

# pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
# tim2 = pyb.Timer(2, freq=1000)
# ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)
# ch1.pulse_width_percent(90)


def led_setup():
pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
tim2 = pyb.Timer(2, freq=1000)
ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)

def led_bightness(self):
ch1.pulse_width_percent(90)

if __name__ = "__main__":
    
led_setup()
while True:
    duty = 0
    led_brightness(duty)
    sleep(
    i += 1
