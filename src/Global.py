"""
Functions which are used both in Sender and Receiver
"""
from requests import get, post
from serial import Serial
from time import sleep
import threading
import json 

SERIAL_PORTS = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', '/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2']
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def config_setup():
    question = input("Do you want to import your last settings?[y/n]")
    try:
        with open('sho_config.json', 'r') as f:
            read = f.readlines()
            if read == "":
                print("Config File Empty")
                raise Exception("File Empty")
    except:
        with open('sho_config.json', 'w') as f:
            f.write('{    \n"serial_port": "",    \n"Mode": "",    \n"BAUDRATE": 9600,    \n"Networking": {        \n"API_URL": "https://development-sho.herokuapp.com/1",        \n"URL_R": "/receiver",        \n"URL_S": "/servo",        \n"URL_C": "/custom",        \n"DATA_TEMPLATE": {            \n"s1": 200,            \n"s2": 200,            \n"s3": 200,            \n"s4": 200,            \n"s5": 200        \n},        \n"PREFERED_ORDER": {            \n"F1": "s1",            \n"F2": "s2",            \n"F3": "s3",            \n"F4": "s4",            \n"F5": "s5"        \n}    \n}\n}')
    with open('sho_config.json', 'r') as f:
        return json.load(f), not (question == "y" or question == "Y")

def config_write(config):
    with open('sho_config.json', 'r+') as f:
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(config, f, indent=4)
        f.truncate()     # remove remaining part
        

def arduino_connect(selection, baudrate):
    print(f'{bcolors.OKCYAN}[INFO] Connecting to Serial Port {SERIAL_PORTS[int(selection)]} with {baudrate} Baudrate{bcolors.ENDC}')
    try:
        ard = Serial(port=SERIAL_PORTS[int(selection)], baudrate=baudrate, timeout=.1)
        print(f"{bcolors.OKGREEN}[INFO] Connected with Arduino in serial port: {SERIAL_PORTS[int(selection)]}{bcolors.ENDC}")
        return ard
    except Exception:
        print(f"{bcolors.WARNING}[ERROR] Arduino not connected to serial port {SERIAL_PORTS[int(selection)]}{bcolors.ENDC}")
        raise Exception(f"{bcolors.WARNING}[ERROR] Arduino not connected to serial port {SERIAL_PORTS[int(selection)]}{bcolors.ENDC}")


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
