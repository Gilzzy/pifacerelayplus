
import pifacerelayplus

pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

pfr.motors[0].forward()
pfr.motors[1].forward()
pfr.motors[2].forward()
pfr.motors[3].forward()



#CONTROLLING A STEPPER MOTOR
#Author: Robert Caldwell
#Date: 14 August 2013

#from time import sleep
#import piface.pfio as pfio
#pfio.init()

#def anticlockwise(rotations, speed):
#	sleep_time = 0.1 / float(speed)
#	for loop in range(1,int(512*float(rotations))):
#		pfio.digital_write(4,1)
#		sleep(sleep_time)
#		pfio.digital_write(7,0)
#		sleep(sleep_time)
#		pfio.digital_write(5,1)
#		sleep(sleep_time)
#		pfio.digital_write(4,0)
#		sleep(sleep_time)
#		pfio.digital_write(6,1)
#		sleep(sleep_time)
#		pfio.digital_write(5,0)
#		sleep(sleep_time)
#		pfio.digital_write(7,1)
#		sleep(sleep_time)
#		pfio.digital_write(6,0)
#		sleep(sleep_time)
#		pfio.digital_write(7,0)
#  
#def clockwise(rotations, speed):
#	sleep_time=0.1 / float(speed)
#	for loop in range(1,int(512*float(rotations))):
#		pfio.digital_write(7,1)
#		sleep(sleep_time)
#		pfio.digital_write(4,0)
#		sleep(sleep_time)
#		pfio.digital_write(6,1)
#		sleep(sleep_time)
#		pfio.digital_write(7,0)
#		sleep(sleep_time)
#		pfio.digital_write(5,1)
#		sleep(sleep_time)
#		pfio.digital_write(6,0)
#		sleep(sleep_time)
#		pfio.digital_write(4,1)
#		sleep(sleep_time)
#		pfio.digital_write(5,0)
#		sleep(sleep_time)
#		pfio.digital_write(4,0)

