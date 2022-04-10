
from .Global import *


def receiver_launcher(selection, ard):
    print(f"{bcolors.HEADER}[INFO] Starting Receiver{bcolors.ENDC}")
    receiver = Receiver(selection, ard)
    receiver_server_thread = threading.Thread(target=receiver.receiver_server, args=())
    print("[INFO] Starting Receiver Server Thread")
    receiver_server_thread.start()
    receiver_arduino_thread = threading.Thread(target=receiver.receiver_arduino, args=())
    print("[INFO] Starting Receiver Arduino Thread")
    receiver_arduino_thread.start()
    print(f"{bcolors.HEADER}[INFO] Initialization Finalized Successfully{bcolors.ENDC}")
    print("---------- LOG DATA ----------")


class Receiver:
    def __init__(self, config, ard):
        Networking = config["Networking"]
        self.URL_R = Networking["API_URL"] + Networking["URL_R"]
        self.selection = config["Mode"]
        self.ard = ard
        self.i = 0
        self.ser = True
        self.BAUDRATE = config["BAUDRATE"]
        self.DATA_TEMPLATE = Networking["DATA_TEMPLATE"]
        self.ct = Networking["DATA_TEMPLATE"]
        self.PREFERED_ORDER = Networking["PREFERED_ORDER"]
        self.data = list(self.DATA_TEMPLATE)

    def write_read(self, x):
        self.ard.write(bytes(x, 'utf-8'))
        sleep(0.05)
        return self.ard.readline()

    def get_server(self):
        req = get(self.URL_R)
        return req

    def receiver_server(self):
        sleep(2)
        while True:
            if self.ser:
                sleep(0.05)
                try:
                    x = self.get_server()
                    try:
                        self.ct = json.loads(x.content.decode())  # Convert JSON => Dictionary Python
                    except Exception:
                        print(f"{bcolors.WARNING}[ERROR] Error while Jsonifying content {bcolors.ENDC}")
                        self.ct = self.DATA_TEMPLATE
                except Exception:
                    print(f"{bcolors.WARNING}[ERROR] Error while connecting to the server {self.URL_R} {bcolors.ENDC}")
                    self.ct = self.DATA_TEMPLATE

    def receiver_arduino(self):
        sleep(2)
        while True:
            sleep(0.05)
            print(self.ct)
            for index in self.data:
                if int(self.ct[index]) < 10:  # If the number is lower than 10
                    self.ct[index] = f"00{int(self.ct[index])}"  # We add two zeros to the data

                elif int(self.ct[index]) < 100:  # If the number is lower than 100
                    self.ct[index] = f"0{int(self.ct[index])}"  # We add one zero to the data
            num = str(f'{self.ct["s1"]}{self.ct["s2"]}{self.ct["s3"]}{self.ct["s4"]}{self.ct["s5"]}')  # The String That will be sent to the arduino with the information
            try:
                value = self.write_read(num)
            except Exception:
                print(f"{bcolors.WARNING}[ERROR] Error while sending data to arduino in port {SERIAL_PORTS[int(self.selection)]}{bcolors.ENDC}")
                try:
                    self.ard = arduino_connect(int(self.selection), self.BAUDRATE)
                except Exception:
                    self.i += 1
                    if self.i > 10:
                        print('\n\n')
                        self.ser = False
                        sleep(0.6)
                        self.selection = ask_user_port()
                        try:
                            self.ard = arduino_connect(int(self.selection), self.BAUDRATE)
                            self.ser = True
                        except Exception:
                            pass
