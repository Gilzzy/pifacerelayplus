from time import sleep
import pifacerelayplus


DELAY = 1.0  # seconds


if __name__ == "__main__":
	pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.MOTOR_DC)
	while True:
		pfr.motors[0].forward()		
		sleep(2.0)
		pfr.motors[0].brake()
		sleep(DELAY)
		pfr.motors[0].reverse()
		sleep(2.0)
		pfr.motors[0].brake()
		sleep(DELAY)
#		pfr.motors[0].reverse()
#		sleep(DELAY)
#		pfr.motors[1].forward()
#		sleep(DELAY)
#		pfr.motors[0].reverse()
#		sleep(DELAY)
#		pfr.motors[1].reverse()
#		sleep(DELAY)

#		pfr.relays[0].toggle()
#		sleep(DELAY)
#		pfr.relays[1].toggle()
#		sleep(DELAY)
#		pfr.relays[2].toggle()
#		sleep(DELAY)
#		pfr.relays[3].toggle()
#		sleep(DELAY)

