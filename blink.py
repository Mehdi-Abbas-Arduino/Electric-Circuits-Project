# from machine import Pin, time_pulse_us
# from utime import sleep ,sleep_us 

# ULTRA_PIN_Trigger = 2
# ULTRA_PIN_Echo = 3
# # VBUS = 40


# ULTRA_PIN_Echo_pin = Pin(ULTRA_PIN_Echo,Pin.IN)
# ULTRA_PIN_Trigger_pin = Pin(ULTRA_PIN_Trigger,Pin.OUT)

# def func():
#     ULTRA_PIN_Trigger_pin.low()
#     sleep_us(2)
#     ULTRA_PIN_Trigger_pin.high()
#     sleep_us(10)
#     ULTRA_PIN_Trigger_pin.low()
#     t = time_pulse_us(ULTRA_PIN_Echo_pin,1,30000)
#     if t < 0:
#         return None
#     return (t*0.03430) / 2


# while True:
#     d = func()
#     print("No Echo" if d is None else f"Distance{d}")
#     sleep(0.5)
# 6
# # from machine import Pin , I2C
# # from ssd1306 import SSD1306_I2C

# # i2c = I2C(0 , scl = Pin(1) , sda = Pin(0))

# # oled = SSD1306_I2C(128 , 64 , i2c)
# # oled.fill(0)
# # oled.text("Hello" , 10 , 25)
# # oled.show()

# from machine import Pin, time_pulse_us
# from time import sleep, sleep_us

# TRIG = Pin(3, Pin.OUT)   # your trigger GPIO
# ECHO = Pin(2, Pin.IN)    # your echo GPIO

# print("ECHO idle level:", ECHO.value())   # should be 0

# while True:
#     TRIG.value(0); sleep_us(2)
#     TRIG.value(1); sleep_us(10)
#     TRIG.value(0)
#     t = time_pulse_us(ECHO, 1, 30000)
#     print("t =", t)
#     sleep(0.5)

from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=3, echo_pin=2, echo_timeout_us=30000)

while True:
    try:
        d = sensor.distance_cm()
        print("Distance:", d, "cm")
    except OSError as e:
        print("No echo:", e)
    sleep(0.5)