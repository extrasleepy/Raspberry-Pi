# provides arrival time in minutes at stop 13548 which is a 1 California route stop at 32nd and Clement St.

import time
from requests import get

url='https://webservices.umoiq.com/api/pub/v1/agencies/sfmta-cis/stopcodes/13548/predictions?key=0be8ebd0284ce712a63f29dcaf7798c4'

while True:
   muni_route = get(url).json()[0]['route']['title']
   muni_stop = get(url).json()[0]['stop']['name']
   muni_eta = get(url).json()[0]['values'][0]['minutes']
   #print(muni['direction']['prediction'][0]['minutes'])
   print(muni_route + " arrives in " + str(muni_eta) + " minutes at " + str(muni_stop) + " stop")
   time.sleep(30)
