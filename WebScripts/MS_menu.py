#!/usr/bin/python3

from os import system as comando
from os import popen 
from time import sleep
from colorama import Fore,Style,init

#importando clases
import MS_clases

init()

def menu_principal():
  print(Fore.BLUE + Style.BRIGHT + '\n  ScriptMe / MySapache.py')
  print(Fore.GREEN + Style.BRIGHT + '  -----------------------')
  
  #SACAMOS INFORMACION SOBRE EL ESTADO DE APACHE
  print(Fore.CYAN + Style.BRIGHT + '\n  1)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' Apache Options',end='')
  print(Fore.CYAN + Style.BRIGHT + ' ('+Fore.YELLOW + Style.BRIGHT + 'Status: ',end='')
  
  ruta_log = MS_clases.file_path() + '/log.txt'
  command='sudo systemctl status apache2 > '+ruta_log
  comando(command)
  with open(ruta_log) as log:
    status_apache=log.readlines()[2]
    status_apache = status_apache.split(' ')
    if status_apache[6] == 'active':
      print(Fore.GREEN + Style.BRIGHT + '● ' +status_apache[6],end='')
    elif status_apache[6] == 'inactive':
      print(Fore.RED + Style.DIM + '● ' +status_apache[6],end='')
    else:
      print(Fore.RED + Style.DIM + 'Unknow')

  print(Fore.CYAN + Style.DIM + ')')
  #-----------------X----------------------
  #SACAMOS INFORMACION SOBRE EL ESTADO DE MYSQL
  print(Fore.CYAN + Style.BRIGHT + '\n  2)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' MySQL Options',end='')
  print(Fore.CYAN + Style.BRIGHT + ' ('+Fore.YELLOW + Style.BRIGHT + 'Status: ',end='')

  ruta_log = MS_clases.file_path() + '/log.txt'
  command='sudo systemctl status mysql > '+ruta_log
  comando(command)
  with open(ruta_log) as log:
    status_apache=log.readlines()[2]
    status_apache = status_apache.split(' ')
    if status_apache[6] == 'active':
      print(Fore.GREEN + Style.BRIGHT + '● ' +status_apache[6],end='')
    elif status_apache[6] == 'inactive':
      print(Fore.RED + Style.DIM + '● ' +status_apache[6],end='')
    else:
      print(Fore.RED + Style.DIM + 'Unknow')

  print(Fore.CYAN + Style.DIM + ')')
#-----------------X----------------------

  print(Fore.CYAN + Style.BRIGHT + '\n  3)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' OpenBrowser http//localhost.')

  print(Fore.CYAN + Style.BRIGHT + '\n  4)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' Exit.')

  print(Fore.GREEN + Style.BRIGHT + '\n  >> ',end="")

def menu_apache():
  print(Fore.BLUE + Style.BRIGHT + '\n  MySapache / Apache Options')
  print(Fore.GREEN + Style.BRIGHT + '  --------------------------')

  print(Fore.CYAN + Style.BRIGHT + '\n  1)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' Apache Start.')

  print(Fore.CYAN + Style.BRIGHT + '\n  2)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' Apache Stop.')

  print(Fore.CYAN + Style.BRIGHT + '\n  3)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' Cambiar directorio de locahost.')

  print(Fore.WHITE + Style.BRIGHT + '\n  >>Para retroceder ingrese prev')

  print(Fore.GREEN + Style.BRIGHT + '\n  >> ',end="")

def menu_mysql():
  print(Fore.BLUE + Style.BRIGHT + '\n  MySapache / MySQL Options')
  print(Fore.GREEN + Style.BRIGHT + '  --------------------------')

  print(Fore.CYAN + Style.BRIGHT + '\n  1)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' MySQL Start.')

  print(Fore.CYAN + Style.BRIGHT + '\n  2)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' MySQL Stop.')

  print(Fore.CYAN + Style.BRIGHT + '\n  3)',end='')
  print(Fore.WHITE + Style.BRIGHT + ' PhpMyadmin-Mysql')

  print(Fore.WHITE + Style.BRIGHT + '\n  >>Para retroceder ingrese prev')

  print(Fore.GREEN + Style.BRIGHT + '\n  >> ',end="")

def menu_open_browser(apacheFolderPath,browser):
  print(Fore.BLUE + Style.BRIGHT + '\n  MySapache / Open in Browser')
  print(Fore.GREEN + Style.BRIGHT + '  --------------------------')

  print(Fore.WHITE + Style.DIM + '  >>Para retroceder ingrese prev')

  comand = 'ls ' + apacheFolderPath
  read_comando = str(popen(comand).read())#pope().read() nos permite almacenar las salida del comando en una variable
  cut_comando=read_comando.split('\n')
  cantidad_elementos = len(cut_comando)
  ultimo_elemento = cantidad_elementos - 1#Obtenemos el numero del ultimo elemento
  cut_comando.pop(ultimo_elemento)#Eliminamos el ultimo elemento de la lista

  print(Fore.CYAN + Style.BRIGHT + f'\n  Carpetas de proyectos dentro de {apacheFolderPath}' + Fore.WHITE + Style.BRIGHT)

  for e in cut_comando:
    print(Fore.WHITE + Style.BRIGHT + '  - ' + e)

  print(Fore.CYAN + Style.BRIGHT + '\n  Complete la direccion:',end='')
  print(Fore.GREEN + Style.BRIGHT + f'\n\n\t{browser}',end="")
  print(Fore.YELLOW + Style.BRIGHT + '\n\n\t- http://localhost/',end="")
 

