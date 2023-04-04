from machine import I2C, Pin
from time import sleep
from APDS9960LITE import APDS9960LITE

# Initialise I2C bus
i2c = I2C(0, scl=Pin(17), sda=Pin(16))
# Initialise APDS9960
apds9960=APDS9960LITE(i2c) # Create APDS9960 sensor object
apds9960.prox.enableSensor() # Send I2C command to enable sensor
sleep(0.1) # Let sensor measurment stabilise before starting loop

while True:
 proximity_measurement = apds9960.prox.proximityLevel # Read the proximity
#...value
 print(proximity_measurement) # Print proximity value
 sleep(0.2) # Wait for measurement to be ready

