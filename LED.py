#ME 405 Lab 1 Week 5

# pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
# tim2 = pyb.Timer(2, freq=1000)
# ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)
# ch1.pulse_width_percent(90)

#bobobobo
import time

def led_setup():
    pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer(2, freq=10000)
    ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)

def led_bightness(duty):
    ch1 = pyb.Timer(2).channel(1)
    ch1.pulse_width_percent(duty)

if __name__ == "__main__":
    
    led_setup()
    duty = 100
    i = 0
    while True:
        led_bightness(duty)
        time.sleep(.1)
        duty += -2
        i+= 1
        if i >= 50:
            duty = 100
            i=0
            led_bightness(duty)
            time.sleep(1)
        
            
        
        
            
