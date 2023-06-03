from code_connector import (is_full, is_field_empty, append_elements, 
                            player1_input, display_table, win_combo, player2_input)
import random 
def game_procces_weak_ai():
    while True:
        if is_full() == True:
            break
        while True:
            input_user1 = input("User:")
            x1, x2 = map(int, input_user1.split())
            if is_field_empty(x1, x2) == True:
                append_elements(x1, x2, player1_input)
                break
            else:
                print("The field is not empty")
        display_table()
        if win_combo() == True:
            break    
        print("Next AI turn")
        while True:
            x1 = random.randint(0, 2)
            x2 = random.randint(0, 2)
            if is_field_empty(x1, x2) == True:
                append_elements(x1, x2, player2_input)
                break
        display_table()
        if win_combo() == True:
            break           
        print("Next user turn")
        
