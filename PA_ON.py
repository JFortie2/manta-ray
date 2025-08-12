
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

from .Talise import *

@attribute(Display(Name="PA_ON", Description="Reboot Talise Description", Group="Manta Ray"))
class PA_ON(TestStep):

	# Add your Test Step settings here
	Talise = property(Talise, None)\
			.add_attribute(Display("Talise", "", "Resources", 0))

	PAon = property(bool, False)\
			.add_attribute(Display(Name="PA_ON", Description="Select for PA_ON high", Group="Adar1000 Settings", Order=20))
	
	def __init__(self):
		super().__init__()
		self.Name="PA_ON"

	def Run(self):
		# Add code here to execute when test step runs
		opentap.debug_this_thread() 
		time.sleep(0.1)
		
		self.Talise.PA_ON(self.PAon)
		time.sleep(0.1)