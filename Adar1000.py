
"""
 An example of how to define a Python DUT driver
"""
import opentap
from opentap import *
import System
from System import Double, Int32, String
import OpenTap
from OpenTap import Display, Unit

import adi

@attribute(Display(Name="ADAR1000", Description="ADAR1000 Description", Group="Manta Ray"))
class ADAR1000(Dut):
	# Add your DUT settings here
	IPaddress = property(String, "192.168.2.1")\
		.add_attribute(OpenTap.Display("IP Address", "The IP Address of the DUT", "DUT Settings"))
	Chip_ID = property(String, "adar1000_csb_0_1_1")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
			
	def __init__(self):
		super().__init__()
		self.Name="ADAR1000"
		self.dev = None


	def Open(self):
		super().Open()

		self.log.Info("ADAR1000 Opened")

	def Close(self):
		super().Close()
		self.log.Info("ADAR1000 closed")


	def Connect(self):
		self.dev = adi.adar1000(
			f"ip:" + self.IPaddress, 
			chip_id= self.Chip_ID,
    		array_element_map=[[1, 2, 3, 4]],
			channel_element_map=[2, 1, 4, 3],
		)

		self.log.Info("ADAR1000 Connected")

	def Initialize(self, pa_off=-4.8, pa_on=-4.8, lna_off=-4.8, lna_on=-4.8):
		self.dev.initialize(pa_off, pa_on, lna_off, lna_on)
		self.dev.rx_vga_vm_bias_current = 0x16 # these are programming example value, but what is impact???
		self.dev.tx_vga_vm_bias_current = 0x16 # these are programming example value, but what is impact???
		self.dev.mode = "rx"
		self.dev.bias_dac_mode = "on"
		for channel in self.dev.channels:
            # Default channel enable
			channel.rx_enable = True
		self.log.Info("ADAR1000: " + str(self.Name) + " Initialization Complete")

	def SetRxAttenuation(self, Channel, attenuation):
		self.dev.channels[Channel - 1].rx_attenuator = attenuation
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Attenuation set to: " + str(attenuation))

	def GetRxAttenuation(self, Channel):
		attenuation = self.dev.channels[Channel - 1].rx_attenuator
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Attenuation is: " + str(attenuation))
		return attenuation

	def SetTxAttenuation(self, Channel, attenuation):
		self.dev.channels[Channel - 1].tx_attenuator = attenuation
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Attenuation set to: " + str(attenuation))

	def GetTxAttenuation(self, Channel):
		attenuation = self.dev.channels[Channel - 1].tx_attenuator
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Attenuation is: " + str(attenuation))
		return attenuation

	def SetRxPhase(self, Channel, phase):
		self.dev.channels[Channel - 1].rx_phase = phase
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Phase set to: " + str(phase))

	def GetRxPhase(self, Channel):
		phase = self.dev.channels[Channel - 1].rx_phase
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Phase is: " + str(phase))
		return phase

	def SetTxPhase(self, Channel, phase):
		self.dev.channels[Channel - 1].tx_phase = phase
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Phase set to: " + str(phase))

	def GetTxPhase(self, Channel):
		phase = self.dev.channels[Channel - 1].tx_phase
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Phase is: " + str(phase))
		return phase

	def SetLNAvoltage(self, Channel, bias):
		self.dev.lna_bias_on = bias
		self.log.Info("ADAR1000 Channel " + str(Channel) + " LNA bias voltage set to: " + str(bias))

	def GetLNAvoltage(self, Channel):
		bias = self.dev.lna_bias_on
		self.log.Info("ADAR1000 Channel " + str(Channel) + " LNA bias voltage is: " + str(bias))
		return bias

	def SetPAvoltage(self, Channel, bias):
		self.dev.channels[Channel - 1].pa_bias_on = bias
		self.log.Info("ADAR1000 Channel " + str(Channel) + " PA bias voltage set to: " + str(bias))

	def GetPAvoltage(self, Channel):
		bias = self.dev.channels[Channel - 1].pa_bias_on
		self.log.Info("ADAR1000 Channel " + str(Channel) + " PA bias voltage is: " + str(bias))
		return bias	

	def SetRxGain(self, Channel, gain):
		self.dev.channels[Channel - 1].rx_gain = gain
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Gain set to: " + str(gain))

	def GetRxGain(self, Channel):
		gain = self.dev.channels[Channel - 1].rx_gain
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Gain is: " + str(gain))
		return gain

	def SetTxGain(self, Channel, gain):
		self.dev.channels[Channel - 1].tx_gain = gain
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Gain set to: " + str(gain))

	def GetTxGain(self, Channel):
		gain = self.dev.channels[Channel - 1].tx_gain
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Gain is: " + str(gain))
		return gain	

	def SetRxEnable(self, Channel, on):
		self.dev.channels[Channel - 1].rx_enable = on
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Enable set to: " + str(on))

	def GetRxEnable(self, Channel):
		on = self.dev.channels[Channel - 1].rx_enable
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Enable is: " + str(on))

	def SetTxEnable(self, Channel, on):
		self.dev.channels[Channel - 1].tx_enable = on
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Enable set to: " + str(on))

	def GetTxEnable(self, Channel):
		on = self.dev.channels[Channel - 1].tx_enable
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Enable is: " + str(on))

	def SetTRsource(self, Channel, external):
		if external:
			self.dev.tr_source = "external"
			self.dev.bias_dac_mode = "toggle"
		else:
			self.dev.tr_source = "spi"
			self.dev.bias_dac_mode = "on"
		self.log.Info("ADAR1000 Channel " + str(Channel) + " TR Source set to: " + str(external))

	def GetTRsource(self, Channel):
		external = self.dev.channels[Channel - 1].tr_source
		self.log.Info("ADAR1000 Channel " + str(Channel) + " TR Source is: " + str(external))