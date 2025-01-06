from XRPLib.defaults import *
from .imu import IMU
# available variables from defaults: left_motor, right_motor, drivetrain,
#      imu, rangefinder, reflectance, servo_one, board, webserver
# Write your code Here
IMU.get_default_imu()

while True:
    print("accel [x,y,z] =", IMU.get_acc_rates())
    print("gyro [x,y,x] =", IMU.get_gyro_rates())
    time.sleep(1)
