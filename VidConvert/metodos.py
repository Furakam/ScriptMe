from os import system as command
from colorama import init,Fore,Style
from os import listdir,path
from time import sleep
from mecanografiar import mecanografiar
from tkinter import Tk
from tkinter import filedialog

root=Tk()
root.wm_withdraw()

def encabezado():
  command('clear')
  mecanografiar('cyan', 'ConvertMe - Si convertirte quieres, usarme debes', 0)
  mecanografiar('blue', '------------------------------------------------', 1)

def menu():
  encabezado()

  mecanografiar('green', '  |Opciones|','none')
  mecanografiar('red', 'Ingrese "exit" para salir','none')
  mecanografiar('green', '|',2)

  mecanografiar('blue','  1-','none')
  mecanografiar('white',' Convertir formato de video y su audio.',0)

  mecanografiar('blue','  2-','none')
  mecanografiar('white',' Extraer fotogramas de un video.',0)

  mecanografiar('blue','  3-','none')
  mecanografiar('white',' Extraer frangmento de un video.',0)
  
  mecanografiar('blue','  4-','none')
  mecanografiar('white',' Cambiar carpeta de destino.',0)
  
  mecanografiar('blue','  5-','none')
  mecanografiar('white',' Cambiar carpeta de ffmpeg',2)

def cambiandoRuta_ffmpeg():
  newPath=filedialog.askdirectory()
  cambioConfig=open('.convertmeConf','r').read().splitlines()
  newConf='ffmpegRute="'+newPath+'"'
  cambioConfig.pop(1)
  cambioConfig.insert(1,newConf)
  f= open('.convertmeConf','w')
  f.writelines("\n".join(cambioConfig))

def cambiandoRuta_destino():
  newPath=filedialog.askdirectory()
  cambioConfig=open('.convertmeConf','r').read().splitlines()
  newConf='directorio_destino="'+newPath+'"'
  cambioConfig.pop(2)
  cambioConfig.insert(2,newConf)
  f= open('.convertmeConf','w')
  f.writelines("\n".join(cambioConfig))

def convertirVideos(opcion):
  command('clear')
  mecanografiar('green', 'CONVIERTE TU VIDEO 100% REAL NO FAKE LIBRE DE VIRUS', 2)
