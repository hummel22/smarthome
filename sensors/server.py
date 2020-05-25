import os

from smarthome.parse.read import read_json

CONFIG_FILE = os.getenv('SMARTHOME_SERVER_CONFIG')

if CONFIG_FILE is None:
    print("SMARTHOME_SERVER_CONFIG env variable does not exists")

server = read_json(CONFIG_FILE)
server.run()
