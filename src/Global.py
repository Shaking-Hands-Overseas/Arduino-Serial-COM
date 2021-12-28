"""
Functions which are used both in Sender and Receiver
"""

from serial import Serial
from .Var import *


def arduino_connect(selection: int, baudrate: int):
    print(f'{bcolors.OKCYAN}[INFO] Connecting to Serial Port {SERIAL_PORTS[int(selection)]} with {BAUDRATE} Baudrate{bcolors.ENDC}')
    try:
        ard = Serial(port=SERIAL_PORTS[int(selection)], baudrate=baudrate, timeout=.1)
        print(f"{bcolors.OKGREEN}Connected with Arduino in serial port: {SERIAL_PORTS[int(selection)]}{bcolors.ENDC}")
        return ard
    except Exception:
        raise Exception(f"{bcolors.FAIL}[ERROR] Arduino not connected to serial port {SERIAL_PORTS[int(selection)]}{bcolors.ENDC}")


def ask_user_port():
    print(f"\n[0]'COM1', [1]'COM2', [2]'COM3', \n[3]'/dev/ttyACM0', [4]'/dev/ttyACM1', [5]'/dev/ttyACM2' ")
    response = input('Select a Serial Port:')
    try:
        int(response)
    except Exception:
        print(f'{bcolors.WARNING}[ERROR] Invalid Input{bcolors.ENDC}')
    if int(response) > 6:
        print(f'{bcolors.WARNING}[ERROR] Invalid Input{bcolors.ENDC}')
        response = None
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
