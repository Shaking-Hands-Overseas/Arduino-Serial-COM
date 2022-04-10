import unittest

from ..src import *


class test_sender(unittest.TestCase, Sender):
    config = {"serial_port": "3", "Mode": "", "BAUDRATE": 9600,
                   "Networking": {"API_URL": "https://development-sho.herokuapp.com/1", "URL_R": "/receiver",
                                  "URL_S": "/servo", "URL_C": "/custom",
                                  "DATA_TEMPLATE": {"s1": 200, "s2": 200, "s3": 200, "s4": 200, "s5": 200},
                                  "PREFERRED_ORDER": {"F1": "s1", "F2": "s2", "F3": "s3", "F4": "s4", "F5": "s5"}}}
    Networking = config["Networking"]

    def test_ArduinoConnect(self):
        ard = Serial(port="COM4", baudrate=115200, timeout=.1)
        ard.write(bytes("A", 'utf-8'))
        ard.readline().decode('utf-8')

    def test_server_post_servo(self):
        post("https://development-sho.herokuapp.com/1/servo", self.Networking["DATA_TEMPLATE"])

    def test_server_post_custom(self):
        post("https://development-sho.herokuapp.com/1/custom", self.Networking["PREFERRED_ORDER"])

    def test_server_get(self):
        x = get("https://development-sho.herokuapp.com/1/receiver")
        self.ct = json.loads(x.content.decode())


if __name__ == '__main__':
    unittest.main()
