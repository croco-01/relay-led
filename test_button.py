import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button(channel):
    print("GPIO18 event:", GPIO.input(channel), flush=True)

GPIO.add_event_detect(
    18,
    GPIO.BOTH,
    callback=button,
    bouncetime=100
)

print("Waiting for GPIO18...", flush=True)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
