from .Global import *


def sender_launcher(config, ard):
    print(f"{bcolors.HEADER}[INFO] Starting Sender{bcolors.ENDC}")
    sender = Sender(config, ard)
    print("[INFO] Starting Sender Server Thread")
    threading.Thread(target=sender.sender_server, args=()).start()
    print("[INFO] Starting Sender Arduino Thread")
    threading.Thread(target=sender.sender_arduino, args=()).start()
    print(f"{bcolors.HEADER}[INFO] Initialization Finalized Successfully{bcolors.ENDC}")
    print("---------- LOG DATA ----------")


class Sender:
    def __init__(self, config, ard):
        Networking = config["Networking"]
        self.URL_Sender = Networking["API_URL"] + Networking["URL_S"]
        self.URL_Custom = Networking["API_URL"] + Networking["URL_C"]
        self.Sender_data = Networking["DATA_TEMPLATE"]
        self.PREFERED_ORDER = Networking["PREFERED_ORDER"]
        self.selection = config["Mode"]
        self.BAUDRATE = config["BAUDRATE"]
        self.ard = ard
        self.i = 0
        self.ser = True

    def arduino_read(self):
        """
        Reads data from arduino
        :return: String
        """
        self.ard.write(bytes("A", 'utf-8'))
        #sleep(0.7)
        return self.ard.readline().decode('utf-8')

    def sender_server(self):
        while True:
            if self.ser:
                try:
                    req_response_s = post(url=self.URL_Sender, json=self.Sender_data)
                except Exception:
                    print(f"{bcolors.WARNING}[ERROR] Server {self.URL_Sender} not responding /servo to request{bcolors.ENDC}")
                try:
                    req_response_c = post(url=self.URL_Custom, json=self.PREFERED_ORDER)
                except Exception:
                    print(f"{bcolors.WARNING}[ERROR] Server {self.URL_Sender} not responding to /custom request{bcolors.ENDC}")
                try:
                    print(f"{bcolors.OKCYAN}[SERVER]{bcolors.ENDC} Server Response: /servo : {req_response_s} ; /custom {req_response_c}")
                except:
                    pass
            else:
                sleep(1)

    def sender_arduino(self):
        while True:
            try:
                data = self.arduino_read()
            except Exception:
                print(f"{bcolors.WARNING}[ERROR] Error while sending data to arduino in port {SERIAL_PORTS[int(self.selection)]}{bcolors.ENDC}")
                try:
                    self.ard = arduino_connect(int(self.selection), self.BAUDRATE)
                    self.ser = True
                except Exception:
                    self.i += 1
                    if self.i > 10:
                        print('\n\n')
                        self.ser = False
                        sleep(1)
                        self.selection = ask_user_port()
                        try:
                            self.ard = arduino_connect(int(self.selection), self.BAUDRATE)
                            self.ser = True
                        except Exception:
                            pass
            data2 = data.split()
            for value_index in range(len(data2)):
                self.Sender_data[f"s{value_index + 1}"] = int(data2[value_index])
            print(f"{bcolors.OKGREEN}[ARDUINO]{bcolors.ENDC}{data}")
            sleep(0.1)
