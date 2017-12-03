import wpilib
import ctre
import logging

logging.basicConfig(level=logging.DEBUG)


class WAPURBot(wpilib.IterativeRobot):
    def robotInit(self):
        print("Robot Init")
        # self.l_motor = ctre.CANTalon(3)
        # self.l_motor2 = ctre.CANTalon(4)
        # self.r_motor = ctre.CANTalon(1)
        # self.r_motor2 = ctre.CANTalon(2)
        # self.robot_drive = wpilib.RobotDrive(self.l_motor, self.l_motor2, self.r_motor, self.r_motor2)
        # self.stick = wpilib.Joystick(0)
        print("Robot Init Done!")

    def robotPeriodic(self):
        print("Robot Periodic!")

    def teleopInit(self):
        print("Teleop Init")

    def teleopPeriodic(self):
        # self.robot_drive.arcadeDrive(self.stick)
        # print(self.l_motor.get())
        print("Teleop Periodic")

    def autonomousInit(self):
        print("Auto Init")

    def autonomousPeriodic(self):
        # self.l_motor.set(1)
        # self.r_motor.set(-1)
        print("Auto Periodic")

    def disabledInit(self):
        print("Disabled Init")

    def disabledPerodic(self):
        print("Disabled Perodic")

    def testInit(self):
        print("Test Init")

    def testPeriodic(self):
        print("Test Perodic")

print("A")
if __name__ == '__main__':
    wpilib.run(WAPURBot)
    print("shouldn't get here???")