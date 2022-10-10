import ctre
import pyfrc.tests
import rev
import wpilib
from networktables import NetworkTables
from pyfrc.tests import *


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.pcm = wpilib.PneumaticsControlModule()
        self.safePSI = 120

    def teleopPeriodic(self):
