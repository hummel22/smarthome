import time
from typing import List

from smarthome.db.db import DB
from smarthome.objects.controllerinfo import ControllerInfo
from smarthome.sensors.sensor import Sensor


class Server():
    def __init__(self, controller: ControllerInfo, sensors: List[Sensor], dbs: List[DB], sample_period: int):
        self.controller = controller
        self.sensors = sensors
        self.dbs = dbs
        self.sample_period = sample_period

    def run(self):
        while True:
            results = []
            for sensor in self.sensors:
                data = sensor.read()
                results.extend(data)

            if results is not None:
                for db in self.dbs:
                    db.write(results, self.controller)
            else:
                print("no data returned")

            time.sleep(self.sample_period)
