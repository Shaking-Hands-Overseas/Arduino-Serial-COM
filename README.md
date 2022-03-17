# SHAKING HANDS OVERSEAS DRIVER
This is the improved version of the Serial Receiver and Serial Sender, merging them together into a singe project.

## Overview:
This code allows the user to send data to an API using an Arduino and a computer as an intermediary.
You can choose from two options:

- Sender : To send data from an arduino to an API
- Receiver: To receive data from an API and send it to an arduino
## Important Information:
I recommend using my arduino Firmware, but feel free to use whatever you prefer. But in the case of creating your own firmware, it's key to understand that the data will only be sent (This applies to the sender Only) if the computer sends the letter "A" and then will respond the Arduino. So then have in mind dealing with this

[Sender Firmware](https://github.com/Shaking-Hands-Overseas/Arduino-Glove-Firmware) <p></p>
[Receiver Firmware](https://github.com/Shaking-Hands-Overseas/Arduino-Hand-Firmware)

## Installation Guide:
1. Download the lastest version from releases in this repository or clone the repository using the following command:
```
git clone https://github.com/Shaking-Hands-Overseas/Serial-Sender-Receiver
```
2. 
Execute the Powershell file. This will automatically install all dependencies and start the program:
```
.\run.ps1
```
Or Install Necessary Dependencies using pip:
```
pip install pyserial
```
and:
```
pip install requests
```
3. Open the file "src\Var.py" via your text editor and specify your API URL and routes for sending and receiving data. It should be noticed that data will be sent to you server as follows:
```
POST_REQUEST = {
"s1":0,
"s2":1,
"s3":2,
"s4":3,
"s5":100
}
```
And it is expected to get the information in the same way when using GET with your API.
4. Change the prefered order and template according to your data

With the above should work just fine.

## Todo List for next Versions:
- Creating a GUI
- Allow more than 5 data values at the same time
