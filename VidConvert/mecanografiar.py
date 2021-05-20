from sys import stdout
from time import sleep
from colorama import init,Fore,Style

init()
def mecanografiar(color,texto,lineas):
  #Dando colores a la salida con Colorama
  if color == "cyan":
    print(Fore.CYAN+Style.BRIGHT,end='')
  elif color == "red":
    print(Fore.RED+Style.BRIGHT,end='')
  elif color == "blue":
    print(Fore.BLUE+Style.BRIGHT,end='')
  elif color == "green":
    print(Fore.GREEN+Style.BRIGHT,end='')
  elif color == "yellow":
    print(Fore.YELLOW+Style.BRIGHT,end='')
  elif color == "white":
    print(Fore.WHITE+Style.BRIGHT,end='')
  #Aqui empieza la funcion demecanografiar
  li=[]
  num_caracteres=len(texto)
  for letra in range(0,num_caracteres):
    li.append(texto[letra])
  for palabra in li:
    stdout.write(palabra)
    stdout.flush()
    sleep(.015)

  if lineas == 'none':
    print("",end='')
  elif lineas == 0:
    print("")
  else:
    for l in range(0,lineas+1):
      print("")
