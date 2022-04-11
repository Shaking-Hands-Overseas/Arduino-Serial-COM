from .Global import *


def receiver_launcher(config, ard):
    """
    Launches The receiver threads
    :param config: Dictionary containing the config file
    :type config: dict
    :param ard: Arduino object
    :type ard: ard object
    :return: None
    :rtype: None
    """
    print(f"{bcolors.HEADER}[INFO] Starting Receiver{bcolors.ENDC}")
    receiver = Receiver(config, ard)
    print("[INFO] Starting Receiver Threads")
    threading.Thread(target=receiver.receiver_server, args=()).start()
    threading.Thread(target=receiver.receiver_arduino, args=()).start()
    print(f"{bcolors.HEADER}[INFO] Initialization Finalized Successfully{bcolors.ENDC}")
    print("---------- LOG DATA ----------")


class Receiver:
    def __init__(self, config, ard):
        Networking = config["Networking"]
        self.URL_R = Networking["API_URL"] + Networking["URL_R"]
        self.URL_B = Networking["API_URL"] + Networking["URL_B"]
        self.selection = config["Mode"]
        self.ard = ard
        self.i = 0
        self.ok = True
        self.BAUDRATE = config["BAUDRATE"]
        self.DATA_TEMPLATE = Networking["DATA_TEMPLATE"]
        self.BUTTONS = Networking["BUTTONS_TEMPLATE"]
        self.ct = Networking["DATA_TEMPLATE"]
        self.PREFERRED_ORDER = Networking["PREFERRED_ORDER"]
        self.data = list(self.DATA_TEMPLATE)

    def write_read(self, x):
        """
        Writes and reads data from the arduino
        :param x: Data Sent to the arduino
        :type x: string
        :return: Data Received from the arduino
        :rtype: string
        """
        self.ard.write(bytes(x, 'utf-8'))
        sleep(0.05)
        return self.ard.readline()

    def receiver_server(self):
        """
        Server Thread. Gets the data stored in the server and stores it into the variable self.ct
        :return: None
        :rtype: None
        """
        sleep(2)
        while True:
            if self.ok:
                try:
                    response = get(self.URL_R)
                    print(f"{bcolors.OKCYAN}[SERVER]{bcolors.ENDC} Response from server: {response.status_code}")
                    self.ct = json.loads(response.content.decode())
                except json.decoder.JSONDecodeError:
                    print(f"{bcolors.WARNING}[ERROR] Error while connecting to the server {self.URL_R} {bcolors.ENDC}")
                    self.ct = self.DATA_TEMPLATE
            else:
                sleep(1)

    def receiver_arduino(self):
        """
        Arduino Thread. Sends the data to the arduino from the variable self.ct
        :return: None
        :rtype: None
        """
        sleep(2)
        while True:
            sleep(0.05)
            print(f"{bcolors.OKGREEN}[ARDUINO]{bcolors.ENDC}{self.ct}")
            for key, value in self.ct.items():
                if len(str(int(value))) == 1:
                    self.ct[key] = "00" + str(int(value))
                elif len(str(int(value))) == 2:
                    self.ct[key] = "0" + str(int(value))
            To_send = "".join(str(x) for x in self.ct.values())
            try:
                received = self.write_read(To_send).split()
                for value_index, value in enumerate(received):
                    self.BUTTONS[f"b{value_index + 1}"] = int(value)
                post(self.URL_B, self.BUTTONS)
            except Exception:
                print(f"{bcolors.WARNING}[ERROR] Error while sending data to arduino in port {SERIAL_PORTS[int(self.selection)]}{bcolors.ENDC}")
                try:
                    self.ard = arduino_connect(int(self.selection), self.BAUDRATE)
                except Exception:
                    self.i += 1
                    if self.i > 10:
                        print('\n\n')
                        self.ok = False
                        sleep(0.6)
                        self.selection = ask_user_port()
                        try:
                            self.ard = arduino_connect(int(self.selection), self.BAUDRATE)
                            self.ok = True
                        except Exception:
                            pass
