from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=2, echo_pin=3, echo_timeout_us=10000)

while True:
    try:
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm')
    except OSError as e:
        print('Error:', e)
    sleep(1)