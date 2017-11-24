import json
import paho.mqtt.client as mqtt
from rasp_control import *

import logging
logging.basicConfig(
    format = "%(asctime)s %(filename)s: %(lineno)d %(levelname)s %(message)s",
    datefmr = "%m-%d %H:%M:%S",
    level = logging.INFO)

DEV_NAME = "light"
TOPIC_UPLOAD = "/%(DEV_NAME)s/upload"%globals()
TOPIC_GET = "/%(DEV_NAME)s/get"%globals()
MQTT_SERVER_HOST = "139.199.191.81"
MQTT_SERVER_PORT = 1883

def on_connect(client, userdata, flags, rc):
    logging.info("connected with result code: %(rc)s"%vars())
    logging.info("now subscribe topic: %(TOPIC_GET)s"%globals())
    logging.info(client.subscribe(TOPIC_GET))

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload
    logging.info("topic: %(topic)s, payload: %(payload)s"%vars())
    payload = json.loads(payload)
    if payload["action"] == "open":
        led_control(GPIO.HIGH)
    elif payload["action"] == "close":
        led_control(GPIO.LOW)
    elif payload["action"] == "color":
        led_blink(PIN=7)

led_control(PIN=7)
led_control(PIN=8)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER_HOST, MQTT_SERVER_PORT, 60)

client.loop_forever()
