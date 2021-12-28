# Arduino-Serial-COM
This is the improved version of the Serial Receiver and Serial Sender, merging them together into a singe project.

## Overview:
This code allows the user to send data to an API using an Arduino and a computer as an intermediary.
You can choose from two options:

- Sender : To send data from an arduino to an API
- Receiver: To receive data from an API and send it to an arduino
## Important Information:
I recommend using my arduino Firmware, but feel free to use whatever you prefer. But in the case of creating your own firmware, it's key to understand that the data will only be sent (This applies to the sender Only) if the computer sends the letter "A" and then will respond the Arduino. So then have in mind dealing with this

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
3. Open the file "src\Var.py" via your text editor and specify on the URL_R & URL_S Variables your API URLS.

4. Change the post request according to your data, so increasing or reducing the ammount of variables "data\[n]"

With the above should work just fine.

## Todo List for next Versions:
- Creating a GUI
