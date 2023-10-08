import numpy as np

SIZE_TABLERO = (10, 10)



# Lista de históricos de las coordenadas de los disparos
player_shots_hist  = []
machine_shots_hist = []

rango_militar = ""
player = ""

# player = input("Introduce el nombre de jugador/a: ")

# Niveles de dificultad
CADETE     = 1
TENIENTE   = 2
COMANDANTE = 3
CAPITAN    = 4
ALMIRANTE  = 5

aciertos = 0

level = False

players_win = False

shots = 20

#############################################################
# Coordenadas (manuales) de barcos 
# Barcos de la máquina
# Barcos de eslora = 1
barco_MAC_1 = [(5,6)]
barco_MAC_2 = [(1,7)]
barco_MAC_3 = [(7,1)]
barco_MAC_4 = [(3,8)]

# Barcos de eslora = 2
barco_MAC_5 = [(3,4), (3,5)]
barco_MAC_6 = [(6,3), (6,4)]
barco_MAC_7 = [(8,3), (8,4)]

# Barcos de eslora = 3
barco_MAC_8 = [(3,1), (4,1), (5,1)]
barco_MAC_9 = [(7,6), (7,7), (7,8)]

# Barco de eslora = 4
barco_MAC_10 = [(1,1), (1,2), (1,3), (1,4)]

# Lista de coordenads de los barcos de la máquina
lista_barcos_MAC = [barco_MAC_1, barco_MAC_2, barco_MAC_3, barco_MAC_4,
                barco_MAC_5, barco_MAC_6, barco_MAC_7,
                barco_MAC_8, barco_MAC_9,
                barco_MAC_10]

# Barcos del player
# Barcos de eslora = 1
barco_PLA_1 = [(1,1)]
barco_PLA_2 = [(3,1)]
barco_PLA_3 = [(8,2)]
barco_PLA_4 = [(8,8)]

# Barcos de eslora = 2
barco_PLA_5 = [(1,3), (1,4)]
barco_PLA_6 = [(3,3), (3,4)]
barco_PLA_7 = [(5,1), (6,1)]

# Barcos de eslora = 3
barco_PLA_8 = [(3,8), (4,8), (5,8)]
barco_PLA_9 = [(6,4), (7,4), (8,4)]

# Barco de eslora = 4
barco_PLA_10 = [(4,6), (5,6), (6,6), (7,6)]

# Lista de coordenads de los barcos de la máquina
lista_barcos_PLA = [barco_PLA_1, barco_PLA_2, barco_PLA_3, barco_PLA_4,
                barco_PLA_5, barco_PLA_6, barco_PLA_7,
                barco_PLA_8, barco_PLA_9,
                barco_PLA_10]
