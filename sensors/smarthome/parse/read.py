import json
from typing import List

from smarthome.db.db import DB
from smarthome.db.influxdb import InfluxDB
from smarthome.objects.controllerinfo import ControllerInfo
from smarthome.objects.dbs import INFLUXDB
from smarthome.objects.readers import DHT, DHT_LEGACY
from smarthome.objects.sensorinfo import SensorInfo
from smarthome.sensors.dht import DHTSensor
from smarthome.sensors.dht_legacy import DHTLegacySensor
from smarthome.sensors.sensor import Sensor
from smarthome.server.server import Server


def read_json(filepath: str) -> Server:
    with open(filepath) as f:
        data = json.load(f)
    print(data)

    assert "sample_rate_sec" in data, "missing sample_rate_sec"
    poll_rate = data["sample_rate_sec"]
    controller = read_controller_json(data)
    sensors = read_sensors_json(data)
    dbs = read_dbs_json(data)
    return Server(controller, sensors, dbs, poll_rate)


def read_controller_json(data: dict) -> ControllerInfo:
    assert "controller" in data, "missing controller"
    cdata = data["controller"]
    assert "name"  in cdata, "missing name"
    assert "model"  in cdata, "missing model"
    name = cdata["name"]
    model = cdata["model"]
    return ControllerInfo(name, model)


def read_sensors_json(data: dict) -> List[Sensor]:
    assert "sensors" in data, "missing sensors"
    sensor_configs = data["sensors"]
    sensors: List[Sensor] = [read_sensor(config) for config in sensor_configs]
    return sensors


def read_sensor(data: dict) -> Sensor:
    assert "model" in data, "missing model"
    assert "id"  in data, "missing id"
    assert "location"  in data,"missing location"
    assert "reader" in data,"missing reader"
    assert "parse"  in data, "missing parse"
    model = data["model"]
    id = data["id"]
    location = data["location"]
    reader = data["reader"]
    config = data["parse"]
    info = SensorInfo(model, id, location)

    if reader == DHT:
        assert "pin" in config, "missing pin"
        assert "retries" in config, "missing retries"
        pin = config["pin"]
        retires = config["retries"]
        return DHTSensor(info, pin, retires)
    elif reader == DHT_LEGACY:
        assert "pin" in config, "missing pin"
        pin = config["pin"]
        return DHTLegacySensor(info, pin)
    else:
        raise


def read_dbs_json(data: dict) -> List[DB]:
    assert "db" in data, "missing db"
    configs = data["db"]
    dbs: List[DB] = [read_db(config) for config in configs]
    return dbs


def read_db(data: dict) -> DB:
    assert "type" in data, "missing type"
    assert "parse"  in data, "missing parse"
    db_type = data["type"]
    config = data["parse"]
    if db_type == INFLUXDB:
        assert "host"  in config, "missing host"
        assert "port"  in config, "missing port"
        assert "username"  in config, "missing username"
        assert "password"  in config, "missing password"
        assert "database"  in config, "missing database"
        host = config["host"]
        port = config["port"]
        username = config["username"]
        password = config["password"]
        database = config["database"]
        return InfluxDB(host, port, username, password, database)
    else:
        raise
