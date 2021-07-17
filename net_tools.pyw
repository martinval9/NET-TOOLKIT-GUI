from tkinter import *
from tkinter import messagebox as MessageBox

import os

root = Tk()
root.title("Net_Toolkit")
root.resizable(0,0)
root.config(bg = "#1e1e1e")

#---FUNCIONES---

def conectar():
	os.system("kitty python3 connect.py")

def interfaz():
	os.system("kitty sudo ifconfig wlan0 up")
	messagebox.showInfo("Interfaz levantada","Interfaz levantada")

def desconectar():
	os.system("kitty sudo ifconfig wlan0 down")
	messagebox.showInfo("Wifi Desconectado","Wifi Desconectado")

def escanear():
	os.system("kitty sudo connmanctl scan wifi")

def redes():
	os.system("kitty sudo connmanctl services")

def agente():
	os.system("kitty sudo connmanctl agent on")

def ip():
	os.system("kitty ifconfig -a && sleep 20")

def grafico():
	os.system("kitty sudo etherape")

def wireshark():
	os.system("kitty sudo wireshark")

def zenmap():
	os.system("kitty sudo zenmap")

def nombre_tarjeta_red():
	os.system("kitty python3 nombre_tarjeta_red.py")

def escanear_tarjeta_red():
	os.system("kitty python3 escanear_tarjeta_red.py")

def bash():
	os.system("kitty bash")

def ping():
	os.system("kitty python3 ping.py")

def info_detallada():
	os.system("kitty python3 info_detallada.py")

def fast():
	os.system("kitty ./fast")

def net_checker():
	os.system("kitty ./net_checker")

def network_top():
	os.system("kitty network-top")
"""
imagen = PhotoImage(file = "net2.gif")
imagen.config(width = 200,
              height = 15)
Label(root,
    image = imagen,
    border = 0).grid(row = 0, column = 1)
"""
Label(text = "直 Net Toolkit 直",
      bg = "#1e1e1e",
      fg = "#00ffa4",
      font = "JetBrainsMonoExtraBold 12").grid(row = 1, column = 1)

boton_conectar = Button(text = "Conectarse a una red wifi",
                        width = 38,
                        command = conectar,
                        bg = "#000",
                        fg = "#fff",
                        activebackground = "#1e1e1e",
                        activeforeground = "#00ffa4",
                        border = 0,
                        font = "JetBrainsMonoMedium 9").grid(row = 2, column = 0)

boton_interfaz_de_red = Button(text = "Levantar Interfaz de red",
                               width = 38,
                               command = interfaz, 
                               bg = "#000",
                               fg = "#fff", 
                               activebackground = "#1e1e1e", 
                               activeforeground = "#00ffa4", 
                               border = 0, 
                               font = "JetBrainsMonoMedium 9").grid(row = 2, column = 1)

boton_desconectar_wifi = Button(text = "Desconectar Wifi",
                                width = 38,
                                command = desconectar, 
                                bg = "#000", 
                                fg = "#fff", 
                                activebackground = "#1e1e1e", 
                                activeforeground = "#00ffa4", 
                                border = 0, 
                                font = "JetBrainsMonoMedium 9").grid(row = 2, column = 2)

boton_escanear_wifi = Button(text = "Escanear Wifi",
                             width = 38,
                             command = escanear, 
                             bg = "#000", 
                             fg = "#fff", 
                             activebackground = "#1e1e1e", 
                             activeforeground = "#00ffa4", 
                             border = 0, 
                             font = "JetBrainsMonoMedium 9").grid(row = 3, column = 0)

boton_redeswifi = Button(text = "Ver redes Wifi disponibles",
                         width = 38,
                         command = redes, 
                         bg = "#000", 
                         fg = "#fff", 
                         activebackground = "#1e1e1e", 
                         activeforeground = "#00ffa4", 
                         border = 0, 
                         font = "JetBrainsMonoMedium 9").grid(row = 3, column = 1)

boton_registrar_agente = Button(text = "Registrar agente",
                                width = 38,
                                command = agente,
                                bg = "#000",
                                fg = "#fff",
                                activebackground = "#1e1e1e",
                                activeforeground = "#00ffa4",
                                border = 0,
                                font = "JetBrainsMonoMedium 9").grid(row = 3, column = 2)

