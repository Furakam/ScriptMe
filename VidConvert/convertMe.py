from os import system as command
from colorama import init,Fore,Style
from os import listdir,path
from time import sleep
from metodos import *
from mecanografiar import mecanografiar#('color','mensaje','numero de lineas')

#Limpiando pantalla
command('clear')
#Validando archivo de configuracion
path_script= path.split(__file__)#Divide la ruta del archivo Separando la carpeta del archivo
#Metodo para comprobar la configuracion y obtener valores
mecanografiar('yellow','Iniciando...',1)
sleep(.5)
def comprobarConfiguracion():

  if ".convertmeConf" in listdir(path_script[0]):
    f=open(path_script[0]+'/.convertmeConf','r')
    datosConfig= f.read().splitlines()
    #Obteniendo las rutas del archivo de configuracion
    ffmpegRute=datosConfig[1].replace('ffmpegRute="',"")
    ffmpegRute=ffmpegRute.replace('"',"")

    directorio_destino=datosConfig[2].replace("directorio_destino=","")
    directorio_destino=directorio_destino.replace('"',"")
    #---------------------------------------------------
    return directorio_destino,ffmpegRute
  else:
    mecanografiar('red',"Archivo de configuracion no encontrado.",0)
    mecanografiar('blue','Se procedera a crear un archivo predeterminado.',1)
    f=open(path_script[0]+'/.convertmeConf','w')
    f.write('#Recuerda que el orden de las variables es obligatorio.\n')
    f.write('ffmpegRute="/el/directorio/ffmpeg"\n')
    f.write('directorio_destino="/tu/directorio/destino"')


listaRutas=comprobarConfiguracion()
menu(listaRutas[0],listaRutas[1])
input(Fore.WHITE)

cambiandoRuta_destino()

listaRutas=comprobarConfiguracion()
menu(listaRutas[0],listaRutas[1])
input(Fore.WHITE)
