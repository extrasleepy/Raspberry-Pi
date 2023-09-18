import time

# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# holds the count for the feed
run_count = 0

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'YOUR_KEY_HERE'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'YOUR_USERNAME_HERE'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# feed name goes here
feed = Feed(name="test")

while True:
    print('sending count: ', run_count)
    run_count += 1
    aio.send_data('test', run_count)  #feed name and data to send
    time.sleep(5)
