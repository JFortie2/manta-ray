
"""
 An example of how to define a Python Test Step
"""
import time
import opentap
from opentap import *
import System
from System import Double, Int32, String
import OpenTap
from OpenTap import Display, Unit

from .Antenna import *

@attribute(Display(Name="Connect Antenna", Description="Connect Antenna", Group="Manta Ray"))
class Antenna_Connect(TestStep):

	# Add your Test Step settings here
	Antenna = property(Antenna, None)\
			.add_attribute(Display("Antenna", "", "Resources", 0))

	def __init__(self):
		super().__init__()
		self.Name="Connect Antenna"

	def Run(self):
		# Add code here to execute when test step runs
		opentap.debug_this_thread() 
		time.sleep(0.1)
		
		self.log.Info("Connecting Antenna: " + str(self.Antenna.Name))
		time.sleep(0.1)