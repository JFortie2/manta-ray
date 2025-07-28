
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

@attribute(Display(Name="Set ADAR1000 Rx", Description="Set ADAR1000 Rx Description", Group="Manta Ray"))
class Adar1000Rx(TestStep):

	# Add your Test Step settings here
	ADAR1000 = property(ADAR1000, None)\
			.add_attribute(Display("ADAR1000", "", "Resources", 0))
	
	Channel = property(Int32, 1)\
			.add_attribute(Display(Name="Adar1000 Channel", Description="", Group="Adar1000 Channel Settings", Order=1))
	
	Enable = property(bool, True)\
			.add_attribute(Display(Name="Rx Enable", Description="", Group="Adar1000 Channel Settings", Order=1))

	gain = property(Int32, 0)\
			.add_attribute(Display(Name="Rx Gain", Description="", Group="Adar1000 Channel Settings", Order=2))

	attenuation = property(bool, True)\
			.add_attribute(Display(Name="Rx Attenuation", Description="", Group="Adar1000 Channel Settings", Order=2))

	phase = property(Double, 0)\
	        .add_attribute(Unit("Degrees", UseEngineeringPrefix=False)) \
			.add_attribute(Display(Name="Rx Phase", Description="", Group="Adar1000 Channel Settings", Order=3)) \

	lnaBias = property(Double, -1)\
	        .add_attribute(Unit("V", UseEngineeringPrefix=True)) \
			.add_attribute(Display(Name="LNA bias level", Description="", Group="Adar1000 Channel Settings", Order=4))

	def __init__(self):
		super().__init__()
		self.Name="Set ADAR1000 Rx"

	def Run(self):
		# Add code here to execute when test step runs
		opentap.debug_this_thread() 
		time.sleep(0.1)
		'''
		self.ADAR1000.GetRxGain(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetRxAttenuation(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetRxPhase(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetLNAvoltage(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetRxEnable(self.Channel)
		time.sleep(0.1)
		'''
		self.log.Info("ADAR1000 Channel " + str(self.Channel))
		self.ADAR1000.SetRxGain(self.Channel, self.gain)
		time.sleep(0.1)
		self.ADAR1000.SetRxAttenuation(self.Channel, self.attenuation)
		time.sleep(0.1)
		self.ADAR1000.SetRxPhase(self.Channel, self.phase)
		time.sleep(0.1)
		self.ADAR1000.SetLNAvoltage(self.Channel, self.lnaBias)
		time.sleep(0.1)
		self.ADAR1000.SetRxEnable(self.Channel, self.Enable)
		time.sleep(0.1)
		self.ADAR1000.dev.latch_rx_settings()
		time.sleep(0.1)
		'''
		self.ADAR1000.GetRxGain(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetRxAttenuation(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetRxPhase(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetLNAvoltage(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetRxEnable(self.Channel)
		time.sleep(0.1)
		'''