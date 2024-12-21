import RPi.GPIO as GPIO 
import time

# Pin configuration
RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

def traffic_light_sequence():
    try:
        while True:
            # Red light
            GPIO.output(RED_PIN, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(RED_PIN, GPIO.LOW)

            # Yellow light
            GPIO.output(YELLOW_PIN, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(YELLOW_PIN, GPIO.LOW)

            # Green light
            GPIO.output(GREEN_PIN, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(GREEN_PIN, GPIO.LOW)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    traffic_light_sequence()