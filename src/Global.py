"""
Functions which are used both in Sender and Receiver
"""

from serial import Serial
from .Var import *


def arduino_connect(selection: int, baudrate: int):
    print(f'{bcolors.OKCYAN}[INFO] Connecting to Serial Port {SERIAL_PORTS[int(selection)]} with {BAUDRATE} Baudrate{bcolors.ENDC}')
    try:
        ard = Serial(port=SERIAL_PORTS[int(selection)], baudrate=baudrate, timeout=.1)
        print(f"{bcolors.OKGREEN}[INFO] Connected with Arduino in serial port: {SERIAL_PORTS[int(selection)]}{bcolors.ENDC}")
        return ard
    except Exception:
        print(f"{bcolors.WARNING}[ERROR] Arduino not connected to serial port {SERIAL_PORTS[int(selection)]}{bcolors.ENDC}")
        raise Exception(f"{bcolors.FAIL}[ERROR] Arduino not connected to serial port {SERIAL_PORTS[int(selection)]}{bcolors.ENDC}")


def ask_user_port():
    print(f"\n[0]'COM1', [1]'COM2', [2]'COM3', [3]'COM4', [4]'COM5', [5]'COM6' \n[6]'/dev/ttyACM0', [7]'/dev/ttyACM1', [8]'/dev/ttyACM2, [9]'Other' ")
    response = input('Select a Serial Port:')
    if len(SERIAL_PORTS) >= 10:
        SERIAL_PORTS.pop()
    try:
        if int(response) == len(SERIAL_PORTS):
            serial_port = input("Enter Custom Serial Port:")
            SERIAL_PORTS.append(serial_port)
        elif int(response) > len(SERIAL_PORTS):
            print(f'{bcolors.WARNING}[ERROR] Invalid Input{bcolors.ENDC}')
            response = None
    except Exception:
        print(f'{bcolors.WARNING}[ERROR] Invalid Input{bcolors.ENDC}')
    print(SERIAL_PORTS, len(SERIAL_PORTS))
    return response


def ask_user():
    x = True
    choice = None
    while x:
        print('Specify whether you want to be a sender or a receiver.\n [0] Sender \n [1] Receiver')
        try:
            choice = int(input('\n Input:'))
        except Exception:
            pass
        if choice == 0 or choice == 1:
            break
        else:
            print(f'{bcolors.WARNING}[ERROR] Invalid Input{bcolors.ENDC}')
            pass
    return choice
