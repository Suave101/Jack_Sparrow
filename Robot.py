import ctre
import rev
import wpilib
from networktables import NetworkTables


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        NetworkTables.initialize()
        self.smartDash = NetworkTables.getTable("SmartDashboard")

        # Define Things
        # TODO: Automate in the future: https://robotpy.readthedocs.io/projects/wpilib/en/stable/wpilib/CANStatus.html
        self.prefs = wpilib.Preferences()
        if self.prefs.containsKey("Spark_Max_Brushed"):
            self.CANSparkMaxType = rev.CANSparkMaxLowLevel.MotorType(int(self.prefs.getString("Spark_Max_Brushed")))
        else:
            self.prefs.initString("Front_Left_Motor", "0")
            self.CANSparkMaxType = rev.CANSparkMaxLowLevel.MotorType(0)  # 0 is Brushed and 1 is Brushless
        if self.prefs.containsKey("Front_Left_Motor"):
            if self.prefs.containsKey("Front_Left_Motor_ID"):
                pass
            else:
                self.prefs.initInt("Front_Left_Motor", "0")
            if self.prefs.getString("Front_Left_Motor") == "Spark_Max":
                self._Front_Left_Motor = rev.CANSparkMax(int(self.prefs.getString("Front_Left_Motor_ID")), self.CANSparkMaxType)
            elif self.prefs.getString("Front_Left_Motor") == "Talon_FX":
                self._Front_Left_Motor = ctre.TalonFX(int(self.prefs.getString("Front_Left_Motor_ID")))
            elif self.prefs.getString("Front_Left_Motor") == "Talon_SRX":
                self._Front_Left_Motor = ctre.TalonSRX(int(self.prefs.getString("Front_Left_Motor_ID")))
            elif self.prefs.getString("Front_Left_Motor") == "Victor_SPX":
                self._Front_Left_Motor = ctre.VictorSPX(int(self.prefs.getString("Front_Left_Motor_ID")))
        else:
            self.prefs.initString("Front_Left_Motor", "Spark_Max")
            self._Front_Left_Motor = rev.CANSparkMax(int(self.prefs.getString("Front_Left_Motor_ID")), self.CANSparkMaxType)
        if self.prefs.containsKey("Front_Right_Motor"):
            if self.prefs.containsKey("Front_Right_Motor_ID"):
                pass
            else:
                self.prefs.initInt("Front_Right_Motor", "1")
            if self.prefs.getString("Front_Right_Motor") == "Spark_Max":
                self._Front_Right_Motor = rev.CANSparkMax(int(self.prefs.getString("Front_Right_Motor_ID")), self.CANSparkMaxType)
            elif self.prefs.getString("Front_Right_Motor") == "Talon_FX":
                self._Front_Right_Motor = ctre.TalonFX(int(self.prefs.getString("Front_Right_Motor_ID")))
            elif self.prefs.getString("Front_Right_Motor") == "Talon_SRX":
                self._Front_Right_Motor = ctre.TalonSRX(int(self.prefs.getString("Front_Right_Motor_ID")))
            elif self.prefs.getString("Front_Right_Motor") == "Victor_SPX":
                self._Front_Right_Motor = ctre.VictorSPX(int(self.prefs.getString("Front_Right_Motor_ID")))
        else:
            self.prefs.initString("Front_Right_Motor", "Spark_Max")
            self._Front_Right_Motor = rev.CANSparkMax(int(self.prefs.getString("Front_Right_Motor_ID")), self.CANSparkMaxType)
        if self.prefs.containsKey("Back_Right_Motor"):
            if self.prefs.containsKey("Back_Right_Motor_ID"):
                pass
            else:
                self.prefs.initInt("Back_Right_Motor", "2")
            if self.prefs.getString("Back_Right_Motor") == "Spark_Max":
                self._Back_Right_Motor = rev.CANSparkMax(int(self.prefs.getString("Back_Right_Motor_ID")), self.CANSparkMaxType)
            elif self.prefs.getString("Back_Right_Motor") == "Talon_FX":
                self._Back_Right_Motor = ctre.TalonFX(int(self.prefs.getString("Back_Right_Motor_ID")))
            elif self.prefs.getString("Back_Right_Motor") == "Talon_SRX":
                self._Back_Right_Motor = ctre.TalonSRX(int(self.prefs.getString("Back_Right_Motor_ID")))
            elif self.prefs.getString("Back_Right_Motor") == "Victor_SPX":
                self._Back_Right_Motor = ctre.VictorSPX(int(self.prefs.getString("Back_Right_Motor_ID")))
        else:
            self.prefs.initString("Back_Right_Motor", "Spark_Max")
            self._Back_Right_Motor = rev.CANSparkMax(int(self.prefs.getString("Back_Right_Motor_ID")), self.CANSparkMaxType)
        if self.prefs.containsKey("Back_Left_Motor"):
            if self.prefs.containsKey("Back_Left_Motor_ID"):
                pass
            else:
                self.prefs.initInt("Back_Left_Motor", "3")
            if self.prefs.getString("Back_Left_Motor") == "Spark_Max":
                self._Back_Left_Motor = rev.CANSparkMax(int(self.prefs.getString("Back_Left_Motor_ID")), self.CANSparkMaxType)
            elif self.prefs.getString("Back_Left_Motor") == "Talon_FX":
                self._Back_Left_Motor = ctre.TalonFX(int(self.prefs.getString("Back_Left_Motor_ID")))
            elif self.prefs.getString("Back_Left_Motor") == "Talon_SRX":
                self._Back_Left_Motor = ctre.TalonSRX(int(self.prefs.getString("Back_Left_Motor_ID")))
            elif self.prefs.getString("Back_Left_Motor") == "Victor_SPX":
                self._Back_Left_Motor = ctre.VictorSPX(int(self.prefs.getString("Back_Left_Motor_ID")))
        else:
            self.prefs.initString("Back_Left_Motor", "Spark_Max")
            self._Back_Left_Motor = rev.CANSparkMax(int(self.prefs.getString("Back_Left_Motor_ID")), self.CANSparkMaxType)
        if self.prefs.containsKey("Shooter_Motor"):
            if self.prefs.containsKey("Shooter_Motor_ID"):
                pass
            else:
                self.prefs.initInt("Shooter_Motor", "4")
            if self.prefs.getString("Shooter_Motor") == "Spark_Max":
                self._Shooter_Motor = rev.CANSparkMax(int(self.prefs.getString("Shooter_Motor_ID")), self.CANSparkMaxType)
            elif self.prefs.getString("Shooter_Motor") == "Talon_FX":
                self._Shooter_Motor = ctre.TalonFX(int(self.prefs.getString("Shooter_Motor_ID")))
            elif self.prefs.getString("Shooter_Motor") == "Talon_SRX":
                self._Shooter_Motor = ctre.TalonSRX(int(self.prefs.getString("Shooter_Motor_ID")))
            elif self.prefs.getString("Shooter_Motor") == "Victor_SPX":
                self._Shooter_Motor = ctre.VictorSPX(int(self.prefs.getString("Shooter_Motor_ID")))
        else:
            self.prefs.initString("Shooter_Motor", "Talon_FX")
            self._Shooter_Motor = ctre.TalonFX(int(self.prefs.getString("Shooter_Motor_ID")))
        if self.prefs.containsKey("Intake_Motor"):
            if self.prefs.containsKey("Intake_Motor_ID"):
                pass
            else:
                self.prefs.initInt("Intake_Motor", "5")
            if self.prefs.getString("Intake_Motor") == "Spark_Max":
                self._Intake_Motor = rev.CANSparkMax(int(self.prefs.getString("Intake_Motor_ID")), self.CANSparkMaxType)
            elif self.prefs.getString("Intake_Motor") == "Talon_FX":
                self._Intake_Motor = ctre.TalonFX(int(self.prefs.getString("Intake_Motor_ID")))
            elif self.prefs.getString("Intake_Motor") == "Talon_SRX":
                self._Intake_Motor = ctre.TalonSRX(int(self.prefs.getString("Intake_Motor_ID")))
            elif self.prefs.getString("Intake_Motor") == "Victor_SPX":
                self._Intake_Motor = ctre.VictorSPX(int(self.prefs.getString("Intake_Motor_ID")))
        else:
            self.prefs.initString("Intake_Motor", "Talon_SRX")
            self._Intake_Motor = ctre.TalonSRX(int(self.prefs.getString("Intake_Motor_ID")))
        # Start Network Tables Stuff

        def getNetworkTables():
            nonlocal self
            entries = self.smartDash.getEntries("")
            for preference in self.prefs.getKeys():
                if preference not in entries:
                    self.smartDash.setDefaultString(str(preference), self.prefs.getString(preference))
                else:
                    if self.smartDash.getString(preference) != self.prefs.getString(preference):
                        if preference == "Front_Left_Motor":
                            if self.smartDash.getString(preference) == "Spark_Max":
                                self._Front_Left_Motor = rev.CANSparkMax(
                                    int(self.prefs.getString("Front_Left_Motor_ID")), self.CANSparkMaxType)
                            elif self.smartDash.getString(preference) == "Talon_FX":
                                self._Front_Left_Motor = ctre.TalonFX(int(self.prefs.getString("Front_Left_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Talon_SRX":
                                self._Front_Left_Motor = ctre.TalonSRX(int(self.prefs.getString("Front_Left_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Victor_SPX":
                                self._Front_Left_Motor = ctre.VictorSPX(
                                    int(self.prefs.getString("Front_Left_Motor_ID")))
                            else:
                                self.smartDash.putString(preference, f"Invalid String - Defaulted to {self.prefs.getString(preference)}")
                        if preference == "Front_Right_Motor":
                            if self.smartDash.getString(preference) == "Spark_Max":
                                self._Front_Right_Motor = rev.CANSparkMax(
                                    int(self.prefs.getString("Front_Right_Motor_ID")), self.CANSparkMaxType)
                            elif self.smartDash.getString(preference) == "Talon_FX":
                                self._Front_Right_Motor = ctre.TalonFX(int(self.prefs.getString("Front_Right_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Talon_SRX":
                                self._Front_Right_Motor = ctre.TalonSRX(int(self.prefs.getString("Front_Right_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Victor_SPX":
                                self._Front_Right_Motor = ctre.VictorSPX(
                                    int(self.prefs.getString("Front_Right_Motor_ID")))
                            else:
                                self.smartDash.putString(preference, f"Invalid String - Defaulted to {self.prefs.getString(preference)}")
                        if preference == "Back_Left_Motor":
                            if self.smartDash.getString(preference) == "Spark_Max":
                                self._Back_Left_Motor = rev.CANSparkMax(
                                    int(self.prefs.getString("Back_Left_Motor_ID")), self.CANSparkMaxType)
                            elif self.smartDash.getString(preference) == "Talon_FX":
                                self._Back_Left_Motor = ctre.TalonFX(int(self.prefs.getString("Back_Left_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Talon_SRX":
                                self._Back_Left_Motor = ctre.TalonSRX(int(self.prefs.getString("Back_Left_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Victor_SPX":
                                self._Back_Left_Motor = ctre.VictorSPX(
                                    int(self.prefs.getString("Back_Left_Motor_ID")))
                            else:
                                self.smartDash.putString(preference, f"Invalid String - Defaulted to {self.prefs.getString(preference)}")
                        if preference == "Back_Right_Motor":
                            if self.smartDash.getString(preference) == "Spark_Max":
                                self._Back_Right_Motor = rev.CANSparkMax(
                                    int(self.prefs.getString("Back_Right_Motor_ID")), self.CANSparkMaxType)
                            elif self.smartDash.getString(preference) == "Talon_FX":
                                self._Back_Right_Motor = ctre.TalonFX(int(self.prefs.getString("Back_Right_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Talon_SRX":
                                self._Back_Right_Motor = ctre.TalonSRX(int(self.prefs.getString("Back_Right_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Victor_SPX":
                                self._Back_Right_Motor = ctre.VictorSPX(
                                    int(self.prefs.getString("Back_Right_Motor_ID")))
                            else:
                                self.smartDash.putString(preference, f"Invalid String - Defaulted to {self.prefs.getString(preference)}")
                        if preference == "Shooter_Motor":
                            if self.smartDash.getString(preference) == "Spark_Max":
                                self._Shooter_Motor = rev.CANSparkMax(
                                    int(self.prefs.getString("Shooter_Motor_ID")), self.CANSparkMaxType)
                            elif self.smartDash.getString(preference) == "Talon_FX":
                                self._Shooter_Motor = ctre.TalonFX(int(self.prefs.getString("Shooter_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Talon_SRX":
                                self._Shooter_Motor = ctre.TalonSRX(int(self.prefs.getString("Shooter_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Victor_SPX":
                                self._Shooter_Motor = ctre.VictorSPX(
                                    int(self.prefs.getString("Shooter_Motor_ID")))
                            else:
                                self.smartDash.putString(preference, f"Invalid String - Defaulted to {self.prefs.getString(preference)}")
                        if preference == "Intake_Motor":
                            if self.smartDash.getString(preference) == "Spark_Max":
                                self._Intake_Motor = rev.CANSparkMax(
                                    int(self.prefs.getString("Intake_Motor_ID")), self.CANSparkMaxType)
                            elif self.smartDash.getString(preference) == "Talon_FX":
                                self._Intake_Motor = ctre.TalonFX(int(self.prefs.getString("Intake_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Talon_SRX":
                                self._Intake_Motor = ctre.TalonSRX(int(self.prefs.getString("Intake_Motor_ID")))
                            elif self.smartDash.getString(preference) == "Victor_SPX":
                                self._Intake_Motor = ctre.VictorSPX(
                                    int(self.prefs.getString("Intake_Motor_ID")))
                            else:
                                self.smartDash.putString(preference, f"Invalid String - Defaulted to {self.prefs.getString(preference)}")
                        if preference == "Spark_Max_Brushed":
                            if self.prefs.containsKey("Spark_Max_Brushed"):
                                self.CANSparkMaxType = rev.CANSparkMaxLowLevel.MotorType(
                                    int(self.prefs.getString("Spark_Max_Brushed")))
                            else:
                                self.prefs.initString("Front_Left_Motor", "0")
                                self.CANSparkMaxType = rev.CANSparkMaxLowLevel.MotorType(
                                    0)  # 0 is Brushed and 1 is Brushless

        self.addPeriodic(getNetworkTables, 0.25, offset=2)

        # Define Game Stuff getJoystickIsXbox()
        self.controller = wpilib.XboxController(0)
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
