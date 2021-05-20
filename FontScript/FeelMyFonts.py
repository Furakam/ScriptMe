from subprocess import call as command
from subprocess import run
from time import sleep
from tkinter import Tk
from os import listdir
from tkinter import filedialog
from getpass import getuser
from colorama import Fore,Style,init

init()
root=Tk()
root.wm_withdraw()
run(['sudo','echo'])

error=Fore.RED+Style.BRIGHT
title=Fore.CYAN+Style.BRIGHT
subtitle=Fore.BLUE + Style.BRIGHT
defti=Fore.YELLOW+Style.BRIGHT
enun=Fore.WHITE+Style.BRIGHT
deco=Fore.GREEN+Style.BRIGHT

usuario=getuser()
carpetaActual= "/home/" + usuario



def menu():
  command('clear')
  print(Fore.CYAN+Style.DIM+"  Instalador de fuentes 'FeelMyFonts.py'")
  print(deco+"\n  1."+enun+"Seleccionar carpeta.")
  print(deco+"  2."+enun+"Instalar.")
  print(deco+"  3."+enun+"Salir.")
  print(defti+"\n  Carpeta actual: ", carpetaActual)
  
  lista_fuentes=[]
  if carpetaActual != "/home/"+usuario:
    print(deco+"\n  Fuentes encontradas:\n")
    for fuentes in listdir(carpetaActual):
      if fuentes.endswith(".ttf") or fuentes.endswith(".TTF") or fuentes.endswith(".otf"):
        lista_fuentes.append(fuentes)

  if len(lista_fuentes) != 0:
    for index in range(0,len(lista_fuentes)):
      print(subtitle+"    - ",lista_fuentes[index])
  else:
    print(error+"    -No se encontro las fuentes.")

bucle=True
while bucle == True:
  bucle_interno=True
  while bucle_interno == True:
    menu()
    try:
      opcion = int(input(deco+"\n  >> "+Fore.RESET))
      bucle_interno=False
    except:
      print(error+"\n  Debe ingresar un numero.")
      sleep(1)
  
  if opcion == 1:
    carpetaActual=filedialog.askdirectory()
    if str(carpetaActual) == '()':
      carpetaActual="/home/"+usuario

  elif opcion == 2:

   
    lista_fuentes=[]
    for fuentes in listdir(carpetaActual):
      if fuentes.endswith(".ttf") or fuentes.endswith(".TTF") or fuentes.endswith(".otf"):
        lista_fuentes.append(fuentes)
    lista_fuentes_cant=len(lista_fuentes)
    if lista_fuentes_cant != 0:
      print(deco+"\n    Ingrese el nombre general de la fuente: ",end='')
      name=input(enun+"")
      path_fonts="/usr/share/fonts/"+name+"/"
      run(['sudo','mkdir',path_fonts])
      for i in range(0, len(lista_fuentes)):
        path_file=carpetaActual+"/"+lista_fuentes[i]
        run(['sudo','cp',path_file,path_fonts])
    else:
      print(error+"\n    Sin fuentes no hay paraiso.")
      sleep(2)
  else:
    command('clear')
    break
