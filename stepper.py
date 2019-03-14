from time import sleep
from triangula.input import SixAxis, SixAxisResource
import pifacerelayplus

#def handler(button):
#	print "Button {} pressed".format(button)


DELAY = 0.001 # seconds


if __name__ == "__main__":
	pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.MOTOR_STEPPER)
	with SixAxisResource(bind_defaults=True) as joystick:
		joystick.register_button_handler(handler, SixAxis.BUTTON_SQUARE)
		while True:
			x = joystick.axes[0].corrected_value()
			y = joystick.axes[1].corrected_value()
			
			print(x,y)
			
			pfr.motors[0].coast()
#			sleep(DELAY)
			pfr.motors[1].brake()
			sleep(0.11)
#			pfr.motors[0].forward(10,DELAY)
#			sleep(DELAY)
			pfr.motors[1].forward(500,DELAY)
			sleep(0.1)
			pfr.motors[1].coast()
			sleep(0.1)
			pfr.motors[1].reverse(500,DELAY)
			sleep(0.1)
			pfr.motors[0].brake()
			sleep(0.11)
#               pfr.motors[0].forward(10,DELAY)
#               sleep(DELAY)
		pfr.motors[0].forward(500,DELAY)
		sleep(1)
		pfr.motors[0].coast()
		sleep(1)
		pfr.motors[0].reverse(500,DELAY)
		sleep(1)

