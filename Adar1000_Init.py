
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

from .Adar1000 import *

@attribute(Display(Name="Initialize ADAR1000", Description="Initialize ADAR1000", Group="Manta Ray"))
class Adar1000_Init(TestStep):

	# Add your Test Step settings here
	ADAR1000 = property(ADAR1000, None)\
			.add_attribute(Display("ADAR1000", "", "Resources", 0))
	
	lnaBias = property(Double, -4.8)\
	        .add_attribute(Unit("V", UseEngineeringPrefix=True)) \
			.add_attribute(Display(Name="LNA bias level", Description="", Group="Adar1000 Channel Settings", Order=4))

	paBias = property(Double, -4.8)\
	        .add_attribute(Unit("V", UseEngineeringPrefix=True)) \
			.add_attribute(Display(Name="PA bias level", Description="", Group="Adar1000 Channel Settings", Order=4))

	def __init__(self):
		super().__init__()
		self.Name="Initialize ADAR1000"

	def Run(self):
		# Add code here to execute when test step runs
		opentap.debug_this_thread() 
		time.sleep(0.1)
		
		self.log.Info("Initializing ADAR1000: " + str(self.ADAR1000.Name))
		self.ADAR1000.Initialize(-4.8, self.paBias, -4.8, self.lnaBias)
		time.sleep(0.1)