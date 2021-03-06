import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_SENSOR11 = Adafruit_DHT.DHT11
DHT_PIN1 = 17
DHT_PIN2 = 27
DHT_PIN3 = 27

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN1)
    temperature = temperature * (9 / 5) + 32

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensors")

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN2)
    temperature = temperature * (9 / 5) + 32

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensors")
