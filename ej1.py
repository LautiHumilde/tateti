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


tateti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
    ]

for i in range(0,len(tateti)):
    for j in range(0,len(tateti)):
            if jugadorQempieza == nombre1 and jugador1 == "X":

                #horizontal

                if tateti[0] == ["X","X","X"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break
            
                if tateti[1] == ["X","X","X"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break

                if tateti[2] == ["X","X","X"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break

                #vertical

                if tateti[0][0] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][0] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][0] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                if tateti[0][1] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][1] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break
                
                if tateti[0][2] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][2] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                #diagonal
                        
                if tateti[0][0] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break



                if tateti[0][0] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

            if jugadorQempieza == nombre1 and jugador1 == "O":
                
                #horizontal
                if tateti[0] == ["O","O","O"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break
            
                if tateti[1] == ["O","O","O"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break

                if tateti[2] == ["O","O","O"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break

                #vertical

                if tateti[0][0] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][0] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][0] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                if tateti[0][1] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][1] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                if tateti[0][2] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][2] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                #diagonal
                if tateti[0][0] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break



                if tateti[2][0] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][0] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break












            

            if jugadorQempieza == nombre2 and jugador2 == "X":

                #horizontal

                if tateti[0] == ["X","X","X"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break
            
                if tateti[1] == ["X","X","X"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break

                if tateti[2] == ["X","X","X"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break

                #vertical

                if tateti[0][0] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][0] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][0] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                if tateti[0][1] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][1] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break
                
                if tateti[0][2] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][2] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                #diagonal
                        
                if tateti[0][0] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break



                if tateti[0][0] == "X":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "X":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "X":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                







            if jugadorQempieza == nombre2 and jugador2 == "O":
                
                #horizontal
                if tateti[0] == ["O","O","O"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break
            
                if tateti[1] == ["O","O","O"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break

                if tateti[2] == ["O","O","O"]:
                    print(f"gano el jugador" + jugadorQempieza)
                    break

                #vertical

                if tateti[0][0] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][0] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][0] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                if tateti[0][1] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][1] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                if tateti[0][2] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][2] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break

                #diagonal
                if tateti[0][0] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][2] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break



                if tateti[2][0] == "O":
                     print(f"gano el jugador" + jugadorQempieza)
                     if tateti[1][1] == "O":
                        print(f"gano el jugador" + jugadorQempieza)
                        if tateti[2][0] == "O":
                            print(f"gano el jugador" + jugadorQempieza)
                            break









            ficha1 = "nada"
            ficha2 = "nada"

            if jugadorQempieza == nombre1:
                ficha1 = jugador1

            if jugadorQempieza == nombre2:
                ficha2 = jugador2

            
            if jugadorQempieza == nombre1:
                 print(f"empieza el jugador " + jugadorQempieza + " con la ficha " + ficha1)
            else:
                 print(f"empieza el jugador " + jugadorQempieza + " con la ficha " + ficha2)

            print("en que fila quieres poner tu ficha : ")
            fila = input()

            for romper in range(0,100):
                 if fila == "0" or fila == "1" or fila == "2":
                      break
                 else:
                      print("la pocicion q ingresaste se pasa o no esta adentro del tateti/n porfavor ingresa una pocicion que este adentro")
                      print("ingresa la posicion : ")
                      fila = input()

            print("y en que columna")
            columna = input()
            for romper in range(0,100):
                 if columna == "0" or columna == "1" or columna == "2":
                      break
                 else:
                      print("la pocicion q ingresaste se pasa o no esta adentro del tateti/n porfavor ingresa una pocicion que este adentro")
                      print("ingresa la posicion : ")
                      columna = input()
            
            fila = int(fila)
            columna = int(columna)


            if jugadorQempieza == nombre1:
                 tateti[fila][columna] = ficha1
            else:
                 tateti[fila][columna] = ficha2

            print(f"" + tateti[0][0]+ " " + tateti[0][1] + " " +  tateti[0][2])
            print(f"" + tateti[1][0]+ " " + tateti[1][1] + " " +  tateti[1][2])
            print(f"" + tateti[2][0]+ " " + tateti[2][1] + " " +  tateti[2][2])

            if jugadorQempieza == nombre1:
                jugadorQempieza = nombre2
            else:
                jugadorQempieza = nombre1



print(f"gano " + jugadorQempieza)
