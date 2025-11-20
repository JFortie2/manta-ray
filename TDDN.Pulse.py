import time
import opentap
import paramiko
from opentap import *
import System
from System import Double, Int32, String
import OpenTap
from OpenTap import Display, Unit

import adi

from .Talise import *

@attribute(Display(Name="TDDN Pulse", Description="Pulse TX", Group="Manta Ray"))
class TDD_Pulse(TestStep):

	# Add your Test Step settings here
	Talise = property(Talise, None)\
			.add_attribute(Display("Talise", "", "Resources", Order=0))
	TDDN_Pulse = property(bool, False)\
			.add_attribute(Display(Name="TDDN_PULSE", Description="Trigger TR Pin on ", Group="Adar1000 Settings", Order=20))

	def __init__(self):
		super().__init__()
		self.Name="TDDN Pulse"

	def Run(self):
		# Add code here to execute when test step runs
		opentap.debug_this_thread() 
		time.sleep(0.1)
		
		self.log.Info("TDD Pulse: " + str(self.Talise.Name))

		# Prefer using the assigned Talise DUT to perform TDDN actions
		if self.Talise is None:
			self.log.Error("TDDN Pulse test step has no Talise resource assigned")
			return

		# call the DUT method which encapsulates TDDN logic and state
		try:
			self.Talise.TDDN_Pulse()
		except Exception as e:
			self.log.Error(f"Error while running Talise.TDDN_Pulse(): {e}")
			return

		time.sleep(0.1)
