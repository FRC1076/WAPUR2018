import wpilib
import ctre
import magicbot
import robotpy_ext

from robotpy_ext.autonomous import AutonomousModeSelector
from magicbot import StateMachine, state, timed_state
from wpilib.interfaces import GenericHID

LEFT = GenericHID.Hand.kLeft
RIGHT = GenericHID.Hand.kRight

class DriveControl(StateMachine):
    motor = ctre.CANTalon

    def forward(self):
        self.engage()

    @state(first=True)
    def prepare_to_forward(self):
        self.motor.enable()

        if self.motor.is_ready():
            self.next_state_now('moving')

    @timed_state(duration=1, must_finish=True)
    def moving(self):
        self.motor.enable()
        self.motor()

class DriveTrain:
    drive_motor = wpilib.RobotDrive

    def __init__(self):
        self.enabled = False

    def __enable__(self):
        self.enabled = True

    def forward(self, speed, time):
        pass


class WAPURBot(wpilib.IterativeRobot):
    def robotInit(self):
        self.r_motor = ctre.CANTalon(1)
        self.r_motor2 = ctre.CANTalon(2)
        self.l_motor = ctre.CANTalon(3)
        self.l_motor2 = ctre.CANTalon(4)
        self.robot_drive = wpilib.RobotDrive(self.l_motor, self.l_motor2, self.r_motor, self.r_motor2)
        self.catapult_motor = ctre.CANTalon(5)

        self.driver = wpilib.XboxController(0)
        self.operator = wpilib.XboxController(1)

        self.automodes = AutonomousModeSelector('autonomous')

    def teleopPeriodic(self):
        driver_right_y = self.driver.getY(RIGHT)
        driver_left_x = self.driver.getX(LEFT)
        self.robot_drive.arcadeDrive(moveValue=driver_right_y, rotateValue=driver_left_x)
        operator_left_y = self.operator.getY(LEFT)
        self.catapult_motor.set(operator_left_y)

    def autonomousInit(self):
        print("Auto Init")

    def autonomousPeriodic(self):
        self.automodes.run()

    def forwardCommand(speed, time):
        speed = self.wheel(1)

if __name__ == '__main__':
    wpilib.run(WAPURBot, physics_enabled=True)
