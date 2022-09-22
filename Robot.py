import pyfrc
import ctre
import rev
import wpilib


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        def getNetworkTables():
            # TODO: Define get NetworkTables
            pass
        self.addPeriodic(getNetworkTables, 5, offset=2)
        # Get Network tables Data || Define Things
        self.CANSparkMaxType = rev.CANSparkMaxLowLevel.MotorType(0)  # 0 is Brushed and 1 is Brushless
        self.prefs = wpilib.Preferences()
        if self.prefs.containsKey("Front_Left_Motor"):
            _temp = self.prefs.getString("Front_Left_Motor")
            if _temp == "Spark_Max":
                self._FLM = rev.CANSparkMax(0, self.CANSparkMaxType)
            elif _temp == "Talon_FX":
                # TODO: Add Talon_FX Functionality
                pass
            elif _temp == "Talon_SRX":
                # TODO: Add Talon_SRX Functionality
                pass
            elif _temp == "Victor_SPX":
                # TODO: Add Victor_SPX Functionality
                pass
            del _temp
        else:
            self.prefs.initString("Front_Left_Motor", "Spark_Max")
            self._FLM = rev.CANSparkMax(0, self.CANSparkMaxType)
        # Define Game Stuff
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        # if self.timer.get() < 2.0:
        #     self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        # else:
        #     self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        # self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
