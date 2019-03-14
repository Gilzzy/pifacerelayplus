import robot_arm
import time


if __name__ == '__main__':
    arm = robot_arm.RobotArm()
    arm.set_light(1)

    delay = 5

    while True:
        direction = 0
        arm.move_base(delay, direction)
        arm.move_shoulder(delay, direction)
        arm.move_elbow(delay, direction)
        arm.move_wrist(delay, direction)
        arm.move_grip(delay, direction)

        direction = 1
        arm.move_grip(delay, direction)
        arm.move_wrist(delay, direction)
        arm.move_elbow(delay, direction)
        arm.move_shoulder(delay, direction)
        arm.move_base(delay, direction)
