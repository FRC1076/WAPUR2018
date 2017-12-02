from pyfrc.physics import drivetrains

class PhysicsEngine:

    def __init__(self, physics_controller):
        self.physics_controller = physics_controller

    def update_sim(self, hal_data, now, dt):
        l_motor = -hal_data['CAN'][3]['value'] / 1024
        r_motor = -hal_data['CAN'][1]['value'] / 1024
        
        speed, rotation = drivetrains.two_motor_drivetrain(l_motor, r_motor)
        self.physics_controller.drive(speed, rotation, dt)