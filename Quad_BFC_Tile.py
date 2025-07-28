
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

@attribute(Display(Name="Quad BFC Tile", Description="Quad BFC Tile Description", Group="Manta Ray"))
class Quad_BFC_Tile(Dut):
	# Add your DUT settings here
	IPaddress = property(String, "192.168.2.1")\
		.add_attribute(OpenTap.Display("IP Address", "The IP Address of the DUT", "DUT Settings"))
	Chip_ID1 = property(String, "adar1000_csb_0_1_1")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID2 = property(String, "adar1000_csb_0_1_2")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID3 = property(String, "adar1000_csb_0_1_3")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID4 = property(String, "adar1000_csb_0_1_4")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID5 = property(String, "adar1000_csb_0_2_1")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID6 = property(String, "adar1000_csb_0_2_2")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID7 = property(String, "adar1000_csb_0_2_3")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID8 = property(String, "adar1000_csb_0_2_4")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID9 = property(String, "adar1000_csb_1_1_1")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID10 = property(String, "adar1000_csb_1_1_2")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID11 = property(String, "adar1000_csb_1_1_3")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID12 = property(String, "adar1000_csb_1_1_4")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID13 = property(String, "adar1000_csb_1_2_1")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID14 = property(String, "adar1000_csb_1_2_2")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID15 = property(String, "adar1000_csb_1_2_3")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID16 = property(String, "adar1000_csb_1_2_4")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
			
	def __init__(self):
		super().__init__()
		self.Name="Quad BFC Tile"
		self.dev = None


	def Open(self):
		super().Open()

		self.dev = adi.adar1000_array(
			f"ip:" + self.IPaddress, 
			chip_ids= 	[	
							self.Chip_ID1, self.Chip_ID2, self.Chip_ID3, self.Chip_ID4, 
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

		self.log.Info("Quad BFC Tile Opened")

	def Close(self):
		super().Close()
		self.log.Info("Quad BFC Tile closed")