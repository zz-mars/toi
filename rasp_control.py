import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import sys

import logging
logging.basicConfig(
    format = "%(asctime)s %(filename)s: %(lineno)d %(levelname)s %(message)s",
    datefmr = "%m-%d %H:%M:%S",
    level = logging.INFO)

def led_control(value=GPIO.LOW, PIN=8):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, value)

def led_blink(interval=1, count=1, PIN=8):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    for i in range(count):
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(interval)
    GPIO.cleanup()

def get_temp():
    sensor = Adafruit_DHT.AM2302
    PIN = 2
    humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
    return (humidity, temperature)

if __name__ == "__main__":
    humidity, temperature = get_temp()
    logging.info("humidity => %(humidity).1f%%"%vars())
    logging.info("temperature => %(temperature).1f*C"%vars())
    sys.exit(0)
    led_control(GPIO.HIGH)
    time.sleep(1)
    led_control(GPIO.LOW)
    time.sleep(1)

    led_control(GPIO.HIGH, PIN=7)
    time.sleep(1)
    led_control(GPIO.LOW, PIN=7)
    time.sleep(1)
    
    led_blink()
