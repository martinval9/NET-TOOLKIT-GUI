from getpass import getpass
from colorama import *
import os

while True:
	try:
		id_net = input("SSID de red: ")
		contraseña = getpass("Contraseña: ")
		print(Fore.GREEN)
		os.system("sudo nmcli d wifi connect " + id_net + " password " + contraseña)
		time.sleep(2)
		break

	except ValueError:
		pass