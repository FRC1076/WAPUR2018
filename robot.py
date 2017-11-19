import wpilib
import ctre

from wpilib.interfaces import GenericHID

LEFT = GenericHID.kLeft
RIGHT = GenericHID.kRight

class WAPURBot(wpilib.IterativeRobot):
    def robotInit(self):
        self.l_motor = ctre.CANTalon(3)
        self.l_motor2 = ctre.CANTalon(4)
        self.r_motor = ctre.CANTalon(1)
        self.r_motor2 = ctre.CANTalon(2)
        self.robot_drive = wpilib.RobotDrive(self.l_motor, self.l_motor2, self.r_motor, self.r_motor2)
        self.controller = wpilib.XboxController(0)

    def teleopPeriodic(self):
        right_y = self.controller.getY(wpilib.RIGHT)
        left_x = self.controller.getX(wpilib.LEFT)
        self.robot_drive.arcadeDrive(moveValue=right_y, rotateValue=left_x)

    def autonomousInit(self):
        print("Auto Init")

    def autonomousPeriodic(self):
        self.l_motor.set(1)
        self.r_motor.set(-1)

if __name__ == '__main__':
    wpilib.run(WAPURBot)
