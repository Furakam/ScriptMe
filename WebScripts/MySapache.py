#!/usr/bin/python3

from os import system as comando
from  os import  popen,getcwd,path
from getpass import getuser
#importando clases
import MS_clases,MS_menu
from colorama import Fore,Style,init

init()
comando('sudo echo "Ingresando contraseña"')
comando('clear')

MS_clases.comprobacion_archivos()

repeticion = True
while repeticion == True:
  comando('clear')
  MS_menu.menu_principal()
  try:
    respuesta = int(input())
  except:
    print(Fore.LIGHTRED_EX + Style.BRIGHT + '\n  ERROR: No puede ingresar un caracter...',end='')
    input('Presione ENTER')
    respuesta = 0
  if respuesta == 1:
    apache_repeat = True
    while apache_repeat == True:
      comando('clear')
      MS_menu.menu_apache()
      opcion = input()
      try:
        option=int(opcion)
        if option > 0 and option < 4:
          MS_clases.apache_function(option)
      except:
        if opcion == 'prev':
          apache_repeat = False
  if respuesta == 2:
    apache_repeat = True
    while apache_repeat == True:
      comando('clear')
      MS_menu.menu_mysql()
      opcion = input()
      try:
        option=int(opcion)
        if option > 0 and option < 4:
          MS_clases.mysql_function(option)
      except:
        if opcion == 'prev':
          apache_repeat = False
  if respuesta == 3:
    apache_repeat = True
    while apache_repeat == True:
      comando('clear')
      ruta = MS_clases.file_path()+'/config.txt'
      with open(ruta) as apache_config:
        browser=apache_config.readlines()[1]
        browser_split=browser.split(' ')
        browser=browser_split[1]
      with open(ruta) as apache_config:
        path=apache_config.readlines()[2]
        path_split=path.split(' ')
        path=path_split[1]
      MS_menu.menu_open_browser(path,browser)
      direccion = input()
      if direccion != 'prev':
        MS_clases.browser_function(direccion)
        apache_repeat=False
      else:
        apache_repeat=False
  elif respuesta == 4:
    repeticion = False

