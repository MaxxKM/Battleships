"""
Creates a 5 x 5 board filled with '.' for empty spaces
"""
def create_board():
    return [['.' for i in range(5)] for i in range(5)]

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