
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
class BFC_Tile(Dut):
	# Add your DUT settings here
	IPaddress = property(String, "192.168.2.1")\
		.add_attribute(OpenTap.Display("IP Address", "The IP Address of the DUT", "DUT Settings"))
	Chip_ID1 = property(String, "adar1000_csb_1_1")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID2 = property(String, "adar1000_csb_1_2")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID3 = property(String, "adar1000_csb_1_3")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
	Chip_ID4 = property(String, "adar1000_csb_1_4")\
		.add_attribute(OpenTap.Display("Chip ID", "The Chip ID of the DUT", "DUT Settings"))
			
	def __init__(self):
		super().__init__()
		self.Name="BFC Tile"
		self.dev = None


	def Open(self):
		super().Open()

		self.dev = adi.adar1000_array(
			f"ip:" + self.IPaddress, 
			chip_ids= 	[	
							self.Chip_ID1, self.Chip_ID2, self.Chip_ID3, self.Chip_ID4
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

		self.log.Info("BFC Tile Opened")

	def Close(self):
		super().Close()
		self.log.Info("BFC Tile closed")