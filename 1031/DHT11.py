import Adafruit_DHT

class DHT11:
    def __init__(self):
        self.senser = Adafruit_DHT.DHT11
        self.pin = 23
    
    def getNow(self):
        hum, temp = Adafruit_DHT.read_retry(self.senser, self.pin)
        print(temp, hum)
        return [temp, hum]