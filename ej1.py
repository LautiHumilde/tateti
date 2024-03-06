import random

print("q onda rey , como andas")
print("vamos a jugar al tateti")
print("ingresa tu nombre o apodo")

nombre1 = input("nombre del jugador 1 : ")
nombre2 = input("nombre del jugador 2 : ")

jugador1 = input(f"bueno ahora el jugador " + nombre1 + " que quieres usar X o O : ")

for romper in range(0,100):
     if jugador1 == "X" or jugador1 == "O":
         break
     else:
        print("porfavor ingresa X o O , o puede ser q lo pusiste en minuscula")
        jugador1 = input("ingresa nueva mente tu ficha : ")


jugador2 = "X"

if jugador1 == "X" :
    jugador2 = "O"


jugadorQempieza = random.choice([nombre1, nombre2])

print(f"empueza el jugador : " + jugadorQempieza)

tateti = [
    ["-","-","-"],
    ["-","-","_"],
    ["-","-","-"]
    ]

for i in range(0,len(tateti)):
    for j in range(0,len(tateti)):
            ficha = "nada"

            if jugadorQempieza == nombre1:
                 if jugador1 == "X":
                    if i+j % 2 == 0:
                        ficha = "X"
                    else:
                        ficha = "O"
                 else:
                    if jugador1 == "O":
                        if i+j % 2 == 0:
                            ficha = "O"
                    else:
                        ficha = "X"
            else:
                if jugadorQempieza == nombre2:
                    if jugador2 == "X":
                        if i+j % 2 == 0:
                            ficha = "X"
                    else:
                        ficha = "O"
                else:
                    if jugador2 == "O":
                        if i+j % 2 == 0:
                            ficha = "O"
                    else:
                        ficha = "X"
            
            print(f"empieza el jugador " + jugadorQempieza + "con la ficha " + ficha)

            print("en que fila quieres poner tu ficha : ")
            fila = input()

            for romper in range(0,100):
                 if fila == "0" or fila == "1" or fila == "2":
                      break
                 else:
                      print("la pocicion q ingresaste se pasa o no esta adentro del tateti/n porfavor ingresa una pocicion que este adentro")
                      fila = input("ingresa la posicion : ")

            print("y en que columna")
            columna = input()
            for romper in range(0,100):
                 if columna == "0" or columna == "1" or columna == "2":
                      break
                 else:
                      print("la pocicion q ingresaste se pasa o no esta adentro del tateti/n porfavor ingresa una pocicion que este adentro")
                      fila = input("ingresa la posicion")
            
            tateti[fila][columna].append(fila)

            print(f"" + tateti[0][0]+ " " + tateti[0][1] + " " +  tateti[0][2])
            print(f"" + tateti[1][0]+ " " + tateti[1][1] + " " +  tateti[1][2])
            print(f"" + tateti[2][0]+ " " + tateti[2][1] + " " +  tateti[2][2])
