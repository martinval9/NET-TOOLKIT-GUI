import os

while True:
	try:
		ping = input("Enlace de la pagina: ")
		os.system("ping " + ping)
		break
				
	except ValueError:
		pass