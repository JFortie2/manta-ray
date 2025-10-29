
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
from .BFC_Tile import *

@attribute(Display(Name="Quad BFC Tile", Description="Quad BFC Tile Description", Group="Manta Ray"))
class Quad_BFC_Tile(BFC_Tile):
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
	Chip_ID5 = property(String, "adar1000_csb_0_2_1")\
		.add_attribute(OpenTap.Display("Chip ID5", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID6 = property(String, "adar1000_csb_0_2_2")\
		.add_attribute(OpenTap.Display("Chip ID6", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID7 = property(String, "adar1000_csb_0_2_3")\
		.add_attribute(OpenTap.Display("Chip ID7", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID8 = property(String, "adar1000_csb_0_2_4")\
		.add_attribute(OpenTap.Display("Chip ID8", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID9 = property(String, "adar1000_csb_1_1_1")\
		.add_attribute(OpenTap.Display("Chip ID9", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID10 = property(String, "adar1000_csb_1_1_2")\
		.add_attribute(OpenTap.Display("Chip ID10", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID11 = property(String, "adar1000_csb_1_1_3")\
		.add_attribute(OpenTap.Display("Chip ID11", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID12 = property(String, "adar1000_csb_1_1_4")\
		.add_attribute(OpenTap.Display("Chip ID12", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID13 = property(String, "adar1000_csb_1_2_1")\
		.add_attribute(OpenTap.Display("Chip ID13", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID14 = property(String, "adar1000_csb_1_2_2")\
		.add_attribute(OpenTap.Display("Chip ID14", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID15 = property(String, "adar1000_csb_1_2_3")\
		.add_attribute(OpenTap.Display("Chip ID15", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID16 = property(String, "adar1000_csb_1_2_4")\
		.add_attribute(OpenTap.Display("Chip ID16", "The Chip ID of the DUT", "DUT Settings"))
			
	def __init__(self):
		super().__init__()
		self.Name="Quad BFC Tile"
		self.dev = None


	def Open(self):
		super().Open()

		self.log.Info("Quad BFC Tile Opened")

	def Close(self):
		super().Close()
		self.log.Info("Quad BFC Tile closed")

	def Connect(self):
		self.dev = adi.adar1000_array(
			f"ip:" + self.IPaddress, 
			chip_ids= 	[	
							self.Chip_ID, self.Chip_ID2, self.Chip_ID3, self.Chip_ID4, 
			  				self.Chip_ID5, self.Chip_ID6, self.Chip_ID7, self.Chip_ID8, 
							self.Chip_ID9, self.Chip_ID10, self.Chip_ID11, self.Chip_ID12, 
							self.Chip_ID13, self.Chip_ID14, self.Chip_ID15, self.Chip_ID16
						],
    		device_map=	[	
							[2, 1, 6, 5], 
				  			[3, 4, 7, 8], 
							[10, 9, 14, 13], 
							[11, 12, 15, 16]
						],
			element_map=[	
							[1,  2,  3,  4,  5,  6,  7,  8], 
							[9,  10, 11, 12, 13, 14, 15, 16],
							[17, 18, 19, 20, 21, 22, 23, 24], 
							[25, 26, 27, 28, 29, 30, 31, 32],
							[33, 34, 35, 36, 37, 38, 39, 40], 
							[41, 42, 43, 44, 45, 46, 47, 48],
							[49, 50, 51, 52, 53, 54, 55, 56], 
							[57, 58, 59, 60, 61, 62, 63, 64]
						],
			device_element_map={
						1: 	[4, 12, 11, 3],
						2: 	[2, 10, 9, 1],
						3: 	[25, 17, 18, 26],
						4: 	[27, 19, 20, 28],
						5: 	[8, 16, 15, 7],
						6: 	[6, 14, 13, 5],
						7: 	[29, 21, 22, 30],
						8: 	[31, 23, 24, 32],
						9: 	[36, 44, 43, 35],
						10: [34, 42, 41, 33],
						11: [57, 49, 50, 58],
						12: [59, 51, 52, 60],
						13: [40, 48, 47, 39],
						14: [38, 46, 45, 37],
						15: [61, 53, 54, 62],
						16: [63, 55, 56, 64],
			},
		)
		self.log.Info("BFC_Tile Connected")


	def Initialize(self, pa_off=-4.8, pa_on=-4.8, lna_off=-4.8, lna_on=-4.8):
		self.dev.initialize_devices(pa_off, pa_on, lna_off, lna_on)
		for device in self.dev.devices.values():
			#device.rx_vga_vm_bias_current = 0x16 # these are programming example value, but what is impact???
			#device.tx_vga_vm_bias_current = 0x16 # these are programming example value, but what is impact???
			device.mode = "rx"
			device.bias_dac_mode = "on"
			for channel in device.channels:
				# Default channel enable
				channel.rx_enable = True
		self.log.Info("BFC_Tile: " + str(self.Name) + " Initialization Complete")
	
	def GetTemp(self, Channel):
		for device in self.dev.devices.values():
			for channel in device.channels:
				if channel == self.dev.elements[Channel]:
					temp = (device.temperature-145)/0.8+25
					self.log.Info("ADAR1000 temp = " + str(temp) + "°C")
					return temp
	
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