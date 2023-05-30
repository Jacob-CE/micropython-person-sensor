"""
Simple example show how to read faces from the sensor
"""

import time
from person_sensor import PersonSensor

sensor = PersonSensor(bus=0, sda=8, scl=9)

while True:
    faces = sensor.read_faces()
    print(faces)    
    time.sleep(0.2)
