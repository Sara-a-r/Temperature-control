import serial
import numpy as np

# declare variables to be used

n_data = 100        # number of data to get from Arduino

singleT_read = []   # values of the 3 T at each reading
list_T = []         # list of all T 

#--------------Read data from Arduino------------------#
# establish serial cocnnection to Arduino
arduino = serial.Serial('/dev/ttyACM1', 9600)
    
for i in range(0,n_data):
    # read all data until EOL ('\n')
    arduino_data = arduino.readline()
    # convert data (bytes) in str
    decoded_values = str(arduino_data[0:len(arduino_data)].decode())
    # split values (Tcontrol x Tref x Troom)
    singleT_read = decoded_values.split('x')
    # extract T values
    for T in singleT_read:
        list_T.append(float(T))

arduino.close()

# reshape list of T in a matrix (n_data, 3)
matrix_T = (np.array(list_T)).reshape(-1,3)

#save data in a file txt
np.savetxt('data_T.txt', matrix_T, fmt = '%.2f')