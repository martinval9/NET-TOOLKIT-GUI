import os

while True:
	os.system("sudo server-info --show --system")

	try:
		input("Pulsa Cualquier tecla para continuar")

	except ValueError:
		pass