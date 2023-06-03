from code_connector import (dashboard_table, is_full, is_field_empty, player1_input,
                            player2_input, append_elements, display_table)
import numpy as np
def ai_evaluation():
    for length in range(len(dashboard_table)):
        if sum(dashboard_table[length]) == 3:
            return 1
        if sum(dashboard_table[length]) == -3:
            return -1
    for column in zip(*dashboard_table):
        if sum(column) == 3:
            return 1
        if sum(column) == -3:
            return -1
    diagonal_sum = np.asarray(dashboard_table)
    diagonal_sum = np.fliplr(diagonal_sum)
    if np.trace(diagonal_sum) == 3:
        return 1
    if np.trace(diagonal_sum) == -3:
        return -1
    diagonal_sum_reversed = np.asarray(dashboard_table[::-1])
    diagonal_sum_reversed = np.fliplr(diagonal_sum_reversed)
    if np.trace(diagonal_sum_reversed) == 3:
        return 1
    if np.trace(diagonal_sum_reversed) == -3:
        return -1
    if is_full():
        return 0
    return None

def minimax(depth, isMax):
    score = ai_evaluation()
    if score == 1:
        return score, None, None
    if score == -1:
        return score, None, None
    if score == 0:
        return score, None, None
    if isMax:
        best_input = float("-inf")
        best_x1 = None
        best_x2 = None

        for data in range(len(dashboard_table)):
            for insert_data in range(len(dashboard_table[data])):
                if is_field_empty(data, insert_data):
                    dashboard_table[data][insert_data] = player1_input
                    action, _, _ = minimax(depth + 1, False)
                    dashboard_table[data][insert_data] = 0
                    if action > best_input:
                        best_input = action
                        best_x1 = data
                        best_x2 = insert_data
            
        return best_input, best_x1, best_x2
    else:
        best_input = float("inf")
        best_x1 = None
        best_x2 = None

        for data in range(len(dashboard_table)):
            for insert_data in range(len(dashboard_table[data])):
                if is_field_empty(data, insert_data):
                    dashboard_table[data][insert_data] = player2_input
                    action, _, _ = minimax(depth + 1, True)
                    dashboard_table[data][insert_data] = 0
                    if action < best_input:
                        best_input = action
                        best_x1 = data
                        best_x2 = insert_data
        return best_input, best_x1, best_x2

def game_procces():
    while True:
        if is_full() == True:
            break
        while True:
            input_user1 = input("User1:")
            x1, x2 = map(int, input_user1.split())
            if is_field_empty(x1, x2) == True:
                append_elements(x1, x2, player1_input)
                break
            else:
                print("The field is not empty")
        display_table()
        if ai_evaluation() == 1 or ai_evaluation() == -1:
            break    
        print("Next user turn")
        while True:
            _, x1, x2 = minimax(0, True)
            try:
                if is_field_empty(x1, x2) == True:
                    append_elements(x1, x2, player2_input)
                    break
                else:
                    print("The field is not empty")
            except TypeError:
                break
        display_table()
        if ai_evaluation() == 1 or ai_evaluation() == -1:
            break           
        print("Next user turn")
        
