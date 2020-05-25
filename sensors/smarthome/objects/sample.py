from smarthome.objects.controllerinfo import ControllerInfo
from smarthome.objects.sensorinfo import SensorInfo


class Sample:
    def __init__(self, measurement_name: str, sensor: SensorInfo, value: any, time: any):
        self.measurement_name = measurement_name
        self.sensor = sensor
        self.value = value
        self.time = time

    def data(self, controller_info: ControllerInfo):
        return {
            "measurement": "temperature",
            "tags": {
                "device_name": controller_info.name,
                "device_model": controller_info.model,
                "sensor_id": self.sensor.id,
                "sensor_location": self.sensor.location,
                "sensor_model": self.sensor.model,
            },
            "fields": {
                "value": self.value
            },
            "time": self.time
        }
