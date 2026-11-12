from machine import I2C, Pin
import time
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=50000)
ok = bad = 0
for _ in range(50):
    try:
        i2c.writeto(0x27, bytes([0x08]))
        ok += 1
    except OSError:
        bad += 1
    time.sleep_ms(20)
print("ok:", ok, "bad:", bad)