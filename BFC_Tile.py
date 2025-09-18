
"""
 An example of how to define a Python DUT driver
"""
import opentap
from opentap import *
import System
from System import Double, Int32, String
import OpenTap
from OpenTap import Display, Unit

from .Adar1000 import *
import adi

@attribute(Display(Name="BFC Tile", Description="BFC Tile Description", Group="Manta Ray"))
class BFC_Tile(ADAR1000):
	# Add your DUT settings here
	IPaddress = property(String, "192.168.2.1")\
		.add_attribute(OpenTap.Display("IP Address", "The IP Address of the DUT", "DUT Settings"))
	Chip_ID = property(String, "adar1000_csb_0_1_1")\
		.add_attribute(OpenTap.Display("Chip ID1", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID2 = property(String, "adar1000_csb_0_1_2")\
		.add_attribute(OpenTap.Display("Chip ID2", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID3 = property(String, "adar1000_csb_0_1_3")\
		.add_attribute(OpenTap.Display("Chip ID3", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID4 = property(String, "adar1000_csb_0_1_4")\
		.add_attribute(OpenTap.Display("Chip ID4", "The Chip ID of the DUT", "DUT Settings"))
			
	def __init__(self):
		super().__init__()
		self.Name="BFC Tile"
		self.dev = None


	def Open(self):
		super().Open()

		self.log.Info("BFC Tile Opened")

	def Close(self):
		super().Close()
		self.log.Info("BFC Tile closed")

	def Connect(self):
		self.dev = adi.adar1000_array(
			f"ip:" + self.IPaddress, 
			chip_ids= 	[	
							self.Chip_ID, self.Chip_ID2, self.Chip_ID3, self.Chip_ID4
			   			],
    		device_map=	[
							[2, 1], 
				   			[3, 4]
						],
			element_map=[
							[1, 2, 3, 4], 
							[5, 6, 7, 8], 
							[9, 10, 11, 12], 
							[13, 14, 15, 16]
						],
			device_element_map={
						1: 	[4, 8, 7, 3],
						2: 	[2, 6, 5, 1],
						3: 	[13, 9, 10, 14],
						4: 	[15, 11, 12, 16],
			},
		)
		self.log.Info("BFC_Tile Connected")


	def Initialize(self, pa_off=-4.8, pa_on=-4.8, lna_off=-4.8, lna_on=-4.8):
		self.dev.initialize_devices(pa_off, pa_on, lna_off, lna_on)
		for device in self.dev.devices.values():
			device.rx_vga_vm_bias_current = 0x16 # these are programming example value, but what is impact???
			device.tx_vga_vm_bias_current = 0x16 # these are programming example value, but what is impact???
			device.mode = "rx"
			device.bias_dac_mode = "on"
			for channel in device.channels:
				# Default channel enable
				channel.rx_enable = True
		self.log.Info("BFC_Tile: " + str(self.Name) + " Initialization Complete")
	
	def SetRxAttenuation(self, Channel, attenuation):
		self.dev.elements[Channel].rx_attenuator = attenuation
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Attenuation set to: " + str(attenuation))

	def GetRxAttenuation(self, Channel):
		attenuation = self.dev.elements[Channel].rx_attenuator
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Attenuation is: " + str(attenuation))
		return attenuation

	def SetTxAttenuation(self, Channel, attenuation):
		self.dev.elements[Channel].tx_attenuator = attenuation
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Attenuation set to: " + str(attenuation))

	def GetTxAttenuation(self, Channel):
		attenuation = self.dev.elements[Channel].tx_attenuator
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Attenuation is: " + str(attenuation))
		return attenuation

	def SetRxPhase(self, Channel, phase):
		self.dev.elements[Channel].rx_phase = phase
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Phase set to: " + str(phase))

	def GetRxPhase(self, Channel):
		phase = self.dev.elements[Channel].rx_phase
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Phase is: " + str(phase))
		return phase

	def SetTxPhase(self, Channel, phase):
		self.dev.elements[Channel].tx_phase = phase
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Phase set to: " + str(phase))

	def GetTxPhase(self, Channel):
		phase = self.dev.elements[Channel].tx_phase
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Phase is: " + str(phase))
		return phase

	def SetLNAvoltage(self, Channel, bias):
		for device in self.dev.devices.values():
			for channel in device.channels:
				if channel == self.dev.elements[Channel]:
					device.lna_bias_on = bias
					self.log.Info("ADAR1000 Channel " + str(Channel) + " LNA bias voltage set to: " + str(bias))
					return

	def GetLNAvoltage(self, Channel):
		for device in self.dev.devices.values():
			for channel in device.channels:
				if channel == self.dev.elements[Channel]:
					bias = device.lna_bias_on
					self.log.Info("ADAR1000 Channel " + str(Channel) + " LNA bias voltage is: " + str(bias))
					return bias

	def SetPAvoltage(self, Channel, bias):
		self.dev.elements[Channel].pa_bias_on = bias
		self.log.Info("ADAR1000 Channel " + str(Channel) + " PA bias voltage set to: " + str(bias))

	def GetPAvoltage(self, Channel):
		bias = self.dev.elements[Channel].pa_bias_on
		self.log.Info("ADAR1000 Channel " + str(Channel) + " PA bias voltage is: " + str(bias))
		return bias	

	def SetRxGain(self, Channel, gain):
		self.dev.elements[Channel].rx_gain = gain
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Gain set to: " + str(gain))

	def GetRxGain(self, Channel):
		gain = self.dev.elements[Channel].rx_gain
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Gain is: " + str(gain))
		return gain

	def SetTxGain(self, Channel, gain):
		self.dev.elements[Channel].tx_gain = gain
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Gain set to: " + str(gain))

	def GetTxGain(self, Channel):
		gain = self.dev.elements[Channel].tx_gain
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Gain is: " + str(gain))
		return gain	

	def SetRxEnable(self, Channel, on):
		self.dev.elements[Channel].rx_enable = on
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Enable set to: " + str(on))

	def GetRxEnable(self, Channel):
		on = self.dev.elements[Channel].rx_enable
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Rx Enable is: " + str(on))

	def SetTxEnable(self, Channel, on):
		self.dev.elements[Channel].tx_enable = on
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Enable set to: " + str(on))

	def GetTxEnable(self, Channel):
		on = self.dev.elements[Channel].tx_enable
		self.log.Info("ADAR1000 Channel " + str(Channel) + " Tx Enable is: " + str(on))

	def SetTRsource(self, Channel, external):
		for device in self.dev.devices.values():
			for channel in device.channels:
				if channel == self.dev.elements[Channel]:
					if external:
						device.tr_source = "external"
						device.bias_dac_mode = "toggle"
					else:
						device.tr_source = "spi"
						device.bias_dac_mode = "on"
					self.log.Info("ADAR1000 Channel " + str(Channel) + " TR Source set to: " + str(external))
					return

	def GetTRsource(self, Channel):
		for device in self.dev.devices.values():
			for channel in device.channels:
				if channel == self.dev.elements[Channel]:
					external = device.tr_source
					self.log.Info("ADAR1000 Channel " + str(Channel) + " TR Source is: " + str(external))
					return