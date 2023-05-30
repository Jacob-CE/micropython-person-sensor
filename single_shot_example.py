"""
Example showing how to use the sensor in single-shot mode
"""

import time
from person_sensor import PersonSensor

sensor = PersonSensor(bus=0, sda=8, scl=9)

sensor.set_mode(0)  # Set to single shot mode

last_shot = 0
while True:
    # Run inference once every 5 seconds
    if time.time() - last_shot > 5:
        print('Take single shot')
        sensor.single_shot()
        last_shot = time.time()
    
    faces = sensor.read_faces()

    print(faces)
    
    time.sleep(0.2)