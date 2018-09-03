import machine
import utime

pin0 = machine.Pin(0, machine.Pin.OUT)
pin2 = machine.Pin(2, machine.Pin.OUT)

while True:
    for i in range(0, 10):
        pin0.off()
        pin2.on()
        utime.sleep_ms(60)
        pin0.on()
        pin2.off()
        utime.sleep_ms(60)
    pin0.on()
    pin2.on()
    utime.sleep_ms(500)
