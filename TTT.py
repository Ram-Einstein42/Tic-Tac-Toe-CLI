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
    return int(input("Enter a number (1-9): "))

def place_marker(board, choice, marker):
    row = (choice - 1) // 3 # gets the row
    col = (choice - 1) % 3 # gets the col
    board[row][col] = marker

def check_if_spot_marked(choice, board):
    row = (choice - 1) // 3
    col = (choice - 1) % 3
    return board[row][col] not in ["X", "O"]

def cpu_pick(board):
    while True:
        cpu_choice = random.randint(1, 9)
        if check_if_spot_marked(cpu_choice, board):
            return cpu_choice     

def check_winner(board):
    # rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]

    # columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]

    # diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None 

game_running = True
game_board = board()

while game_running:
    display_board(game_board)

    while True:
        choice = player_input()

        if choice < 1 or choice > 9:
            print("Pick a number from 1 to 9.")
            continue

        if check_if_spot_marked(choice, game_board):
            place_marker(game_board, choice, "X")
            break
        else:
            print("That spot is taken. Try again.")

        

    # cpu move
    cpu_choice = cpu_pick(game_board)
    place_marker(game_board, cpu_choice, "O")

    print(f"CPU picked {cpu_choice}")

     
    

    winner = check_winner(game_board)
    if winner:
        print(f"\n{winner} wins!")
        print("\nUpdated Board:")
        display_board(game_board)
        game_running = False


