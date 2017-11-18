from robotpy_ext.autonomous import StatefulAutonomous, timed_state

from wpilib import RobotDrive

class DrivetrainCommand(StatefulAutonomous):
    MODE_NAME = 'Autonomous 1'
    DEFAULT = True

    # Set by self.components in robot.py
    drivetrain = RobotDrive

    # This function is executed during autonomous_perodic() first, for 1 second
    # and then switches over to rotate()
    # If we wanted, we could also manually set the next state using self.next_state()
    @timed_state(duration=1, first=True, next_state="rotate")
    def drive_forward(self):
        self.drivetrain.arcadeDrive(moveValue=-0.5, rotateValue=0)

    @timed_state(duration=1)
    def rotate(self):
        self.drivetrain.arcadeDrive(moveValue=0, rotateValue=0.5)