# CODE IS CURRENTLY INCOMPLETE, WILL RETURN TO FINISH. ANY HELPFUL INPUT IS VERY MUCH APPRECIATED

# import DistanceSensor, sleep, LED, Button
from gpiozero import DistanceSensor
from time import sleep
from gpiozero import LED 
from gpiozero import Button

# for DistanceSensor using HC-SR04, echo uses GPIO 23, and trigger uses GPIO 24 
sensor = DistanceSensor(echo=23, trigger=24, max_distance=2.0)

# led veriable for LED output using GPIO 12
led = LED(12)
# button variable for Button using GPIO 16
button = Button(16)

# While loop, to do everything
while True:
        # press the button to begin sequence
        button.wait_for_press()
        # use sensor for distance reading
        distance = sensor.distance * 100
        print("Distance: %.2f", % distance)
        sleep(0.5)
        # set distance to light up LED when a certain distance is reached

        # turn on LED when distance is reached
        led.on()
        # turn LED off when distance is less than the set distance
        led.off()
        # end entire sequence when button is relseased
        button.wait_for_release()
