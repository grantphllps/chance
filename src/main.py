from classes import board

if __name__ == '__main__':
    
    board = board()
    board.register_players()
    board.draft()
    board.placement()
    board.run_game()