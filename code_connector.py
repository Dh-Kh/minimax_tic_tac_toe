import numpy as np
dashboard_table = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]

player1_input = 1
player2_input = -1

def display_table():    
    symbol_map = {0: " ", player1_input: "X", player2_input: "O"}

    for row in dashboard_table:
        print(" %c | %c | %c " % (symbol_map[row[0]], symbol_map[row[1]], symbol_map[row[2]]))
        print("___|___|___")
    
def is_full():
    for length in range(len(dashboard_table)):
        for data in dashboard_table[length]:
            if data == 0:
                return False
    return True
        
def is_field_empty(x1, x2):
    if dashboard_table[x1][x2] == 0:
        return True
    else:
        return False
    
def append_elements(x1, x2, player):
    dashboard_table[x1][x2] = player

def win_combo():
    for length in range(len(dashboard_table)):
        if sum(dashboard_table[length]) == 3 or sum(dashboard_table[length]) == -3:
            return True
    for column in zip(*dashboard_table):
        if sum(column) == 3 or sum(column) == -3:
            return True
    diagonal_sum = np.asarray(dashboard_table)
    diagonal_sum = np.fliplr(diagonal_sum)
    if np.trace(diagonal_sum) == 3 or np.trace(diagonal_sum) == -3:
        return True
    diagonal_sum_reversed = np.asarray(dashboard_table[::-1])
    diagonal_sum_reversed = np.fliplr(diagonal_sum_reversed)
    if np.trace(diagonal_sum_reversed) == 3 or np.trace(diagonal_sum_reversed) == -3:
        return True
    return False