
"""
 An example of how to define a Python DUT driver
"""
import opentap
from opentap import *
import System
from System import Double, Int32, String
import OpenTap
from OpenTap import Display, Unit
import time
import os

import adi
import paramiko

@attribute(Display(Name="Talise", Description="Talise Description", Group="Manta Ray"))
class Talise(Dut):
	# Add your DUT settings here
	IPaddress = property(String, "192.168.2.1")\
		.add_attribute(OpenTap.Display("IP Address", "The IP Address of the DUT", "DUT Settings"))
			
	def __init__(self):
		super().__init__()
		self.Name="Talise"
		self.dev = None


	def Open(self):
		super().Open()

		self.dev = adi.adrv9009_zu11eg_fmcomms8(
			f"ip:" + self.IPaddress, 
		)

		self.log.Info("Talise Opened")

	def Close(self):
		super().Close()
		self.log.Info("Talise closed")

	def Reboot(self):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=self.IPaddress, port=22, username="root", password="analog")
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("reboot")
		time.sleep(65)
		self.log.Info("Talise Reboot Complete")

	
	def bind_devices(self):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=self.IPaddress, port=22, username="root", password="analog")

		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo -n "spi1.1" > /sys/bus/spi/drivers/adar1000/unbind')
		time.sleep(0.1)
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo -n "spi1.1" > /sys/bus/spi/drivers/adar1000/bind')
		time.sleep(0.1)
		
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo -n "spi1.2" > /sys/bus/spi/drivers/adar1000/unbind')
		time.sleep(0.1)
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo -n "spi1.2" > /sys/bus/spi/drivers/adar1000/bind')
		time.sleep(0.1)

		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo -n "spi1.3" > /sys/bus/spi/drivers/adar1000/unbind')
		time.sleep(0.1)
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo -n "spi1.3" > /sys/bus/spi/drivers/adar1000/bind')
		time.sleep(0.1)

		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo -n "spi1.4" > /sys/bus/spi/drivers/adar1000/unbind')
		time.sleep(0.1)
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo -n "spi1.4" > /sys/bus/spi/drivers/adar1000/bind')
		time.sleep(0.1)
		
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('systemctl restart iiod')
		time.sleep(1)
		ssh.close()
		time.sleep(1)

	
	def PA_ON(self, on):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=self.IPaddress, port=22, username="root", password="analog")
		if on:
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("iio_attr -c stingray0_control 'voltage0' 'raw' 1")
		else:
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("iio_attr -c stingray0_control 'voltage0' 'raw' 0")
		time.sleep(1)
		ssh.close()
		time.sleep(1)
		self.log.Info("PA_ON set to 1 Complete")