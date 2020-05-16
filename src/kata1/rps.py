from random import randint

options = ["Piedra", "Papel", "Tijeras"]
EMPATE = "Empate!"
GANASTE = "Ganaste!"
PERDISTE = "Perdiste!"
win_dict = {
    "piedra": "tijeras",
    "papel": "piedra",
    "tijeras": "papel",
    }

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    if player == ai:
        result = EMPATE
    elif win_dict[player] == ai:
        result = GANASTE
    else:
        result = PERDISTE
    return result

# Entry Point
def Game():
    #
    #
    
    #
    #
    # Get player's chose
    answer = input("Insertar el numero del opcion, Piedra[0], Papel[1], Tijeras[2]: ")
    answer = int(answer)
    player = options[answer]

    ai = options[randint(0,2)]

    print("AI ha seleccionado " + ai)
    winner = quienGana(player, ai)

    print(winner)

if __name__ == "__main__":
    Game()

