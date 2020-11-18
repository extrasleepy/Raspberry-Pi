import time
import requests
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
#define the pin that goes to the circuit
pin_to_circuit = 16
 
TOKEN = "YOUR TOKEN"  # Put your TOKEN here
DEVICE_LABEL = "pi"  # Put your device label here
VARIABLE_LABEL_1 = "light"  # Put your first variable label here
VARIABLE_LABEL_2 = "temperature"  # Put your second variable label here
light=0
temperature=0
 
def build_payload(variable_1, variable_2):
   value_1=rc_time(pin_to_circuit) #read the sensor
   value_2=temperature
  
   payload = {variable_1: value_1,
              variable_2: value_2}
   print("light="+ str(value_1) + " temperature=" + str(value_2))
   return payload
 
def post_request(payload):
   # Creates the headers for the HTTP requests
   url = "http://industrial.api.ubidots.com"
   url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
   headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
 
   # Makes the HTTP requests
   status = 400
   attempts = 0
   while status >= 400 and attempts <= 5:
       req = requests.post(url=url, headers=headers, json=payload)
       status = req.status_code
       attempts += 1
       time.sleep(1)
 
   # Processes results
   print(req.status_code, req.json())
   if status >= 400:
       print("[ERROR] Could not send data after 5 attempts, please check \
           your token credentials and internet connection")
       return False
 
   print("[INFO] request made properly, your device is updated")
   return True
 
def rc_time (pin_to_circuit):
   count = 0
    #Output on the pin for
   GPIO.setup(pin_to_circuit, GPIO.OUT)
   GPIO.output(pin_to_circuit, GPIO.LOW)
   time.sleep(0.1)
 
   #Change the pin back to input
   GPIO.setup(pin_to_circuit, GPIO.IN)
    #Count until the pin goes high
   while (GPIO.input(pin_to_circuit) == GPIO.LOW):
       count += 1
 
   return count
  
def main():
   payload = build_payload(
       VARIABLE_LABEL_1, VARIABLE_LABEL_2)
 
   print("[INFO] Attemping to send data")
   post_request(payload)
   print("[INFO] finished")
 
if __name__ == '__main__':
   while (True):
       main()
       time.sleep(30) #repeat every 30 seconds
