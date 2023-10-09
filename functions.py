import numpy as np
import time
from variables import SIZE_TABLERO, player_shots_hist, machine_shots_hist
from variables import CADETE, TENIENTE, COMANDANTE, CAPITAN, ALMIRANTE
from variables import rango_militar, player, shots, aciertos, players_win
from variables import lista_barcos_PLA, lista_barcos_MAC


def initialize_board():
    """
    Inicializa un tablero de 10x10 con espacios en blanco (' ').
    """
    return np.full(SIZE_TABLERO, '.')

TABLERO = initialize_board()
TABLERO_MAQUINA = initialize_board()
TABLERO_OCULTO = initialize_board()

# Función para poner los barcos de manera manual
def barco_manual(lista_barcos_MAC:list, lista_barcos_PLA:list):

    # Colocamos los barcos de la máquina MODO PRUEBA
    for barco in lista_barcos_MAC:
        for coord in barco:
            TABLERO_MAQUINA[coord] = "O"    

    # Colocamos los barcos del player
    for barco in lista_barcos_PLA:
        for coord in barco:
            TABLERO[coord] = "O"


def welcome_player():
    time.sleep(.25)
    print("\nBienvenido/a a la US Navy!\n")
    time.sleep(.35)
    player = input("Introduzca su apellido soldado/a: ")
    print()
    
    rango_militar, level = choose_level()

    # Nivel 1 de difcultad CADETE     == 1
    if level == CADETE:
        time.sleep(.5)
        print(f"Veo que es usted nuevo en la marina, {rango_militar} {player}, \nespero que este listo para la batalla!!\n")
    
    # Nivel 2 de difcultad TENIENTE   == 2
    elif level == TENIENTE:
        time.sleep(.5)
        print(f"Buenas, {rango_militar} {player}, le estabamos esperando. \nEl enemigo se encuentra a 10 millas, y acercandose.\n")

    # Nivel 3 de difcultad COMANDANTE == 3
    elif level == COMANDANTE:
        time.sleep(.5)
        print(f"{rango_militar} {player}, le estabamos esperando. \nEstamos en posición de combate!\n")

    # Nivel 4 de difcultad CAPITAN    == 4
    elif level == CAPITAN:
        time.sleep(.5)
        print(f"Estamos listos para el combate {rango_militar} {player}, \nEsperamos sus ordenes, mi {rango_militar}!\n")
                                        
    # Nivel 5 de difcultad ALMIRANTE  == 5
    elif level == ALMIRANTE:
        time.sleep(.5)
        print(f"Oh! Disculpe, no le había reconocido {rango_militar} {player}. \nBarcos en posición y listos para el combate señor/a!\n")
    
    return player, rango_militar, level


def get_info_player(player, rango_militar):
    player = player
    rango_militar = rango_militar
    return player, rango_militar


def choose_level():

    time.sleep(.3)
    print("Escoja el nivel de dificultad que desea jugar.\n")
    time.sleep(.2)
    print("NIVELES DEL JUEGO\n\
------------------------------------------------------------------------------\n\
1 = Nivel CADETE      ->   Jugador/a 1 disparo vs. Maquina 1 disparo\n\
2 = Nivel TENIENTE    ->   Jugador/a 1 disparo vs. Maquina 2 disparos seguidos\n\
3 = Nivel COMANDANTE  ->   Jugador/a 1 disparo vs. Maquina 3 disparos seguidos\n\
4 = Nivel CAPITÁN     ->   Jugador/a 1 disparo vs. Maquina 4 disparos seguidos\n\
5 = Nivel ALMIRANTE   ->   Jugador/a 1 disparo vs. Maquina 5 disparos seguidos\n\
------------------------------------------------------------------------------")

    time.sleep(.15)    
    level = int(input("Introduzca un número del 1 al 5: "))
    print()

    # Nivel 1 de difcultad CADETE     == 1
    if level == CADETE:
        rango_militar = "Cadete"
        return rango_militar, level
    
    # Nivel 2 de difcultad TENIENTE   == 2
    elif level == TENIENTE:
        rango_militar = "Teniente"
        return rango_militar, level

    # Nivel 3 de difcultad COMANDANTE == 3
    elif level == COMANDANTE:
        rango_militar = "Comandante"
        return rango_militar, level

    # Nivel 4 de difcultad CAPITAN    == 4
    elif level == CAPITAN:
        rango_militar = "Capitán"
        return rango_militar, level

    # Nivel 5 de difcultad ALMIRANTE  == 5
    elif level == ALMIRANTE:
        rango_militar = "Almirante"
        return rango_militar, level
    

def cuanta_municion(shots):
    shots = shots
    print(f"Nos quedan {shots} disparos de munición {rango_militar}.\n")


