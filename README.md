# micropython-person-sensor

MicroPython implementation for the Person Sensor by Useful Sensors (https://core-electronics.com.au/catalog/product/view/sku/SEN-21231)

Harware documentation: https://github.com/usefulsensors/person_sensor_docs/blob/main/README.md


## Usage
```
import time
from person_sensor import PersonSensor

sensor = PersonSensor(bus=0, sda=8, scl=9)

while True:
    faces = sensor.read_faces()
    print(faces)    
    time.sleep(0.2)
```