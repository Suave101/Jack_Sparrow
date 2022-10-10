import ctre
import pyfrc.tests
import rev
import wpilib
from networktables import NetworkTables
from pyfrc.tests import *


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.pcm = wpilib.PneumaticsControlModule()
        self.safePSI = 100
        if self.pcm.getCompressor():
            self.compressor = wpilib.Compressor(moduleType=self.pcm.getCompressorConfigType())
            self.solenoid = self.pcm.makeSolenoid(1)  # Solenoid Number
        else:
            wpilib.reportWarning("Compressor Not Found!!!")

    def disabledInit(self):
        self.compressor.stop()
        # if self.compressor.getPressure() > self.safePSI:
        #     self.compressor.stop()
        # else:
        #     self.compressor.start()

    def disabledPeriodic(self):
        self.compressor.stop()
        # if self.compressor.getPressure() > self.safePSI:
        #     self.compressor.stop()
        # else:
        #     self.compressor.start()

    def teleopPeriodic(self):
        if self.compressor.getPressure() > self.safePSI:
            self.compressor.stop()
        else:
            self.compressor.start()

