"""
Example showing how to erase stored face IDs
"""

import time
from person_sensor import PersonSensor

sensor = PersonSensor(bus=0, sda=8, scl=9)

sensor.enable_id_model(1)
sensor.persist_ids(True)

# Not sure if the delay before erase is needed, but a delay after the erase certainly is
time.sleep_ms(1000)
sensor.erase_ids()
time.sleep_ms(1000)
