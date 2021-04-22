#hookup here: https://docs.google.com/document/d/1r1m1IiLGHN1uiaMqXO9lcdAVmkkgwkZvlqTsTdm4cmI/edit
import glob
import time
import blynklib
from gpiozero import DistanceSensor

BLYNK_AUTH = 'Your_Auth_Token'


base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

sensor = DistanceSensor(echo=17, trigger=5)

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"

@blynk.handle_event('read V11')
def read_virtual_pin_handler(pin):
    print(READ_PRINT_MSG.format(pin))
    print(read_temp())
    blynk.virtual_write(pin, read_temp())
    
@blynk.handle_event('read V12')
def read_virtual_pin_handler(pin):
    print(READ_PRINT_MSG.format(pin))
    rounded=round(sensor.distance,2)
    print("distance " + str(rounded))
    blynk.virtual_write(pin,rounded)
    
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return round(temp_f,2)
    
while True:
    blynk.run()