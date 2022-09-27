import rev
import wpilib
import ctre
import wpilib.interfaces


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        class Modes:
            def __init__(self):
                self.Victor = "Victor"
                self.Talon = "Talon"
                self.SparkMax = "SparkMax"

        self.modes = Modes()
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        # self.gyro = wpilib.interfaces.Gyro()
        # self.ds = wpilib.DriverStation()
        self.mode = self.modes.SparkMax
        if self.mode == self.modes.Talon:
            self.frLeft = ctre.TalonSRX(2)
            self.frRight = ctre.TalonSRX(3)
            self.reLeft = ctre.TalonSRX(1)
            self.reRight = ctre.TalonSRX(4)
            self.shooter = ctre.TalonSRX(9)
        elif self.mode == self.modes.Victor:
            self.frLeft = ctre.VictorSPX(2)
            self.frRight = ctre.VictorSPX(3)
            self.reLeft = ctre.VictorSPX(1)
            self.reRight = ctre.VictorSPX(4)
            self.shooter = ctre.VictorSPX(9)
        elif self.mode == self.modes.SparkMax:
            sparkBrushed = rev.CANSparkMaxLowLevel.MotorType(0)
            self.frLeft = rev.CANSparkMax(2, sparkBrushed)
            self.frRight = rev.CANSparkMax(3, sparkBrushed)
            self.reLeft = rev.CANSparkMax(1, sparkBrushed)
            self.reRight = rev.CANSparkMax(4, sparkBrushed)
            self.shooter = rev.CANSparkMax(9, sparkBrushed)
        else:
            self.frLeft = ctre.TalonSRX(2)
            self.frRight = ctre.TalonSRX(3)
            self.reLeft = ctre.TalonSRX(1)
            self.reRight = ctre.TalonSRX(4)
            self.shooter = ctre.TalonSRX(9)
        self.controller = wpilib.XboxController(0)
        self.timer = wpilib.Timer()
        self.stick = wpilib.XboxController(1)
        self.timer = wpilib.Timer()
        if self.mode == self.modes.SparkMax:
            self.frLeft.set(0)
            self.reLeft.set(0)
            self.frRight.set(0)
            self.reRight.set(0)
            self.shooter.set(0)
        else:
            self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.frRight.set(ctre.ControlMode.PercentOutput, 0)
            self.reRight.set(ctre.ControlMode.PercentOutput, 0)
            self.shooter.set(ctre.ControlMode.PercentOutput, 0)
        # TODO: Gyro
        # self.gyro.calibrate()
        # self.gyro.reset()
        # Set Inverted
        self.frLeft.setInverted(False)
        self.reLeft.setInverted(False)
        self.frRight.setInverted(False)
        self.reRight.setInverted(True)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        if self.mode == self.modes.SparkMax:
            self.frLeft.set(0)
            self.reLeft.set(0)
            self.frRight.set(0)
            self.reRight.set(0)
            self.shooter.set(0)
        else:
            self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.frRight.set(ctre.ControlMode.PercentOutput, 0)
            self.reRight.set(ctre.ControlMode.PercentOutput, 0)
            self.shooter.set(ctre.ControlMode.PercentOutput, 0)
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def disabledInit(self):
        self.timer.stop()
        if self.mode == self.modes.SparkMax:
            self.frLeft.set(0)
            self.reLeft.set(0)
            self.frRight.set(0)
            self.reRight.set(0)
            self.shooter.set(0)
        else:
            self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.frRight.set(ctre.ControlMode.PercentOutput, 0)
            self.reRight.set(ctre.ControlMode.PercentOutput, 0)
            self.shooter.set(ctre.ControlMode.PercentOutput, 0)

    def disabledPeriodic(self):
        if self.mode == self.modes.SparkMax:
            self.frLeft.set(0)
            self.reLeft.set(0)
            self.frRight.set(0)
            self.reRight.set(0)
            self.shooter.set(0)
        else:
            self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.frRight.set(ctre.ControlMode.PercentOutput, 0)
            self.reRight.set(ctre.ControlMode.PercentOutput, 0)
            self.shooter.set(ctre.ControlMode.PercentOutput, 0)

    def teleopInit(self):
        self.timer.reset()
        self.timer.start()
        if self.mode == self.modes.SparkMax:
            self.frLeft.set(0)
            self.reLeft.set(0)
            self.frRight.set(0)
            self.reRight.set(0)
            self.shooter.set(0)
        else:
            self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
            self.frRight.set(ctre.ControlMode.PercentOutput, 0)
            self.reRight.set(ctre.ControlMode.PercentOutput, 0)
            self.shooter.set(ctre.ControlMode.PercentOutput, 0)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        if self.mode == self.modes.SparkMax:
            self.frLeft.set(self.controller.getLeftY())
            self.reLeft.set(self.controller.getRightY())
            self.frRight.set(self.controller.getLeftY())
            self.reRight.set(self.controller.getRightY())
            self.shooter.set(self.controller.getRightTriggerAxis())
        else:
            self.frLeft.set(ctre.ControlMode.PercentOutput, -1*self.controller.getLeftY())
            self.reLeft.set(ctre.ControlMode.PercentOutput, -1*self.controller.getRightY())
            self.frRight.set(ctre.ControlMode.PercentOutput, self.controller.getLeftY())
            self.reRight.set(ctre.ControlMode.PercentOutput, self.controller.getRightY())
            self.shooter.set(ctre.ControlMode.PercentOutput, self.controller.getRightTriggerAxis())
        # turnRatio_1 = 0.25
        # turnRatio_2 = 0.75
        # xLeft = self.controller.getLeftX()
        # yLeft = self.controller.getLeftY()
        # xRight = self.controller.getRightX()
        # yRight = self.controller.getRightY()
        # # if self.ds.getBatteryVoltage() < 9:
        # #     self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
        # #     self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
        # #     self.frRight.set(ctre.ControlMode.PercentOutput, 0)
        # #     self.reRight.set(ctre.ControlMode.PercentOutput, 0)
        # if yLeft < 0 and xRight < 0:
        #     if self.mode == self.modes.SparkMax:
        #         self.frLeft.set(xRight * -1 * turnRatio_1)
        #         self.reLeft.set(xRight * -1 * turnRatio_1)
        #         self.frRight.set(yLeft * -1)
        #         self.reRight.set(yLeft * -1)
        #     else:
        #         self.frLeft.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_1)
        #         self.reLeft.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_1)
        #         self.frRight.set(ctre.ControlMode.PercentOutput, yLeft * -1)
        #         self.reRight.set(ctre.ControlMode.PercentOutput, yLeft * -1)
        # elif yLeft < 0 and xRight > 0:
        #     if self.mode == self.modes.SparkMax:
        #         self.frLeft.set(yLeft * -1)
        #         self.reLeft.set(yLeft * -1)
        #         self.frRight.set(xRight * turnRatio_1)
        #         self.reRight.set(xRight * turnRatio_1)
        #     else:
        #         self.frLeft.set(ctre.ControlMode.PercentOutput, yLeft * -1)
        #         self.reLeft.set(ctre.ControlMode.PercentOutput, yLeft * -1)
        #         self.frRight.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_1)
        #         self.reRight.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_1)
        # elif yLeft > 0 and xRight < 0:
        #     if self.mode == self.modes.SparkMax:
        #         self.frLeft.set(xRight * turnRatio_1)
        #         self.reLeft.set(xRight * turnRatio_1)
        #         self.frRight.set(yLeft * -1)
        #         self.reRight.set(yLeft * -1)
        #     else:
        #         self.frLeft.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_1)
        #         self.reLeft.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_1)
        #         self.frRight.set(ctre.ControlMode.PercentOutput, yLeft * -1)
        #         self.reRight.set(ctre.ControlMode.PercentOutput, yLeft * -1)
        # elif yLeft > 0 and xRight > 0:
        #     if self.mode == self.modes.SparkMax:
        #         self.frLeft.set(yLeft * -1)
        #         self.reLeft.set(yLeft * -1)
        #         self.frRight.set(xRight * -1 * turnRatio_1)
        #         self.reRight.set(xRight * -1 * turnRatio_1)
        #     else:
        #         self.frLeft.set(ctre.ControlMode.PercentOutput, yLeft * -1)
        #         self.reLeft.set(ctre.ControlMode.PercentOutput, yLeft * -1)
        #         self.frRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_1)
        #         self.reRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_1)
        # elif yLeft > 0 and (xRight > 0 or xRight < 0):
        #     if self.mode == self.modes.SparkMax:
        #         self.frLeft.set(-1 * yLeft)
        #         self.reLeft.set(-1 * yLeft)
        #         self.frRight.set(-1 * yLeft)
        #         self.reRight.set(-1 * yLeft)
        #     else:
        #         self.frLeft.set(ctre.ControlMode.PercentOutput, -1 * yLeft)
        #         self.reLeft.set(ctre.ControlMode.PercentOutput, -1 * yLeft)
        #         self.frRight.set(ctre.ControlMode.PercentOutput, -1 * yLeft)
        #         self.reRight.set(ctre.ControlMode.PercentOutput, -1 * yLeft)
        # elif yLeft < 0 and (xRight > 0 or xRight < 0):
        #     # TODO: Double Check Direction
        #     if self.mode == self.modes.SparkMax:
        #         self.frLeft.set(yLeft)
        #         self.reLeft.set(yLeft)
        #         self.frRight.set(yLeft)
        #         self.reRight.set(yLeft)
        #     else:
        #         self.frLeft.set(ctre.ControlMode.PercentOutput, yLeft)
        #         self.reLeft.set(ctre.ControlMode.PercentOutput, yLeft)
        #         self.frRight.set(ctre.ControlMode.PercentOutput, yLeft)
        #         self.reRight.set(ctre.ControlMode.PercentOutput, yLeft)
        # elif xRight > 0 and (yLeft > 0 or yLeft < 0):
        #     if self.mode == self.modes.SparkMax:
        #         self.frLeft.set(xRight * turnRatio_2)
        #         self.reLeft.set(xRight * turnRatio_2)
        #         self.frRight.set(xRight * -1 * turnRatio_2)
        #         self.reRight.set(xRight * -1 * turnRatio_2)
        #     else:
        #         self.frLeft.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_2)
        #         self.reLeft.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_2)
        #         self.frRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_2)
        #         self.reRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_2)
        # elif xRight < 0 and (yLeft > 0 or yLeft < 0):
        #     if self.mode == self.modes.SparkMax:
        #         self.frLeft.set(xRight * turnRatio_2)
        #         self.reLeft.set(xRight * turnRatio_2)
        #         self.frRight.set(xRight * -1 * turnRatio_2)
        #         self.reRight.set(xRight * -1 * turnRatio_2)
        #     else:
        #         self.frLeft.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_2)
        #         self.reLeft.set(ctre.ControlMode.PercentOutput, xRight * turnRatio_2)
        #         self.frRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_2)
        #         self.reRight.set(ctre.ControlMode.PercentOutput, xRight * -1 * turnRatio_2)
        # else:
        #     if self.mode == self.modes.SparkMax:
        #         self.frLeft.set(0)
        #         self.reLeft.set(0)
        #         self.frRight.set(0)
        #         self.reRight.set(0)
        #     else:
        #         self.frLeft.set(ctre.ControlMode.PercentOutput, 0)
        #         self.reLeft.set(ctre.ControlMode.PercentOutput, 0)
        #         self.frRight.set(ctre.ControlMode.PercentOutput, 0)
        #         self.reRight.set(ctre.ControlMode.PercentOutput, 0)


if __name__ == "__main__":
    wpilib.run(MyRobot)
