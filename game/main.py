"""Este es un proyecto de piedra, papel o tijera, en donde el computador selecciona aleatoriamente una de las tres para competir"""
import random
round = 0

#El usuario debe ingresar el texto de piedra, papel o tijera para competir
print(
  "BIENVENIDO AL ESPECTACULAR Y ASOMBROSO JUEGO DE PIEDRA, PAPEL O TIJERA...HUMANO"
)


def opcion(round):

  print("*******************")
  print("**** ROUND #", round, "****")
  print("*******************")
  user = input(
    "Si te atreves, selecciona ¿piedra, papel o tijera?... humano: ")
  user = user.upper()
  return user


def juego(round):

  maquina = 0
  humano = 0

  while maquina | humano < 2:

    round += 1
    user = opcion(round)

    #Creamos la tupla
    computer = ("PIEDRA", "PAPEL", "TIJERA")
    eleccion = ("¡Hemos empatado esta mano humano!",
                "¡Papel le gana a piedra, has ganado esta mano humano!",
                "¡Piedra le gana a tijera, has perdido esta mano humano!",
                "¡Papel le gana a piedra, has perdido esta mano humano!",
                "¡Tijera le gana a papel, has ganado esta mano humano!",
                "¡Tijera le gana a papel, has perdido esta mano humano!",
                "¡Piedra le gana a tijera, has ganado esta mano humano!",
                "¡Ha ganado la computadora insignificante humano!",
                "¡Excelente trabajo, me has vencido!")

    #Le gestionamos a la computadora aleatoreamente la elección, numéricamente, de la opción de piedra, papel o tijera
    aleatorio = random.randint(1, 3)
    if aleatorio == 1:
      print("Computadora: " + computer[0])
      if user == computer[0]:
        print(eleccion[0])
      elif user == computer[1]:
        print(eleccion[1])
        humano += 1
      elif user == computer[2]:
        print(eleccion[2])
        maquina += 1
    elif aleatorio == 2:
      print("Computadora: " + computer[1])
      if user == computer[1]:
        print(eleccion[0])
      elif user == computer[0]:
        print(eleccion[3])
        maquina += 1
      elif user == computer[2]:
        print(eleccion[4])
        humano += 1
    else:
      print("Computadora: " + computer[2])
      if user == computer[2]:
        print(eleccion[0])
      elif user == computer[1]:
        print(eleccion[5])
        maquina += 1
      elif user == computer[0]:
        print(eleccion[6])
        humano += 1
    print("Computadora:", maquina, "Humano:", humano)
    print("    ")
    continue

  round += 1

  final_juego(maquina, eleccion)


def final_juego(maquina, eleccion):

  if maquina == 2:
    print(eleccion[7])
  else:
    print(eleccion[8])


juego(round)
