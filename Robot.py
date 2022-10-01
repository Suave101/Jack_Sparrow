import ctre
import rev
import wpilib
from networktables import NetworkTables


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

        self.pdp = wpilib.PowerDistribution()
        self.bia = wpilib.BuiltInAccelerometer()
        NetworkTables.initialize()
        self.smartDash = NetworkTables.getTable("SmartDashboard")

        self.brownStain = False  # Brownout Sustain
        self.brownoutDetection = True  # Enable Brownout Detection

        # Define Things
        self.controllers = []
        # TODO: Automate in the future: https://robotpy.readthedocs.io/projects/wpilib/en/stable/wpilib/CANStatus.html
        # TODO: Automate by scanning data https://robotpy.readthedocs.io/projects/wpilib/en/stable/wpilib/CANData.html
        # TODO: Make robot remember different controller configs https://robotpy.readthedocs.io/projects/wpilib/en/stable/wpilib/Preferences.html
        # TODO: Do above with https://robotpy.readthedocs.io/projects/wpilib/en/stable/wpilib/DriverStation.html#wpilib.DriverStation.getJoystickType
        # Order of controller ID's doesn't matter. Just the amount of each type
        # Do controller config but with motors too
        self.prefs = wpilib.Preferences()
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
        # Start Network Tables Stuff

        def getNetworkTables():
            # Define Dynamic values
            # TODO: Make update rate a non-persistant variable https://robotpy.readthedocs.io/projects/pynetworktables/en/stable/api.html#networktables.NetworkTablesInstance.setUpdateRate

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

            # Brownout Stuff

            if "Brownout_Detection" not in entries:
                self.smartDash.putValue("Brownout_Detection", True)

            # Define Static Variables
            if self.smartDash.containsKey("PDP_Total_Output_Joules"):
                self.smartDash.putValue("PDP_Total_Output_Joules", self.pdp.getTotalEnergy())
            else:
                self.smartDash.setDefaultValue("PDP_Total_Output_Joules", 0)

            if self.smartDash.containsKey("PDP_Temperature_Fahrenheit"):
                self.smartDash.putValue("PDP_Temperature_Fahrenheit", self.pdp.getTemperature())
            else:
                self.smartDash.setDefaultValue("PDP_Temperature_Fahrenheit", 0)

            if self.smartDash.containsKey("PDP_Total_Output_Amperage"):
                self.smartDash.putValue("PDP_Total_Output_Amperage", self.pdp.getTotalCurrent())
            else:
                self.smartDash.setDefaultValue("PDP_Total_Output_Amperage", 0)

            if self.smartDash.containsKey("PDP_Total_Output_Watts"):
                self.smartDash.putValue("PDP_Total_Output_Watts", self.pdp.getTotalPower())
            else:
                self.smartDash.setDefaultValue("PDP_Total_Output_Watts", 0)

            if self.smartDash.containsKey("PDP_Input_Voltage"):
                self.smartDash.putValue("PDP_Input_Voltage", self.pdp.getVoltage())
            else:
                self.smartDash.setDefaultValue("PDP_Input_Voltage", 0)

            if self.smartDash.containsKey("Battery_Percentage"):
                self.smartDash.putValue("Battery_Percentage", (self.pdp.getVoltage()-6.8)/5.2)
            else:
                self.smartDash.setDefaultValue("Battery_Percentage", 0)

            if self.smartDash.containsKey("RIO_Int_Accelerometer_XValue_MpS^2"):
                self.smartDash.putValue("RIO_Int_Accelerometer_XValue_MpS^2", self.bia.getX())
            else:
                self.smartDash.setDefaultValue("RIO_Int_Accelerometer_XValue_MpS^2", 0)

            if self.smartDash.containsKey("RIO_Int_Accelerometer_YValue_MpS^2"):
                self.smartDash.putValue("RIO_Int_Accelerometer_YValue_MpS^2", self.bia.getY())
            else:
                self.smartDash.setDefaultValue("RIO_Int_Accelerometer_YValue_MpS^2", 0)

            if self.smartDash.containsKey("RIO_Int_Accelerometer_ZValue_MpS^2"):
                self.smartDash.putValue("RIO_Int_Accelerometer_ZValue_MpS^2", self.bia.getZ())
            else:
                self.smartDash.setDefaultValue("RIO_Int_Accelerometer_ZValue_MpS^2", 0)

        def brownoutDetection():
            nonlocal self
            if self.smartDash.getValue("Brownout_Detection"):
                if self.smartDash.containsKey("Brownout"):
                    if wpilib.DriverStation.getBatteryVoltage() < 6.8:
                        self.smartDash.putValue("Brownout", "BROWNOUT WARNING")
                        self._Front_Left_Motor.set(0)
                        self._Front_Right_Motor.set(0)
                        self._Back_Right_Motor.set(0)
                        self._Back_Left_Motor.set(0)
                        self._Shooter_Motor.set(0)
                        self._Intake_Motor.set(0)
                else:
                    self.smartDash.setDefaultValue("Brownout", "Not Detected")
            else:
                self.smartDash.delete("Brownout")

        # Initialize Network Tables Interaction 2 seconds after init. Cycles every 0.25 seconds
        self.addPeriodic(getNetworkTables, 0.25, offset=2)
        # Flush Data every 5 seconds for synchronizing network updates
        self.addPeriodic(NetworkTables.flush, 5)
        # Initialize Brownout Detection 1 seconds after init. Cycles every 0.25 seconds
        self.addPeriodic(brownoutDetection, 0.25, offset=1)

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
        # TODO: Implement pnumatics and motors
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
