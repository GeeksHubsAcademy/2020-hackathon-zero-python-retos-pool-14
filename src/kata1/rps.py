from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    if player == "piedra" and ai == "piedra":
        return "Empate!"
    elif player == "papel" and ai == "papel":
        return "Empate!"
    elif player == "tijeras" and ai == "tijeras":
        return "Empate!"
    elif player == "piedra" and ai == "papel":
        return "Perdiste!"
    elif player == "papel" and ai == "tijeras":
        return "Perdiste!"
    elif player == "tijeras" and ai == "piedra":
        return "Perdiste!"
    elif player == "piedra" and ai == "tijeras":
        return "Ganaste!"
    elif player == "tijeras" and ai == "papel":
        return "Ganaste!"
    elif player == "papel" and ai == "piedra":
        return "Ganaste!"                            

# Entry Point
def Game():
    #
    #Consulta y asignación de la respuesta del jugador
    respuesta = False
    while respuesta == False:
        player = input("Piedra, papel o tijeras?")
        player = player.lower()
        if player == "piedra" or player == "papel" or player == "tijeras":
            respuesta = True
        else:
            print("Escriba bien tu respuesta: ")    

    #asignación de la respuesta de la ai
    respuestaIA = randint(0,2)
    if respuestaIA == 0:
        ai = "piedra"
    elif respuestaIA == 1:
        ai = "papel"
    else: 
        ai = "tijeras"    
    #
    winner = quienGana(player, ai)
    print("Has elegido: " + player)
    print("La AI ha elegido: " + ai)
    print(winner)

Game()