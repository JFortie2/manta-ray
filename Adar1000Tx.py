
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

@attribute(Display(Name="Set ADAR1000 Tx", Description="Set ADAR1000 Tx Description", Group="Manta Ray"))
class Adar1000Tx(TestStep):

	# Add your Test Step settings here
	ADAR1000 = property(ADAR1000, None)\
			.add_attribute(Display("ADAR1000", "", "Resources", 0))
	
	Channel = property(Int32, 1)\
			.add_attribute(Display(Name="Adar1000 Channel", Description="", Group="Adar1000 Channel Settings", Order=1))
	
	Enable = property(bool, True)\
			.add_attribute(Display(Name="Tx Enable", Description="", Group="Adar1000 Channel Settings", Order=1))

	gain = property(Int32, 0)\
			.add_attribute(Display(Name="Tx Gain", Description="", Group="Adar1000 Channel Settings", Order=2))

	attenuation = property(bool, True)\
			.add_attribute(Display(Name="Tx Attenuation", Description="", Group="Adar1000 Channel Settings", Order=2))

	phase = property(Double, 0)\
	        .add_attribute(Unit("Degrees", UseEngineeringPrefix=False)) \
			.add_attribute(Display(Name="Tx Phase", Description="", Group="Adar1000 Channel Settings", Order=3))

	paBias = property(Double, -2)\
	        .add_attribute(Unit("V", UseEngineeringPrefix=True)) \
			.add_attribute(Display(Name="PA bias level", Description="", Group="Adar1000 Channel Settings", Order=4))

	def __init__(self):
		super().__init__()
		self.Name="Set ADAR1000 Tx"

	def Run(self):
		# Add code here to execute when test step runs
		opentap.debug_this_thread() 
		time.sleep(0.1)
		'''
		self.ADAR1000.GetTxGain(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetTxAttenuation(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetTxPhase(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetLNAvoltage(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetTxEnable(self.Channel)
		time.sleep(0.1)
		'''
		self.log.Info("ADAR1000 Channel " + str(self.Channel))
		self.ADAR1000.SetTxGain(self.Channel, self.gain)
		time.sleep(0.1)
		self.ADAR1000.SetTxAttenuation(self.Channel, self.attenuation)
		time.sleep(0.1)
		self.ADAR1000.SetTxPhase(self.Channel, self.phase)
		time.sleep(0.1)
		self.ADAR1000.SetPAvoltage(self.Channel, self.paBias)
		time.sleep(0.1)
		self.ADAR1000.SetTxEnable(self.Channel, self.Enable)
		time.sleep(0.1)
		self.ADAR1000.dev.latch_tx_settings()
		time.sleep(0.1)
		'''
		self.ADAR1000.GetTxGain(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetTxAttenuation(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetTxPhase(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetLNAvoltage(self.Channel)
		time.sleep(0.1)
		self.ADAR1000.GetTxEnable(self.Channel)
		time.sleep(0.1)
		'''
	"""
	@gain.setter
	def gain(self, value):
		if value > 127:
			self._gain = 127
		elif value < 0:
			self._gain = 0
		else:
			self._gain = value
	"""