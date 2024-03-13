#importo random y la funcion ganador q esta en la file verificacion.py
import random
from verificacion import ganador

print("q onda rey , como andas")
print("vamos a jugar al tateti")
print("ingresa tu nombre o apodo")

nombre1 = input("nombre del jugador 1 : ")
nombre2 = input("nombre del jugador 2 : ")

jugador1 = input(f"bueno ahora el jugador " + nombre1 + " que quieres usar X o O : ")
#creo un maximo de 100 intentos para q ponga la ficha correcta
for romper in range(0,100):
  if jugador1 == "X" or jugador1 == "O":
    break
  else:
    print("porfavor ingresa X o O , o puede ser q lo pusiste en minuscula")
    jugador1 = input("ingresa nueva mente tu ficha : ")


jugador2 = "X"

if jugador1 == "X" :
  jugador2 = "O"
#aca creo una variable para el jugador q empieza aleatoriamente
jugadorQempieza = random.choice([nombre1, nombre2])
#base del tateti donde se guardan las fichas
tateti = [
  ["-","-","-"],
  ["-","-","-"],
  ["-","-","-"]
]

bool = False
#empieza el juego aca
for i in range(0,len(tateti)):
#llamo a la funcion ganador y le paso estos parametros
  if ganador(jugadorQempieza=jugadorQempieza,nombre1=nombre1,nombre2=nombre2,jugador1=jugador1,jugador2=jugador2,tateti=tateti):
    bool = True
    break
  else:
    bool = False
    for j in range(0,len(tateti)):
#hago lo mismo en el otro for por las dudas
      if ganador(jugadorQempieza=jugadorQempieza,nombre1=nombre1,nombre2=nombre2,jugador1=jugador1,jugador2=jugador2,tateti=tateti):
        bool = True
        break
      else:
        bool = False
#creo la ficha para cada jugador
      ficha1 = "nada"
      ficha2 = "nada"
#le asigno la ficha a cada jugador
      if jugadorQempieza == nombre1:
        ficha1 = jugador1

      if jugadorQempieza == nombre2:
        ficha2 = jugador2

      if jugadorQempieza == nombre1:
        print(f"empieza el jugador " + jugadorQempieza + " con la ficha " + ficha1)
      else:
        print(f"empieza el jugador " + jugadorQempieza + " con la ficha " + ficha2)
#aca le digo q ponga la pocicion en la que desea poner su ficha , y tambien hise un if para verificar si ya fila o el lugar esta ocupada por una ficha
      
      if bool == False:
        print("en que fila quieres poner tu ficha : ")
        fila = input()
        for romper in range(0,100):
          if fila == "0" or fila == "1" or fila == "2":
            fila = int(fila)
            if tateti[fila][0] != "X" or tateti[fila][1] != "X" or tateti[fila][2] != "X" or tateti[fila][0] != "O" or tateti[fila][1] != "O" or tateti[fila][2] != "O":
              break
            else:
              print("la fila esta completa ya")
              print("")
          else:
            print("la pocicion q ingresaste se pasa o no esta adentro del tateti/n porfavor ingresa una pocicion que este adentro")
            print("")
            print("ingresa la posicion : ")
            fila = input()
#y aca es en la columna
      if bool == False:
        print("y en que columna")
        columna = input()
        for romper in range(0,100):
          if columna == "0" or columna == "1" or columna == "2":
            columna = int(columna)
            if tateti[fila][columna] != "X" and tateti[fila][columna] != "O":
              break
            else:
              print("ya hay una ficha aca , ingresa nomas la posicion de columna")
              print("")
          else:
            print("la pocicion q ingresaste se pasa o no esta adentro del tateti/n porfavor ingresa una pocicion que este adentro")
            print("")
            print("ingresa la posicion : ")
            columna = input()

      fila = int(fila)
      columna = int(columna)
#aca inserto la ficha en el tateti
      if jugadorQempieza == nombre1:
        tateti[fila][columna] = ficha1
      else:
        tateti[fila][columna] = ficha2
#printeo el tateti
      print(f"" + tateti[0][0]+ " " + tateti[0][1] + " " +  tateti[0][2])
      print(f"" + tateti[1][0]+ " " + tateti[1][1] + " " +  tateti[1][2])
      print(f"" + tateti[2][0]+ " " + tateti[2][1] + " " +  tateti[2][2])
#cambio de jugador
      if jugadorQempieza == nombre1:
        jugadorQempieza = nombre2
      else:
        jugadorQempieza = nombre1
#cambio de jugador de nuevo para q gane el correcto
if jugadorQempieza == nombre1:
  jugadorQempieza = nombre2
else:
  jugadorQempieza = nombre1
#si gana gana y si empata empata
if bool == True:
    print(f"gano " + jugadorQempieza)
else:
    print("empate , buen juego")
