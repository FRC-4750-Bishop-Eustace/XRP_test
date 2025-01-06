# Import necessary modules
from machine import Pin 
import bluetooth
import time
import math

from XRPLib.defaults import *
from pestolink import PestoLinkAgent

#Choose the name your robot shows up as in the Bluetooth paring menu
#Name should be 8 characters max!
robot_name = "XRProbot"

# Create an instance of the PestoLinkAgent class
pestolink = PestoLinkAgent(robot_name)

# Start an infinite loop
while True:
    if pestolink.is_connected():  # Check if a BLE connection is established
        rotation = -1 * pestolink.get_axis(0)
        throttle = -1 * pestolink.get_axis(1)
        #strafe = 0
        
        if(pestolink.get_button(2)):
            drivetrain.set_effort(1, -1, -1, 1)
        
        if(pestolink.get_button(1)):
            drivetrain.set_effort(-1, 1, 1, -1)
            
        drivetrain.arcade(throttle, rotation)
        
        if(pestolink.get_button(0)):
            servo_one.set_angle(110)
        else:
            servo_one.set_angle(90)
        
        #if(pestoline.get_button)
        
        


    else: #default behavior when no BLE connection is open
        drivetrain.arcade(0, 0)
        servo_one.set_angle(70)
