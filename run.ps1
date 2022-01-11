echo "Checking for updates..."
py -m pip install --upgrade pip -q
pip install pyserial -q
pip install requests -q
echo "Starting Arduino Serial COM..."
echo
python main.py
