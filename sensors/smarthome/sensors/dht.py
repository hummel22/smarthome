import time
from datetime import datetime
from typing import List

import adafruit_dht

from smarthome.objects.measurements import HUMIDITY, TEMPERATURE
from smarthome.objects.models import MODEL_DHT22, MODEL_DHT11
from smarthome.objects.sample import Sample
from smarthome.objects.sensorinfo import SensorInfo
from smarthome.sensors.sensor import Sensor


class DHTSensor(Sensor):
    def __init__(self, sensor: SensorInfo, pin: any, retries: int):
        self.sensorInfo = sensor
        self.pin = pin
        self.retries = retries
        if sensor.model == MODEL_DHT22:
            self.dht_device = adafruit_dht.DHT22(pin, use_pulseio=False)
        elif sensor.model == MODEL_DHT11:
            self.dht_device = adafruit_dht.DHT11(pin, use_pulseio=False)
        else:
            raise

    def read(self) -> List[Sample]:
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        print("read dht sensor")
        attempts = 0
        while attempts < self.retries:
            try:
                # self.dht_device.measure()
                # Print the values to the serial port
                temperature_c = self.dht_device.temperature
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = self.dht_device.humidity
                print(
                    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                        temperature_f, temperature_c, humidity
                    )
                )
                return [
                    Sample(HUMIDITY, self.sensorInfo, humidity, current_time),
                    Sample(TEMPERATURE, self.sensorInfo, temperature_c, current_time),
                ]
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                attempts = attempts + 1
                continue
            except Exception as error:
                print(error)
                return []

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)
