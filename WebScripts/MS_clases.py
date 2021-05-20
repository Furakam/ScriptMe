#!/usr/bin/python3

from os import system as comando
from os import popen ,getcwd,listdir
from time import sleep
from colorama import Fore,Style,init

init() #Inicializando colorama

def file_path():#Obtenemos la ruta de directorio del script
  get_directory_script=  __file__

  path_script=get_directory_script.split("/")
  conca_path=''
  for e in range(1,len(path_script) - 1):
    conca_path=conca_path+'/'+path_script[e]
  return conca_path

def comprobacion_archivos():
  lista_archivos=listdir(file_path())
  ruta_config=file_path()+'/config.txt'
  if 'config.txt' in lista_archivos:
    print('archivo de configuracion encontrado...')
  else:
    print(Fore.RED+Style.DIM+'config.txt no encontrado'+Fore.RESET)
    print('creando archivo de configuracion...')
    f=open(ruta_config,'w')
    configuration_content='apache_config: /etc/apache2/sites-available/000-default.conf\nbrowser: your-browser\napache_server_folder: /your/path/folder\n\n\nFuranku no Sapache - Recuerda modificar la configuracion'
    f.write(configuration_content)
    print('archivo creado...')
    sleep(2)

def config_path():#Leemos el archivo de configuracion del script
  ruta_config=file_path()+'/config.txt'
  with open(ruta_config) as apache_config:
    config_path=apache_config.readlines()[0]
    config_path_split=config_path.split(' ')
    config_path=config_path_split[1]
  return config_path

def apache_function(respuesta):
  if respuesta == 1:
    comando('clear')
    print(Fore.WHITE + Style.RESET_ALL+'\n')
    comando('sudo systemctl start apache2')
  elif respuesta == 2:
    comando('clear')
    print(Fore.WHITE + Style.RESET_ALL+'\n')
    comando('sudo systemctl stop apache2')
  elif respuesta == 3:
    comando('clear')
    print(Fore.WHITE + Style.RESET_ALL+'\n')
    
    print(Fore.BLUE + Style.BRIGHT+'\n  Recuerda cambiar la ruta en ambos archivos')
    sleep(2)
    path = config_path()
    comand_path='sudo nvim '+ path 
    comando(comand_path)
    comand_config='nvim '+file_path()+'/config.txt'
    comando(comand_config)

def mysql_function(respuesta):
  if respuesta == 1:
    comando('clear')
    print(Fore.WHITE + Style.RESET_ALL+'\n')
    comando('sudo systemctl start mysql')
  elif respuesta == 2:
    comando('clear')
    print(Fore.WHITE + Style.RESET_ALL+'\n')
    comando('sudo systemctl stop mysql')
  elif respuesta == 3:
    comando('clear')
    print(Fore.WHITE + Style.RESET_ALL+'\n')
    comando('brave-browser -new-window http://localhost/phpmyadmin/' + '> /dev/null 2>&1')

def browser_function(direccion):
  open_in_browser='brave-browser -new-window http://localhost/' + direccion + '> /dev/null 2>&1'
  #Con "> /dev/null 2>&1" ocultamos la salida del comando
  comando(open_in_browser)
