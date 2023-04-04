from machine import I2C, Pin
from time import sleep
from APDS9960LITE import APDS9960LITE
from ultrasonic import sonic

# Initialise I2C bus
i2c = I2C(0, scl=Pin(21), sda=Pin(20))
# Initialise APDS9660
apds9960=APDS9960LITE(i2c) # Create APDS9660 sensor object
apds9960.prox.enableSensor() # Send I2C command to enable sensor
sleep(0.1) # Let sensor measurement stabilise before starting loop


ultrasonic = sonic(17, 18)

for i in range(100):
 proximity_measurement = apds9960.prox.proximityLevel # Read the proximity
 #...value
 ultrasonic_measurement_mm = ultrasonic.distance_mm()
 print("{:3d}, {:4.2f}".format(proximity_measurement,ultrasonic_measurement_mm))
 #...))
 sleep(0.2) # Wait for measurement to be ready

print("Experiment finished! Please restart processor to repeat.")
