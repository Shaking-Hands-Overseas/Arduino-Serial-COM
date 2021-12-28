from requests import get
from requests.models import encode_multipart_formdata
from .Global import *
from json import loads
from time import sleep
import threading


def receiver_launcher(selection, ard):
    print(f"{bcolors.HEADER}[INFO] Starting Receiver{bcolors.ENDC}")
    receiver = Receiver(selection, ard)
    print(f"{bcolors.OKGREEN}[INFO] Object from Receiver Class Has been created{bcolors.ENDC}")
    print("[INFO] Creating Receiver Server Thread")
    receiver_server_thread = threading.Thread(target=receiver.receiver_server, args=())
    print("[INFO] Starting Receiver Server Thread")
    receiver_server_thread.start()
    print(f"{bcolors.OKGREEN}[INFO] Receiver Server Thread Created and Initialized{bcolors.ENDC}")
    print("[INFO] Creating Receiver Arduino Thread")
    receiver_arduino_thread = threading.Thread(target=receiver.receiver_arduino, args=())
    print("[INFO] Starting Receiver Arduino Thread")
    receiver_arduino_thread.start()
    print(f"{bcolors.OKGREEN}[INFO] Receiver Arduino Thread Created and Initialized{bcolors.ENDC}")
    print(f"{bcolors.HEADER}[INFO] Initialization Finalized Successfully{bcolors.ENDC}")
    print("---------- LOG DATA ----------")


class Receiver:
    def __init__(self, selection, ard):
        self.selection = selection
        self.ard = ard
        self.i = 0
        self.ser = True
        self.ct = {"s1": 200, "s2": 200, "s3": 200, "s4": 200, "s5": 200}

    def write_read(self, x):
        data1 = bytes(x, 'utf-8')
        # print(data1)
        self.ard.write(data1)
        sleep(0.25)
        data = self.ard.readline()
        return data

    @staticmethod
    def get_server():
        req = get(URL_R)
        if req.status_code == "500":
            print(f"{bcolors.WARNING}[ERROR] Received status code 500{bcolors.ENDC}")
        return req

    def receiver_server(self):
        sleep(2)
        self.ser = True
        while True:
            if self.ser:
                sleep(0.1)
                try:
                    x = self.get_server()
                    try:
                        self.ct = loads(x.content.decode())  # Convert JSON => Dictionary Python
                    except Exception:
                        print(f"{bcolors.WARNING}[ERROR] Error while Jsonifying content {bcolors.ENDC}")
                        self.ct = {"s1": 200, "s2": 200, "s3": 200, "s4": 200, "s5": 200}
                except Exception:
                    print(f"{bcolors.WARNING}[ERROR] Error while connecting to the server {URL_R} {bcolors.ENDC}")
                self.ct = {"s1": 200, "s2": 200, "s3": 200, "s4": 200, "s5": 200}

    def receiver_arduino(self):
        sleep(2)
        while True:
            sleep(0.4)
            cnt_index = ["s1", "s2", "s3", "s4", "s5"]  # The indices of your data in the received JSON file
            for index in cnt_index:
                if int(self.ct[index]) < 10:  # If the number is lower than 10
                    self.ct[index] = f"00{self.ct[index]}"  # We add two zeros to the data

                elif int(self.ct[index]) < 100:  # If the number is lower than 100
                    self.ct[index] = f"0{self.ct[index]}"  # We add one zero to the data
            num = str(f'{self.ct["s1"]}{self.ct["s2"]}{self.ct["s3"]}{self.ct["s4"]}{self.ct["s5"]}')  # The String That will be sent to the arduino with the information

            try:
                value = self.write_read(num)
                print(f"[DATA] Data received Back was: {value}")
            except Exception:
                try:
                    print(f"{bcolors.WARNING}[ERROR] Error while sending data to arduino in port {SERIAL_PORTS[int(self.selection)]}{bcolors.ENDC}")
                except:
                    pass
                try:
                    self.ard = arduino_connect(int(self.selection), BAUDRATE)
                except Exception:
                    self.i += 1
                    if self.i > 10:
                        print('\n\n')
                        self.ser = False
                        sleep(0.6)
                        self.selection = ask_user_port()
                        try:
                            self.ard = arduino_connect(int(self.selection), BAUDRATE)
                            self.ser = True
                        except Exception:
                            pass
