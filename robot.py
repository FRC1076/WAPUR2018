import wpilib
import ctre
import magicbot

from robotpy_ext.autonomous import AutonomousModeSelector

class WAPURBot(wpilib.IterativeRobot):
    def robotInit(self):
        self.l_motor = ctre.CANTalon(3)
        self.l_motor2 = ctre.CANTalon(4)
        self.r_motor = ctre.CANTalon(1)
        self.r_motor2 = ctre.CANTalon(2)
        self.robot_drive = wpilib.RobotDrive(self.l_motor, self.l_motor2, self.r_motor, self.r_motor2)
        self.stick = wpilib.Joystick(0)

        # These are the components of the robot.
        self.components = {
            # sets self.drivetrain to self.robot_drive
            'drivetrain': self.robot_drive
        }
        
        self.automodes = AutonomousModeSelector('autonomous',
                                                self.components)

    def teleopPeriodic(self):
        self.robot_drive.arcadeDrive(self.stick)

    def autonomousInit(self):
        print("Auto Init")

    def autonomousPeriodic(self):
        self.automodes.run()


if __name__ == '__main__':
    wpilib.run(WAPURBot)