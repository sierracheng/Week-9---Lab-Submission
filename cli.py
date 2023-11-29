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