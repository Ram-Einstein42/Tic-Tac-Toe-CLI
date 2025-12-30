import random
def board():
    return [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def display_board(board):
    for row in board:
        print(row)


 
def player_input():
    return int(input("Enter the number (1-9): "))

def place_marker(board, choice, marker):
    row = (choice - 1) // 3 # gets the row
    col = (choice - 1) % 3 # gets the col
    board[row][col] = marker

cpu_choice = random.randint(1,9)

 
 
 

game_board= board()
display_board(game_board)
choice = player_input()
place_marker(game_board, choice, "X") 
place_marker(game_board, cpu_choice, "O") 

print("\nUpdated Board:")
display_board(game_board)