boton_ip = Button(text = "Dirección Ip",
                  width = 38,
                  command = ip, 
                  bg = "#000", 
                  fg = "#fff", 
                  activebackground = "#1e1e1e", 
                  activeforeground = "#00ffa4", 
                  border = 0, 
                  font = "JetBrainsMonoMedium 9").grid(row = 4, column = 0)

boton_grafico_red = Button(text = "Grafico de red",
                           width = 38, 
                           command = grafico, 
                           bg = "#000", 
                           fg = "#fff", 
                           activebackground = "#1e1e1e", 
                           activeforeground = "#00ffa4", 
                           border = 0, 
                           font = "JetBrainsMonoMedium 9").grid(row = 4, column = 1)

boton_wireshark = Button(text = "Wireshark",
                         width = 38, 
                         command = wireshark, 
                         bg = "#000", 
                         fg = "#fff", 
                         activebackground = "#1e1e1e", 
                         activeforeground = "#00ffa4", 
                         border = 0, 
                         font = "JetBrainsMonoMedium 9").grid(row = 4, column = 2)

boton_nmap = Button(text = "Zenmap",
                    width = 38, 
                    command = zenmap, 
                    bg = "#000", 
                    fg = "#fff", 
                    activebackground = "#1e1e1e", 
                    activeforeground = "#00ffa4", 
                    border = 0, 
                    font = "JetBrainsMonoMedium 9").grid(row = 5, column = 0)

boton_nombre_tarjeta_red = Button(text = "Nombre de la Tarjeta de red",
                                  width = 38, 
                                  command = nombre_tarjeta_red, 
                                  bg = "#000", 
                                  fg = "#fff", 
                                  activebackground = "#1e1e1e", 
                                  activeforeground = "#00ffa4", 
                                  border = 0, 
                                  font = "JetBrainsMonoMedium 9").grid(row = 5, column = 1)

boton_escanear_tarjeta_red = Button(text = "Escanear Tarjeta de red",
                                    width = 38, 
                                    command = escanear_tarjeta_red, 
                                    bg = "#000", 
                                    fg = "#fff", 
                                    activebackground = "#1e1e1e", 
                                    activeforeground = "#00ffa4", 
                                    border = 0, 
                                    font = "JetBrainsMonoMedium 9").grid(row = 5, column = 2)

boton_comandos = Button(text = "Ejecutar Comandos Propios",
                        width = 38, 
                        command = bash, 
                        bg = "#000", 
                        fg = "#fff", 
                        activebackground = "#1e1e1e", 
                        activeforeground = "#00ffa4", 
                        border = 0, 
                        font = "JetBrainsMonoMedium 9").grid(row = 6, column = 0)

boton_ping = Button(text = "Ping",
                    width = 38, 
                    command = ping, 
                    bg = "#000",
                    fg = "#fff", 
                    activebackground = "#1e1e1e", 
                    activeforeground = "#00ffa4", 
                    border = 0, 
                    font = "JetBrainsMonoMedium 9").grid(row = 6, column = 1)

boton_monitor = Button(text = "Monitorear Red",
                       width = 38, 
                       command = network_top, 
                       bg = "#000", 
                       fg = "#fff", 
                       activebackground = "#1e1e1e", 
                       activeforeground = "#00ffa4", 
                       border = 0, 
                       font = "JetBrainsMonoMedium 9").grid(row = 6, column = 2)

boton_info_detallada = Button(text = "Info detallada del dispositivo",
                              width = 38, 
                              command = info_detallada, 
                              bg = "#000", 
                              fg = "#fff", 
                              activebackground = "#1e1e1e", 
                              activeforeground = "#00ffa4", 
                              border = 0, 
                              font = "JetBrainsMonoMedium 9").grid(row = 7, column = 0)

boton_test = Button(text = "Test de Velocidad",
                    width = 38, 
                    command = fast, 
                    bg = "#000", 
                    fg = "#fff", 
                    activebackground = "#1e1e1e", 
                    activeforeground = "#00ffa4", 
                    border = 0, 
                    font = "JetBrainsMonoMedium 9").grid(row = 7, column = 1)

boton_net_checker = Button(text = "Net_Checker(test de velocidad infinito)",
                           width = 38, 
                           command = net_checker, 
                           bg = "#000", 
                           fg = "#fff", 
                           activebackground = "#1e1e1e", 
                           activeforeground = "#00ffa4", 
                           border = 0, 
                           font = "JetBrainsMonoMedium 9").grid(row = 7, column = 2)

root.mainloop()
