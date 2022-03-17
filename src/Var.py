"""
Global Variables which are used throughout the project
"""

# SERIAL PORTS: Windows = COM1, COM2, ... / Linux = /dev/ttyACM0, /dev/ttyACM1,...
SERIAL_PORTS = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', '/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2']

# MAIN SERVER URL: 
API = 'https://xlbi6e.deta.dev'
# API ROUTE FOR RECEIVING DATA
URL_R = '/reciever'
# API ROUTE FOR SENDING DATA
URL_S = '/servo'
# API ROUTE FOR DATA ORDER
URL_C = '/custom'

# Data template used when sending data
DATA_TEMPLATE = {
    "s1":200,
    "s2":200,
    "s3":200,
    "s4":200,
    "s5":200
}

# Prefered Sensor Order (Input vs Output order)
PREFERED_ORDER = {
    "F1": "s2",
    "F2": "s1",
    "F3": "s3",
    "F4": "s4",
    "F5": "s5"
}

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
