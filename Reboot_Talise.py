
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

@attribute(Display(Name="Reboot Talise", Description="Reboot Talise Description", Group="Manta Ray"))
class Reboot_Talise(TestStep):

	# Add your Test Step settings here
	Talise = property(Talise, None)\
			.add_attribute(Display("Talise", "", "Resources", 0))

	def __init__(self):
		super().__init__()
		self.Name="Reboot Talise"

	def Run(self):
		# Add code here to execute when test step runs
		opentap.debug_this_thread() 
		time.sleep(0.1)
		
		self.log.Info("Rebooting Talise: " + str(self.Talise.Name))
		self.Talise.Reboot()
		time.sleep(0.1)