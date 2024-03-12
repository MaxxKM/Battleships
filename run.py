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
Main Game Loop
"""
def game_loop(player_board, computer_board):
    place_ships(player_board, 4)
    place_ships(computer_board, 4)

    computer_guesses = [] # List to store the computer's guesses
    
    while True:
        print("Player's board:")
        print_board(player_board)
        print("Computer's board:")
        print_board(computer_board, True)

        # Player's turn
        while True:
            try:
                row = int(input("Enter the row (0-4): "))
                col = int(input("Enter the column (0-4): "))
                if row < 0 or row > 4 or col < 0 or col > 4:
                    print("Invalid input! Please enter a number between 0 and 4.")
                    continue
                if computer_board[row][col] in ['X', 'O']:
                    print("You already guessed this location. Please guess again.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
        
        if computer_board[row][col] == '@':
            print("You Hit!")
            computer_board[row][col] = 'X'
        else:
            print("You Missed!")
            computer_board[row][col] = 'O'
        """
        Checks if there is any ships left on computers boards. if not
        player wins.
        """
        if '@' not in [cell for row in computer_board for cell in row]:
            print("You win!")
            break
        
        # Computer's turn
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            guess = (row, col)
            if guess not in computer_guesses:
                computer_guesses.append(guess)
                break
        
        if player_board[row][col] == '@':
            print("Computer hit!")
            player_board[row][col] = 'X'
        else:
            print("Computer missed!")
            player_board[row][col] = 'O'
        
        """
        Checks if there is any ships left on players boards. if not
        computer wins.
        """
        if '@' not in [cell for row in player_board for cell in row]:
            print("Computer wins!")
            break

"""
Main functions for the game and welcome text
"""
def main():
    player_name = input("Enter your name: ")
    player_board = create_board()
    computer_board = create_board()
    
    print(f"Welcome, {player_name}! Let's play Battleship!")
    print("The board is 5 x 5 in size")
    print("The numbers of ships are 4 each")
    print("Your ships are marked with '@'")
    print("Hits are marked with 'X' and misses with 'O'")
    print("Have Fun!")
    game_loop(player_board, computer_board)

if __name__ == "__main__":
    main()