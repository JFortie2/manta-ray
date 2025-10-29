
"""
 An example of how to define a Python Test Step
"""
import time
import opentap
from opentap import property
from opentap import *
import System
from System import Double, Int32, String
import OpenTap
from OpenTap import Display, Unit

from .Adar1000 import *

@attribute(Display(Name="Get ADAR1000 Temp", Description="Get ADAR1000 Temp Description", Group="Manta Ray"))
class Adar1000_Temp(TestStep):

	# Add your Test Step settings here
	ADAR1000 = property(ADAR1000, None)\
			.add_attribute(Display("ADAR1000", "", "Resources", 0))
	
	Channel = property(Int32, 1)\
			.add_attribute(Display(Name="Adar1000 Channel", Description="", Group="Adar1000 Channel Settings", Order=1))

	def __init__(self):
		super().__init__()
		self.Name="Get ADAR1000 Temp"

	def Run(self):
		# Add code here to execute when test step runs
		opentap.debug_this_thread() 
		time.sleep(0.1)
		temp = self.ADAR1000.GetTemp(self.Channel)

		self.PublishResult("TestResults", ["Adar1000 Temp"], [temp])