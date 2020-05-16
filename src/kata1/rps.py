from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    if player == ai:
        return "Empate!"
    if player == 'papel' and ai == "tijeras" or player == 'tijeras' and ai == 'piedra' or player == 'piedra' and ai == "papel":
        return 'Perdiste!'
    return 'Ganaste!'
     

# Entry Point
def Game():
    player = input('Introduce Piedra, Papel o Tijera: ')
    ai = options[randint(0 , 2)]

    
    winner = quienGana(player, ai)

    print(winner)
