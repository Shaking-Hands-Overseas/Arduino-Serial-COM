from requests import post
from .Global import *
from time import sleep
import threading


def sender_launcher(selection, ard):
    print(f"{bcolors.HEADER}[INFO] Starting Sender{bcolors.ENDC}")
    sender = Sender(selection, ard)
    print(f"{bcolors.OKGREEN}[INFO] Class Sender Has been created{bcolors.ENDC}")
    print("[INFO] Creating Sender Server Thread")
    sender_server_thread = threading.Thread(target=sender.sender_server, args=())
    print("[INFO] Starting Sender Server Thread")
    sender_server_thread.start()
    print(f"{bcolors.OKGREEN}[INFO] Sender Server Thread Created and Initialized{bcolors.ENDC}")
    print("[INFO] Creating Sender Arduino Thread")
    sender_arduino_thread = threading.Thread(target=sender.sender_arduino, args=())
    print("[INFO] Starting Sender Arduino Thread")
    sender_arduino_thread.start()
    print(f"{bcolors.OKGREEN}[INFO] Sender Arduino Thread Created and Initialized{bcolors.ENDC}")
    print(f"{bcolors.HEADER}[INFO] Initialization Finalized Successfully{bcolors.ENDC}")
    print("---------- LOG DATA ----------")


class Sender:
    def __init__(self, selection, ard):
        self.Sender_data = {}
        self.selection = selection
        self.ard = ard
        self.i = 0
        self.ser = True

    def arduino_read(self):
        """
        Reads data from arduino
        :return: String
        """
        self.ard.write(bytes("A", 'utf-8'))
        return self.ard.readline().decode('utf-8')

    def sender_server(self):
        while True:
            if self.ser:
                try:
                    req_response = post(url=URL_S, json=self.Sender_data)
                    sleep(0.1)
                    print(f"[INFO] Server Response: {req_response.status_code}")
                except Exception:
                    print(f"{bcolors.WARNING}[ERROR] Server {URL_R} not responding to request{bcolors.ENDC}")
            else:
                sleep(1)

    def sender_arduino(self):
        while True:
            try:
                data = self.arduino_read()
            except Exception:
                print(f"{bcolors.WARNING}[ERROR] Error while sending data to arduino in port {SERIAL_PORTS[int(self.selection)]}{bcolors.ENDC}")
                try:
                    self.ard = arduino_connect(int(self.selection), BAUDRATE)
                    self.ser = True
                except Exception:
                    self.i += 1
                    if self.i > 10:
                        print('\n\n')
                        self.ser = False
                        sleep(0.7)
                        self.selection = ask_user_port()
                        try:
                            self.ard = arduino_connect(int(self.selection), BAUDRATE)
                            self.ser = True
                        except Exception:
                            pass
            try:
                data2 = data.split()
                self.Sender_data = {"s1": int(data2[0]), "s2": int(data2[1]), "s3": int(data2[2]), "s4": int(data2[3]), "s5": int(data2[4])}
                print(self.Sender_data)
            except Exception:
                pass
            sleep(0.1)
