from datetime import datetime
from typing import List

import Adafruit_DHT

from smarthome.objects.measurements import HUMIDITY, TEMPERATURE
from smarthome.objects.models import MODEL_DHT22, MODEL_DHT11
from smarthome.objects.sample import Sample
from smarthome.objects.sensorinfo import SensorInfo
from smarthome.sensors.sensor import Sensor


class DHTLegacySensor(Sensor):
    def __init__(self, sensor: SensorInfo, pin: int):
        self.sensorInfo = sensor
        self.pin = pin
        if sensor.model == MODEL_DHT22:
            self.dht_sensor = Adafruit_DHT.DHT22
        elif sensor.model == MODEL_DHT11:
            self.dht_sensor = Adafruit_DHT.DHT11
        else:
            raise

    def read(self) -> List[Sample]:
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        humidity, temperature_c = Adafruit_DHT.read_retry(self.dht_sensor, self.pin)
        temperature = temperature_c * (9 / 5) + 32
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temperature, humidity))
            return [
                Sample(HUMIDITY, self.sensorInfo, humidity, current_time),
                Sample(TEMPERATURE, self.sensorInfo, temperature_c, current_time),
            ]
        else:
            print("Failed to retrieve data from humidity sensors")
            return []

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)
