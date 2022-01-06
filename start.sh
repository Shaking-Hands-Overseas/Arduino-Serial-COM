echo "Cheking For updates..."
python3 -m pip install --upgrade pip -q
pip install requests -q
pip install pyserial -q
echo "Starting Arduino Serial COM...\n"
python3 main.py
