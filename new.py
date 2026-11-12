# # IR obstacle sensor test - Raspberry Pi Pico 2 W (MicroPython)
# #
# # Wiring (typical 3-pin IR obstacle module, e.g. FC-51):
# #   VCC -> 3V3 (pin 36)
# #   GND -> GND (pin 38)
# #   OUT -> GP15 (pin 20)  <- change IR_PIN below if you use another pin
# #
# # Most modules pull OUT LOW when an object is detected (active-low).
# # If yours is the opposite, set ACTIVE_LOW = False.

# from machine import Pin
# import time

# IR_PIN = 15
# ACTIVE_LOW = True
# DEBOUNCE_MS = 50        # a state change must hold this long to count
# POLL_MS = 10

# ir = Pin(IR_PIN, Pin.IN)
# led = Pin("LED", Pin.OUT)   # onboard LED on Pico 2 W


# def detected():
#     v = ir.value()
#     return (v == 0) if ACTIVE_LOW else (v == 1)


# def stable_read(prev):
#     """Return the new state only if it has held for DEBOUNCE_MS."""
#     now = detected()
#     if now == prev:
#         return prev
#     t0 = time.ticks_ms()
#     while time.ticks_diff(time.ticks_ms(), t0) < DEBOUNCE_MS:
#         if detected() != now:
#             return prev          # bounced back, ignore
#         time.sleep_ms(1)
#     return now


# print("IR sensor test on GP%d (active-%s). Wave a hand in front of it." %
#       (IR_PIN, "LOW" if ACTIVE_LOW else "HIGH"))
# print("Press Ctrl+C to stop.\n")

# state = detected()
# count = 0
# print("Initial state:", "OBJECT" if state else "clear")
# led.value(1 if state else 0)

# # try:
# #     while True:
# #         new = stable_read(state)
# #         if new != state:
# #             state = new
# #             led.value(1 if state else 0)
# #             if state:
# #                 count += 1
# #                 print("[%8d ms] OBJECT detected   (count=%d)" % (time.ticks_ms(), count))
# #             else:
# #                 print("[%8d ms] clear" % time.ticks_ms())
# #         time.sleep_ms(POLL_MS)
# # except KeyboardInterrupt:
# #     led.value(0)
# #     print("\nStopped. Total detections:", count)

# from machine import Pin
# import time
# ir = Pin(15, Pin.IN)
# while True:
#     print(ir.value())
#     time.sleep(0.2)


# from machine import Pin
# import time

# # Setup MH-B IR sensor on GP2 (Physical Pin 4)
# ir_sensor = Pin(2, Pin.IN)

# def is_spot_occupied_raw():
#     # Active-LOW: 0 means car detected, 1 means spot empty
#     return ir_sensor.value() == 0

# def is_spot_occupied_debounced(samples=3, delay_ms=100):
#     # Requires 3 consecutive identical readings (Task 1.5)
#     first = is_spot_occupied_raw()
#     for _ in range(samples - 1):
#         time.sleep_ms(delay_ms)
#         if is_spot_occupied_raw() != first:
#             return None  # Still transitioning / unstable
#     return first

# # Main test loop (Task 1.1 & 1.2 calibration)
# while True:
#     raw_val = ir_sensor.value()
#     occupied = is_spot_occupied_debounced()
#     if occupied is not None:
#         print(f"Raw Pin: {raw_val} | Occupied: {occupied}")
#     time.sleep(0.2)