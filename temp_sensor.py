import json
import time
import paho.mqtt.client as mqtt
from rasp_control import *
from config import *

import logging
logging.basicConfig(
    format = "%(asctime)s %(filename)s: %(lineno)d %(levelname)s %(message)s",
    datefmr = "%m-%d %H:%M:%S",
    level = logging.INFO)

DEV_NAME = "switch"
TOPIC_UPLOAD = "/%(DEV_NAME)s/upload"%globals()
TOPIC_GET = "/%(DEV_NAME)s/get"%globals()

client = mqtt.Client()
client.connect(MQTT_SERVER_HOST, MQTT_SERVER_PORT, 60)

while True:
    humidity, temperature = get_temp()
    if temperature == None:
        logging.info("get temperature fail, sleep and continue..")
        time.sleep(3)
        continue
    payload = {"temp": int(temperature) }
    payload = json.dumps(payload)
    logging.info("publish to topic: %s, payload: %s"%(TOPIC_UPLOAD, payload))
    logging.info(client.publish(TOPIC_UPLOAD, payload=payload, qos=1))
    time.sleep(60)