def shoot2machine():
    global player
    global rango_militar
    time.sleep(1)
    print(f"TURNO DEL {rango_militar.upper()} {player.upper()}:")

    # Pedimos coordenadas de disparo x e y al jugador/a
    time.sleep(.15)
    coord_x = int(input("Introduzca coordenada x: "))
    time.sleep(.15)
    coord_y = int(input("Introduzca coordenada y: "))
    print()
    
    global shots
    shots -= 1

    player_shots_hist.append((coord_x, coord_y))

    global aciertos

    if TABLERO_MAQUINA[coord_x, coord_y] == "O":
        TABLERO_MAQUINA[coord_x, coord_y] = "X"
        TABLERO_OCULTO[coord_x, coord_y] = "X"
        print("LES HEMOS TOCADO!!!")
        aciertos += 1
        time.sleep(.2)
        print(f"Hemos dado a un barco enemigo, {rango_militar} {player}!!!")
        time.sleep(.2)
        cuanta_municion(shots)
        time.sleep(.5)
        print(TABLERO_OCULTO)
        print()
    
    elif TABLERO_MAQUINA[coord_x, coord_y] == " ":
        TABLERO_MAQUINA[coord_x, coord_y] = "-"
        TABLERO_OCULTO[coord_x, coord_y] = "-"
        time.sleep(.2)
        print(f"Hemos fallado, {rango_militar}!!.")
        time.sleep(.2)
        cuanta_municion(shots)
        time.sleep(.5)
        print(TABLERO_OCULTO)
        print()
    
    elif TABLERO_MAQUINA[coord_x, coord_y] == "X":
        time.sleep(.2)
        print(f"Ya hemos disparado previamente a esas coordenadas, {rango_militar} {player}, y hemos dado a un barco.")
        time.sleep(.2)
        cuanta_municion(shots)
        time.sleep(.5)
        print(TABLERO_OCULTO)
        print()

    elif TABLERO_MAQUINA[coord_x, coord_y] == "-":
        time.sleep(.2)
        print(f"Ya hemos disparado previamente a esas coordenadas y solo había agua, {rango_militar}.")
        time.sleep(.2)
        cuanta_municion(shots)
        time.sleep(.5)
        print(TABLERO_OCULTO)
        print()
        
    if aciertos == 20:
        aciertos_final = True
    else:
        aciertos_final = False

    return shots, aciertos_final


def shoot2player():

    time.sleep(1)
    print(f"TURNO DEL ENEMIGO:")
    time.sleep(.3)
    coord_x = np.random.randint(0, 10)
    coord_y = np.random.randint(0, 10)

    machine_shots_hist.append((coord_x, coord_y))

    if TABLERO[coord_x, coord_y] == "O":
        TABLERO[coord_x, coord_y] = "X"
        print("TOCADOS!!!")
        time.sleep(.2)
        print(f"Nos han dado, {rango_militar} {player}!!!\n")
        time.sleep(.5)
        print(TABLERO)
        print()

    elif TABLERO[coord_x, coord_y] == " ":
        TABLERO[coord_x, coord_y] = "-"
        time.sleep(.2)
        print(f"No nos han dado, {rango_militar}!\n")
        time.sleep(.5)
        print(TABLERO)
        print()

    elif TABLERO[coord_x, coord_y] == "X":
        time.sleep(.2)
        print(f"Disparo previamente realizado por la máquina, {rango_militar}.\n")
        time.sleep(.5)
        print(TABLERO)
        print()

    elif TABLERO[coord_x, coord_y] == "-":
        time.sleep(.2)
        print(f"Disparo previamente realizado por la máquina, {rango_militar}.\n")
        time.sleep(.5)
        print(TABLERO)
        print()


aciertos = 0

player, rango_militar, level = welcome_player()

shots = 30

aciertos_final = False


def jugar():

    # Colocamos los barcos de manera manual
    barco_manual(lista_barcos_PLA, lista_barcos_MAC)

    while True:
  
        # Turno de disparo del/a player
        shots, aciertos_final = shoot2machine()

        if aciertos_final == True:
            time.sleep(.5)
            print(f"HEMOS GANADO LA BATALLA {rango_militar.upper()} {player.upper()}!!!!!")
            time.sleep(.5)
            print()
            print("Fin del juego")
            print()
            break

        elif shots == 0:
            print(f"Maldita sea! Nos hemos quedado sin munición, {rango_militar} {player}!!")
            time.sleep(.35)
            print()
            print("RETIRADAAAAA!!!")
            time.sleep(.5)
            print()
            print("Fin del juego")
            print()
            break

        elif players_win == True:
            print(f"Hemos ganado la batalla, {rango_militar} {player}!!!!!")
            break
        
        shoot2player()
