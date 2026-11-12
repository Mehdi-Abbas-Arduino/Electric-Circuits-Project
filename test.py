from machine import Pin
from time import sleep

LED = Pin(28 , Pin.OUT)

LED.value(1)

sleep(2)
LED.value(0)