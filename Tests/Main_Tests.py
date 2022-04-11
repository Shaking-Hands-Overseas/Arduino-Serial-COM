import unittest
import os
from serial import Serial
from json import loads, load
from requests import get, post
class test_sender(unittest.TestCase):
    with open(os.path.join(os.getcwd(), "sho_config.json"), "r") as f:
        config = load(f)
    Networking = config["Networking"]
    def test_ArduinoConnect(self):
        ard = Serial(port="COM4", baudrate=115200, timeout=.1)
        ard.write(bytes("A", 'utf-8'))
        ard.readline().decode('utf-8')

    def test_server_post_servo(self):
        post(f'{self.Networking["API_URL"]}/servo', self.Networking["DATA_TEMPLATE"])

    def test_server_post_custom(self):
        post(f'{self.Networking["API_URL"]}/custom', self.Networking["PREFERRED_ORDER"])

    def test_server_get(self):
        get(f'{self.Networking["API_URL"]}/receiver')

    def test_jsonfy(self):
        _dict = loads(get(f'{self.Networking["API_URL"]}/receiver').content.decode())
        for key, value in _dict.items():
            if len(str(int(value))) == 1:
                _dict[key] = "00" + str(int(value))
            elif len(str(int(value))) == 2:
                _dict[key] = "0" + str(int(value))
        To_send = "".join(str(x) for x in _dict.values())

if __name__ == '__main__':
    unittest.main()
