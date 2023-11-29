# cli.py

import logging
from logic import GameBoard, Player, TicTacToeGame  # Replace 'your_game_module' with the actual module name

# Configure logging
logging.basicConfig(filename='tic_tac_toe.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting a new game of Tic-Tac-Toe")

    # Ask the user if they want to play against a bot
    play_mode = input("Do you want to play against a bot? (y/n): ").strip().lower()
    single_player = play_mode == 'y'

    # Initialize and start the game
    game = TicTacToeGame(single_player=single_player)
    game.play()

    logging.info("Game ended")

if __name__ == "__main__":
    main()
```

```py
# logic.py

import random
class GameBoard:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
    def is_valid_move(self, x, y):
        if 0 <= x <= 2 and 0 <= y <= 2 and self.board[x][y] is None:
            return True
        return False
    def make_move(self, x, y, player):
        if self.is_valid_move(x, y):
            self.board[x][y] = player
            return True
        return False
    def display_board(self):
        for row in self.board:
            print(" | ".join([' ' if cell is None else cell for cell in row]))
            print("-" * 9)

class Player:
    def __init__(self, symbol, is_bot=False):
        self.symbol = symbol
        self.is_bot = is_bot

    def get_move(self, board):
        if self.is_bot:
            return self.get_bot_move(board)
        else:
            return self.get_human_move()

    def get_bot_move(self, board):
        # Your bot logic here (random for simplicity)
        x, y = random.randint(0, 2), random.randint(0, 2)
        while not board.is_valid_move(x, y):
            x, y = random.randint(0, 2), random.randint(0, 2)
        return x, y

    def get_human_move(self):
        x, y = map(int, input("Enter your move (x,y): ").split(","))
        return x, y

class TicTacToeGame:
    def __init__(self, single_player=False):
        self.board = GameBoard()
        self.players = [Player("X"), Player("O", is_bot=single_player)]

    def play(self):
        current_player = 0
        while not self.is_game_over():
            x, y = self.players[current_player].get_move(self.board)
            if self.board.make_move(x, y, self.players[current_player].symbol):
                self.board.display_board()
                if self.check_winner(self.players[current_player].symbol):
                    print(f"Player {self.players[current_player].symbol} wins!")
                    return
                current_player = 1 - current_player
            else:
                print("Invalid move, try again.")

        if self.is_draw():
            print("It's a draw!")
        else:
            print(f"Player {self.players[current_player].symbol} wins!")

    def is_game_over(self):
        # The game is over if there's a winner or a draw
        return self.check_winner("X") or self.check_winner("O") or self.is_draw()

    def check_winner(self, player_symbol):
        # Check rows, columns, and diagonals for a winner
        for row in self.board.board:
            if all(cell == player_symbol for cell in row):
                return True

        for col in range(3):
            if all(self.board.board[row][col] == player_symbol for row in range(3)):
                return True

        if all(self.board.board[i][i] == player_symbol for i in range(3)):
            return True

        if all(self.board.board[i][2 - i] == player_symbol for i in range(3)):
            return True

        return False

    def is_draw(self):
        # The game is a draw if there are no empty spaces left on the board
        for row in self.board.board:
            if any(cell is None for cell in row):
                return False
        return True
```
