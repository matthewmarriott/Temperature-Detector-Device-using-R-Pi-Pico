import machine
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    utime.sleep(3)
    
    # this is a project to program a temperature sensor
    # it measures the Vbe voltage of a biased dual polar diode
    # typically Vbe = 0.706V at 27 degrees Centigrade, with a slope of -1.721mV (0.001721V)
    # By Matthew Marriott 2022
    # Uses Thonny with Micropython
