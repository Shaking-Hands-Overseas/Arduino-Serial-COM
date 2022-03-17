# -*- coding: UTF-8 -*-
###                                         SHAKING HANDS OVERSEAS DRIVER 
###
### Function: Allows you to send data from an arduino to an API.
###
### Purpose:  This code was created for the Project Shaking Hands Overseas 
###           with the purpose of moving a hand from the other side of the ocean using a sensor glove.
###           
###
### NOTES:    1. Instructions of usage are explained in the README file. Check before usage
###
###           2. This code might contain issues. Please report if you found any, i will help you as soon as possible
###
### Author:   Joel Garcia (@Newtoniano20 / Newtoniano#1173 on discord)
###           Webpage: https://newtoniano20.github.io/
###
### GitHub:   https://github.com/Shaking-Hands-Overseas/SHA-Driver
###
### License:  MIT

version= "1.2"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Imports main code library
from src import *



print(f'{bcolors.HEADER}SHAKING HANDS OVERSEAS DRIVER{bcolors.ENDC} \n{bcolors.OKGREEN}Version {version} {bcolors.ENDC}\n{bcolors.OKCYAN}Author: @Newtoniano20 (Joel Garcia) {bcolors.ENDC}\n{bcolors.OKGREEN}Github:https://github.com/Shaking-Hands-Overseas/SHA-Driver {bcolors.ENDC}\n')


def main():
    choice = ask_user()
    if choice == 0:
        print(f"{bcolors.OKCYAN}[INFO] You have chosen Sender{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKCYAN}[INFO] You have chosen Receiver{bcolors.ENDC}")
    selection = ask_user_port()
    i = True
    while i:
        try:
            ard = arduino_connect(int(selection), BAUDRATE)
            i = False
        except Exception:
            selection = ask_user_port()

    if choice == 0:
        sender_launcher(selection, ard)

    elif choice == 1:
        receiver_launcher(selection, ard)


if __name__ == '__main__':
    main()
