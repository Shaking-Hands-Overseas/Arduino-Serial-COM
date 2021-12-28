"""
Author : Joel Garcia (@Newtoniano20 / Newtoniano#1173 on discord)
This code was created for the Project Shaking Hands Overseas with the purpose of moving a hand from the other side
of the ocean. Any questions feel free to ask.
"""
from src import *
print('Arduino Serial Sender & Receiver \n Author: @Newtoniano20 (Joel Garcia) \n Github: https://github.com/Shaking-Hands-Overseas/Arduino-Serial-Sender \n')


def main():
    ard = None
    choice = ask_user()
    if choice == 0:
        print(f"{bcolors.OKCYAN}[INFO] You have chosen Sender{bcolors.ENDC}")
    if choice == 1:
        print(f"{bcolors.OKCYAN}[INFO] You have chosen Receiver{bcolors.ENDC}")
    selection = ask_user_port()
    i = True
    while i:
        try:
            ard = arduino_connect(int(selection), BAUDRATE)
            i = False
        except Exception:
            try:
                print(f"{bcolors.WARNING}[ERROR] Arduino not connected to Serial port {SERIAL_PORTS[int(selection)]}{bcolors.ENDC}")
            except Exception:
                pass
            selection = ask_user_port()

    if choice == 0:
        sender_launcher(selection, ard)

    elif choice == 1:
        receiver_launcher(selection, ard)


if __name__ == '__main__':
    main()
