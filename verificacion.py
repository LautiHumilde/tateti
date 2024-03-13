def ganador(jugadorQempieza,nombre1,nombre2,jugador1,jugador2,tateti):
  if jugadorQempieza == nombre1:
    jugadorQempieza = nombre2
  else:
    jugadorQempieza = nombre1

  if jugadorQempieza == nombre1 and jugador1 == "X":
#horizontal
    if tateti[0] == ["X","X","X"]:
      return True
    if tateti[1] == ["X","X","X"]:
      return True
    if tateti[2] == ["X","X","X"]:
      return True
#vertical
    if tateti[0][0] == "X":
      if tateti[1][0] == "X":
        if tateti[2][0] == "X":
          return True
    if tateti[0][1] == "X":
      if tateti[1][1] == "X":
        if tateti[2][1] == "X":
          return True
    if tateti[0][2] == "X":
      if tateti[1][2] == "X":
        if tateti[2][2] == "X":
          return True
#diagonal
    if tateti[0][0] == "X":
      if tateti[1][1] == "X":
        if tateti[2][2] == "X":
          return True
    if tateti[2][0] == "X":
      if tateti[1][1] == "X":
        if tateti[0][2] == "X":
          return True
  if jugadorQempieza == nombre1 and jugador1 == "O":
#horizontal
    if tateti[0] == ["O","O","O"]:
      return True
    if tateti[1] == ["O","O","O"]:
      return True
    if tateti[2] == ["O","O","O"]:
      return True
#vertical
    if tateti[0][0] == "O":
      if tateti[1][0] == "O":
        if tateti[2][0] == "O":
          return True
    if tateti[0][1] == "O":
      if tateti[1][1] == "O":
        if tateti[2][1] == "O":
          return True
    if tateti[0][2] == "O":
      if tateti[1][2] == "O":
        if tateti[2][2] == "O":
          return True
#diagonal
    if tateti[0][0] == "O":
      if tateti[1][1] == "O":
        if tateti[2][2] == "O":
          return True
    if tateti[2][0] == "O":
      if tateti[1][1] == "O":
        if tateti[0][2] == "O":
          return True

  if jugadorQempieza == nombre2 and jugador2 == "X":
#horizontal
    if tateti[0] == ["X","X","X"]:
      return True
    if tateti[1] == ["X","X","X"]:
      return True
    if tateti[2] == ["X","X","X"]:
      return True
#vertical
    if tateti[0][0] == "X":
      if tateti[1][0] == "X":
        if tateti[2][0] == "X":
          return True
    if tateti[0][1] == "X":
      if tateti[1][1] == "X":
        if tateti[2][1] == "X":
          return True
    if tateti[0][2] == "X":
      if tateti[1][2] == "X":
        if tateti[2][2] == "X":
          return True
#diagonal
    if tateti[0][0] == "X":
      if tateti[1][1] == "X":
        if tateti[2][2] == "X":
          return True
    if tateti[2][0] == "X":
      if tateti[1][1] == "X":
        if tateti[0][2] == "X":
          return True
  if jugadorQempieza == nombre2 and jugador2 == "O":
#horizontal
    if tateti[0] == ["O","O","O"]:
      return True
    if tateti[1] == ["O","O","O"]:
      return True
    if tateti[2] == ["O","O","O"]:
      return True
#vertical
    if tateti[0][0] == "O":
      if tateti[1][0] == "O":
        if tateti[2][0] == "O":
          return True
    if tateti[0][1] == "O":
      if tateti[1][1] == "O":
        if tateti[2][1] == "O":
          return True
    if tateti[0][2] == "O":
      if tateti[1][2] == "O":
        if tateti[2][2] == "O":
          return True
#diagonal
    if tateti[0][0] == "O":
      if tateti[1][1] == "O":
        if tateti[2][2] == "O":
          return True
    if tateti[2][0] == "O":
      if tateti[1][1] == "O":
        if tateti[0][2] == "O":
          return True
  else:
    return False
