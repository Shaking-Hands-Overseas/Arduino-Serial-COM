# Arduino-Serial-Glove
This code is what allows the connection between the Arduino and Computer. This code sends the information recieved from an Arduino to a Server.

## Important Information:
I recommend using my arduino Firmware, but feel free to use whatever you prefer. But in the case of creating your own firmware, it's key to understand that the data will only be sent if the computer sends the letter "A" and then will respond the Arduino. So then have in mind dealing with this

## Installation Guide:
1. Download the lastest version from releases in this repository or clone the repository using the following command:
```
git clone https://github.com/Shaking-Hands-Overseas/Arduino-Serial-Glove
```
2. Install Necessary Dependencies using pip:
```
pip install pyserial
```
3. Open the file "main.py" via your text editor and specify on the URL Variable your API URL and the Serial Port on the SERIAL_PORT variable

4. Change the post request according to your data, so increasing or reducing the ammount of variables "data\[n]"

With the above should work just fine.

## Todo List for next Versions:
- Creating a Serial Port Selector
- Simplify the way in which the API settings are used into a single JSON File
