import unittest
from serial import Serial
import json
from requests import get, post
class test_sender(unittest.TestCase):
    config = {"serial_port": "3", "Mode": "", "BAUDRATE": 9600,
                   "Networking": {"API_URL": "", "URL_R": "/receiver",
                                  "URL_S": "/servo", "URL_C": "/custom",
                                  "DATA_TEMPLATE": {"s1": 200, "s2": 200, "s3": 200, "s4": 200, "s5": 200},
                                  "PREFERRED_ORDER": {"F1": "s1", "F2": "s2", "F3": "s3", "F4": "s4", "F5": "s5"}}}
    Networking = config["Networking"]

    def test_ArduinoConnect(self):
        ard = Serial(port="COM4", baudrate=115200, timeout=.1)
        ard.write(bytes("A", 'utf-8'))
        ard.readline().decode('utf-8')

    def test_server_post_servo(self):
        post(f'{self.Networking["API_URL"]}/custom/servo', self.Networking["DATA_TEMPLATE"])

    def test_server_post_custom(self):
        post(f'{self.Networking["API_URL"]}/custom', self.Networking["PREFERRED_ORDER"])

    def test_server_get(self):
        x = get(f'{self.Networking["API_URL"]}/receiver')
        self.ct = json.loads(x.content.decode())


if __name__ == '__main__':
    unittest.main()
