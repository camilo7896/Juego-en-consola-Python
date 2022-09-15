from ast import If
from concurrent.futures.process import _chain_from_iterable_of_lists
import os
import time

valor1=0

print("Bienvenido... ")
time.sleep(1.5)
#Pregunta nombre.
nombre=input("Como te llamas ? \n")
time.sleep(1.6)
print("Hola "+ nombre+ " tu mision sera encontrar el tesoro perdido.")
time.sleep(1.5)
print("Iniciemos...")
time.sleep(1.5)

os.system('cls')
time.sleep(3)
#************************* INICIO DE DECICIONES  ****************************

#*********** CONDICION 1 DERECHA O IZQUIERDA --> 
print("Por donde deseas iniciar? ")
time.sleep(1.5)
valor=int(input("\n1: Derecha \n2: Izquierda \n"))

#*********** CONDICION 2 NADAR O ESPERAR *******************************-->
if valor == 2:
 valor=int(input(" \n 1: Nadar \n 2: esperar \n ")) #pregunta
 time.sleep(1.5)
elif valor == 1:
 print("Atacado por canivales \n GAME OVER")

#*********** CONDICION 3 ELIGE COLOR DE PUERTA  *************************-->

if valor == 2:
  valor=int(input("\n Cual puerta  \n 1: Azul \n 2: Amarillo \n")) #pregunta
  time.sleep(1.5)
elif valor == 1:
  print("Devorado por un leon")

#*********** CONDICION 4 PUENTE O RIO ********************************-->
if valor == 2:
  valor=int(input("\n Pasar por  \n 1: Puente \n 2: Rio \n")) #pregunta
  time.sleep(1.5)
if valor == 1:
  print("Has encontrado el Tesoro")
elif valor == 2:
  print("Devorado por cocodrilos")



