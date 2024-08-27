from classes import board
from territory_defs import TERRITORIES, CONTIENENTS, STARTING_TROOPS, MAX_ATTACKING_TROOPS, MAX_DEFENDING_TROOPS


if __name__ == '__main__':
    
    board = board()
    board.setup_test_scenario()

    board.place_troops_in_empty_territory(board.players["player1"], 'Alaska', 3)
    board.place_troops_in_empty_territory(board.players["player1"], 'Alberta', 3)
    board.place_troops_in_empty_territory(board.players["player1"], 'Kamchatka', 3)
    board.place_troops_in_empty_territory(board.players["player1"], 'Mongolia', 3)
    board.place_troops_in_empty_territory(board.players["player1"], 'China', 3)
    board.place_troops_in_empty_territory(board.players["player1"], 'Northern Europe', 3)

    #print(board.owned_territories(board.players["player1"]))
    
    #Test functionality here
    print(board.check_territories_connected(board.players["player1"], 'Alaska', 'Northern Europe'))
    