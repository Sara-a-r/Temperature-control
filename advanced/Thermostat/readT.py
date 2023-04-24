import serial
import time
import numpy as np

# declare variables to be used
n_data = 300  # number of data to get from Arduino
single_read = []   # values of heater's state and Troom at each reading
list_data = []     # list of all data (state, T)


# ----------------Read data from Arduino---------------- #

# establish serial connection to Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
print('Start acquisition...')

for i in range(0, n_data):
    # read all data until EOL ('\n')
    arduino_data = arduino.readline()
    # convert data (bytes) in str
    decoded_values = str(arduino_data[0:len(arduino_data)].decode())
    # split values (heater's state x Troom)
    single_read = decoded_values.split('x')
    # extract values
    for data in single_read:
        list_data.append(float(data))

arduino.close()

# reshape list of data in a matrix (n_data, 2)
matrix_data = (np.array(list_data)).reshape(-1, 2)

# save arduino data in a file txt
np.savetxt('3 watt ca/data_5V_25.txt', matrix_data, fmt='%.2f')