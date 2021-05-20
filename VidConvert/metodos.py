from os import system as command
from colorama import init,Fore,Style
from os import listdir,path, getcwd
from time import sleep
from mecanografiar import mecanografiar
from tkinter import Tk
from tkinter import filedialog

root=Tk()
root.wm_withdraw()
path_script= path.split(__file__)#Divide la ruta del archivo Separando la carpeta del archivo

def encabezado():
  command('clear')
  mecanografiar('cyan', 'ConvertMe - Si convertirte quieres, usarme debes', 0)
  mecanografiar('blue', '------------------------------------------------', 1)

def menu(carpeta_destino,ffmpegRute):

  encabezado()

  mecanografiar('green', '  |Opciones|','none')
  mecanografiar('yellow', 'Ingrese ', 'none') 
  mecanografiar('red', '"exit"', 'none') 
  mecanografiar('yellow',' para salir','none')
  mecanografiar('green', '|',0)
  mecanografiar('green', '  |', 0)

  mecanografiar('green', '==|={', 'none')
  mecanografiar('blue', 'Carpeta destino: ', 'none')
  mecanografiar('purple', carpeta_destino, 0)

  mecanografiar('green', '==|={','none')
  mecanografiar('blue', 'ffmpeg ubicado en: ', 'none')
  mecanografiar('purple', ffmpegRute, 0)
  mecanografiar('green', '  |', 0)

  mecanografiar('green', '==|==(', 'none')
  mecanografiar('blue','1-','none')
  mecanografiar('white',' Convertir formato de video y su audio.',0)

  mecanografiar('green', '==|==(', 'none')
  mecanografiar('blue','2-','none')
  mecanografiar('white',' Extraer fotogramas de un video.',0)

  mecanografiar('green', '==|==(', 'none')
  mecanografiar('blue','3-','none')
  mecanografiar('white',' Extraer frangmento de un video.',0)
  
  mecanografiar('green', '==|==(', 'none')
  mecanografiar('blue','4-','none')
  mecanografiar('white',' Cambiar carpeta de destino.',0)
  
  mecanografiar('green', '==|==(', 'none')
  mecanografiar('blue','5-','none')
  mecanografiar('white',' Cambiar carpeta de ffmpeg',0)

  mecanografiar('green', '==|===============================================>', 0)
  mecanografiar('green', '=====>> ', 'none')

def cambiandoRuta_ffmpeg():
  newPath=filedialog.askdirectory(initialdir=getcwd(),title='I Feel your PATH')
  if str(newPath) != '()':
    cambioConfig=open(path_script[0]+'/.convertmeConf','r').read().splitlines()
    newConf='ffmpegRute="'+newPath+'"'
    cambioConfig.pop(1)
    cambioConfig.insert(1,newConf)
    f= open(path_script[0]+'/.convertmeConf','w')
    f.writelines("\n".join(cambioConfig))

def cambiandoRuta_destino():
  newPath=filedialog.askdirectory(initialdir=getcwd(),title='I Feel your PATH')
  print(newPath)
  if str(newPath) != '()':
    print('Entrooooo!!!')
    cambioConfig=open(path_script[0]+'/.convertmeConf','r').read().splitlines()
    newConf='directorio_destino="'+newPath+'"'
    cambioConfig.pop(2)
    cambioConfig.insert(2,newConf)
    f= open(path_script[0]+'/.convertmeConf','w')
    f.writelines("\n".join(cambioConfig))

def convertirVideos(opcion):
  command('clear')
  mecanografiar('green', 'CONVIERTE TU VIDEO 100% REAL NO FAKE LIBRE DE VIRUS', 2)


