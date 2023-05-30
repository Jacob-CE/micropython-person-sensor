"""
Example showing how to ID faces
"""
import time
from person_sensor import PersonSensor

sensor = PersonSensor(bus=0, sda=8, scl=9)

sensor.enable_id_model(1)
sensor.persist_ids(True)
did_label = False
while True:
    faces = sensor.read_faces()
    
    if len(faces):
        face = faces[0]
        print(faces[0])
        if face['is_facing'] and face['id'] == -1 and not did_label:
            print('Found unlabelled face, labelling it in next frame')
            sensor.label_next_id()
            did_label = True

    time.sleep(0.2)
