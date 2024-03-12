"""
Creates a 5 x 5 board filled with '.' for empty spaces
"""
def create_board():
    return [['.' for i in range(5)] for i in range(5)]

"""
Places ships at random positions
"""
def place_ship(board, occupied_positions):
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        position = (row, col)
        """
        Check if the position is empty and not already occupied
        """
        if board[row][col] == '.' and position not in occupied_positions:
            board[row][col] = '@'
            occupied_positions.append(position)
            return

"""
place multiple ships on the board
"""
def place_ships(board, num_ships):
    occupied_positions = []
    for _ in range(num_ships):
        place_ship(board, occupied_positions)

"""
Prints the players and computers board for the player to show
the guesses, hits, misses etc.
"""
def print_board(board, is_computer_board=False):
    board_to_print = [row.copy() for row in board]
    if is_computer_board:
        for i in range(len(board_to_print)):
            for j in range(len(board_to_print[i])):
                if board_to_print[i][j] == '@':
                    board_to_print[i][j] = '.' # Hide the computers ships, so player cannot see them
    for row in board_to_print:
        print(' '.join(row))


"""
Gets the name of the player from their input
"""
def get_player_name():

    return input("Enter you name: ")

def main():
    player_name = get_player_name()
    print(f"Welcome {player_name} to a game of Battleships!")
    print("The board is 5 x 5 in size")

main()