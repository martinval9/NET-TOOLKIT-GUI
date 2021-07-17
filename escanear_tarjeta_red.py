import os

while True:
	os.system("iwlist wlan0 scanning")
	try:
		input("Pulsa Cualquier tecla para continuar")

	except ValueError:
		pass