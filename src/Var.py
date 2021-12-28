"""
Global Variables which are used throughout the project
"""

# SERIAL PORTS: Windows = COM1, COM2, ... / Linux = /dev/ttyACM0, /dev/ttyACM1,...
SERIAL_PORTS = ['COM1', 'COM2', 'COM3', '/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2']

# API URL FOR RECEIVING DATA
URL_R = 'https://xlbi6e.deta.dev/reciever'
# API URL FOR SENDING DATA
URL_S = 'https://xlbi6e.deta.dev/servo'

# ARDUINO SERIAL BAUDRATE
BAUDRATE = 9600


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
