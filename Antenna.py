
"""
 An example of how to define a Python DUT driver
"""
import opentap
from opentap import *
import System
from System import Double, Int32, String
import OpenTap
from OpenTap import Display, Unit
import time
import os

import adi
import paramiko

@attribute(Display(Name="Antenna", Description="Antenna Description", Group="Manta Ray"))
class Antenna(Dut):
	# Add your DUT settings here
			
	def __init__(self):
		super().__init__()
		self.Name="Antenna"
		self.dev = None

	def Open(self):
		super().Open()
		self.log.Info("Antenna Opened")

	def Close(self):
		super().Close()
		self.log.Info("Antenna closed")