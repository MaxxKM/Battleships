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



def get_player_name():
    """
    Gets the name of the player from their input
    """
    return input("Enter you name: ")

def main():
    player_name = get_player_name()
    print(f"Welcome {player_name} to a game of Battleships!")
    print("The board is 5 x 5 in size")

main()