from typing import List

from influxdb import InfluxDBClient

from smarthome.db.db import DB
from smarthome.objects.controllerinfo import ControllerInfo
from smarthome.objects.sample import Sample


class InfluxDB(DB):
  def __init__(self, host: str, port: int, username: str, password: str, database: str):
    self.host = host
    self.port = port
    self.username = username
    self.password = password
    self.database = database
    self.client = client = InfluxDBClient(host=host, port=port, username=username, password=password, database=database)

  def write(self, data: List[Sample], controller: ControllerInfo):
    self.client.write_points([d.data(controller) for d in data], database=self.smarthome)
