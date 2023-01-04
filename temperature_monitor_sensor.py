# Temperature Monitoring Sensor - Climate Science Deployable

import utime
from machine import Pin

led = Pin(25, Pin.OUT)
relay = Pin(22, Pin.OUT)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

led.low()
relay.high()
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    utime.sleep(2)
    print(temperature)
    if temperature > 20.1:
        led.high()
        relay.low()
    elif temperature < 16.1:
        led.low()
        relay.high()
    
    # this is a project to program a temperature sensor
    # it measures the Vbe voltage of a biased dual polar diode
    # typically Vbe = 0.706V at 27 degrees Centigrade, with a slope of -1.721mV (0.001721V)
    # By Matthew Marriott 2022
    # Uses Thonny with Micropython
