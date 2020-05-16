from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    if player.lower() == ai.lower():
        return 'Empate!'

    if player.lower() == "tijeras" and ai.lower() == "papel":
        return 'Ganaste!'
    elif player.lower() == "tijeras" and ai.lower() == "piedra":
        return 'Perdiste!'

    if player == 'Papel' and ai == 'Piedra':
        return 'Ganaste!'
    elif player == 'Papel' and ai == 'Tijeras':
        return 'Perdiste!'

    if player == 'Piedra' and ai == 'Tijeras':
        return 'Ganaste!'
    elif player.capitalize() == 'Piedra' and ai.capitalize() == 'Papel':
        return 'Perdiste!'

# Entry Point
def Game():
    #le damos a la maquina un numero aleatorio entre 0 y 2 para saber que opción elige
    aleatorio = randint(0, 2)
    ai = options[aleatorio]
    
    # Ahora le damos la opción al usuario o player para elegir opción
    player = input("elige piedra, papel o tijeras: ")
        
    # 
    #

    winner = quienGana(player, ai)

    print(winner)