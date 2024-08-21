import random
import copy
from territory_defs import TERRITORIES, CONTIENENTS, STARTING_TROOPS, MAX_ATTACKING_TROOPS, MAX_DEFENDING_TROOPS

#TODO: Keep working on expand function,

class continent:
    def __init__(self,continent_key, continent_defs):
        self.name = str(continent_key)
        self.owner = None
        self.bonus = continent_defs[continent_key]['bonus']
        
        #Dictionary of territory objects
        self.territories = {}

        for territory_key in CONTIENENTS[continent_key]["territories"]:
            self.territories[territory_key] = territory(territory_key, TERRITORIES)

    def __str__(self):
        return f"{self.territories}"

class territory:

    def __init__(self,territory_key, territory_defs):
        self.name = territory_key
        self.occpying_troops = 0
        self.neighbors = territory_defs[territory_key]['neighbors']
        self.occupant = None
        self.continent = territory_defs[territory_key]['continent']

    def add_troops(self, number_of_troops):
        self.occpying_troops += number_of_troops
        print(f"{self.name} now has {self.occpying_troops} troops")

    def remove_troops(self, number_of_troops):
        self.occpying_troops -= number_of_troops
        print(f"{self.name} now has {self.occpying_troops} troops")
        if self.occpying_troops == 0:
            self.occuapnt = None
        
        return self.occpying_troops
    
    def set_occupant(self, player):
        self.occupant = player

    def __str__(self):
        return f"Territory {self.name} is occupied by {self.occupant} and has {self.occpying_troops} troops"

class player:
    def __init__(self, name):
        self.name = name

        #unsure if these are needed
        self.territories = []
        self.continents = []

        self.resource_cards = []

        self.turn_order = None
        self.placement_order = None
        self.troops_to_place = None

    def recruit(self):
        """
        Recruit
        """

        troops_to__recruit = self.territories // 3
        if troops_to__recruit < 3:
            troops_to__recruit = 3
        
        return troops_to__recruit

    def __str__(self):
        return f"{self.name}"
    
class board:

    def __init__(self):
        
        self.players = {}
        self.turn_order = {}
        self.contienent_def = CONTIENENTS
        self.territory_defs = TERRITORIES
        self.contienents = {}
        self.territories = {}

        for contienent_key in CONTIENENTS.keys():
            for territory_key in CONTIENENTS[contienent_key]["territories"]:
                self.territories[territory_key] = territory(territory_key, TERRITORIES)

    def __str__(self):
        return f"{self.contienents}"

    def input_territory_key_from_list(self, prompt, options):
        while True:
            key = input(prompt)
            if key in options:
                return key
            else:
                print(f"Invali input. Please choose from {options}")

    def get_turn_player(self,idx):
        turn_player = self.turn_order[idx]
        return self.players[turn_player]

    def roll6(self, n):
        rolls = []
        try:
            if (n >= 1):
                for i in range(0,n):
                    p = random.randint(1,6)
                    rolls.append(p)
                
            else:
                print("Bad number of rolls")
        except ValueError as e:
            print(f"{e}")

        return rolls

    def placement(self):
        """
        First troop placement, should only be used once
        """
        number_of_players = len(self.players)
        for idx in range(number_of_players):
            placement_player = self.get_turn_player(idx)
            self.place_troops_in_empty_territory(placement_player, STARTING_TROOPS)

    #Troop placement and movement methods
    #Place starting troops >> placement()
    #Place troops into an empty territory >> place_troops_in_empty_territory()
    #place troops into a terriroty the player occpies >> place_troops_in_occupied_territory()
    #Move troops to an unoccpied territory >> move_troops_to_unoccupied
    #attack

    def place_troops_in_empty_territory(self, player, troops_to_place):
        """
        Place troops on a territory
        """
        placement_success = False

        while not placement_success:
            territory_key = input(f"{player.name}, Enter a territory to place troops >> ")
            
            try:
                selected_territory = self.territories[territory_key]
                if selected_territory.occupant == None or selected_territory.occupant == player:
                    selected_territory.add_troops(troops_to_place)
                    selected_territory.set_occupant(player.name)
                    placement_success = True
                else:
                    print(f"This territory is already occupied by {selected_territory.occupant}")
            except KeyError:
                print("Invalid territory")

    def place_troops_in_occupied_territory(self, player, max_troops):
        """
        Place troops in a territory owned by the player
        """
        placement_success = False

        while not placement_success:
            owned_territories = self.owned_territories(player)

            territory_key = input(f"{player.name}, Enter a territory to place troops {owned_territories} >> ")
            try:
                selected_territory = self.territories[territory_key]
                if selected_territory.occupant == player.name:
                    troops_to_place = int(input(f"Enter number of troops to place in {selected_territory.name} (max {max_troops}) >> "))
                    selected_territory.add_troops(troops_to_place)
                    placement_success = True

                    return max_troops - troops_to_place
                else:
                    print(f"This territory is not occupied by {player.name}")

            except KeyError:
                print("Invalid territory")

    def count_territoires(self, player):
        count = 0
        for territory in self.territories.keys():
            if self.territories[territory].occupant == player.name:
                count += 1
        return count

    def register_players(self):
        # Add players

        players = {}

        add_players = True
        while add_players:
            user_in = input('Enter player name or type "done">> ')
            match user_in:
                case "done":
                    add_players = False
                case _: 
                    players[user_in] = player(user_in)
        
        self.players = copy.deepcopy(players)
        print(f"Players: {self.players}")

    def build_draft(self,number_of_players):
        """
        Placement
        Turn order
        Number of troops
        """
        placement_cards = [1, 2] #1st, 2nd
        turn_order_cards = [1, 2] #1st, 2nd
        number_of_troops = [10, 9] # number of troops

        if number_of_players >= 3:
            placement_cards.append(3)
            turn_order_cards.append(3)
            number_of_troops.append(8)

        if number_of_players >= 4:
            placement_cards.append(4)
            turn_order_cards.append(4)
            number_of_troops.append(7)

        if number_of_players >= 5:
            placement_cards.append(5)
            turn_order_cards.append(5)
            number_of_troops.append(6)

        draft_cards = {
            'placement': placement_cards,
            'turn_order': turn_order_cards,
            'number_of_troops': number_of_troops
        }

        return draft_cards
    
    def recruit(self, player):
        """
        Recruit
        """

        population = self.count_territoires(player)
        troops_to__recruit = population // 3
        if troops_to__recruit < 3:
            troops_to__recruit = 3
        
        print(f"{player.name} has {population} territories and can recruit {troops_to__recruit} troops")

        return troops_to__recruit

    def draft(self):
        """
        Draft
        """

        draft_order = list(self.players.keys())
        random.shuffle(draft_order)

        self.turn_order = copy.deepcopy(draft_order)
        print(f"Turn order: {self.turn_order}")

    def owned_territories(self, player):
        owned_terrs = []
        for territory_key in self.territories.keys():
            if self.territories[territory_key].occupant == player.name:
                owned_terrs.append(territory_key)

        return owned_terrs

    def move_troops_to_unoccupied_territory(self,player, source_territory, target_territory, number_of_troops):
        source_territory.occpying_troops -= number_of_troops
        target_territory.occpying_troops += number_of_troops
        target_territory.occupant = player.name
        
        print(f"{source_territory}")
        print(f"{target_territory}")
        
    def expand(self, player):

        """
        Expand Todo
        - Ask successful attacker how many troops to move
        - What to do if a player does not control any territories
        """
        print(f"{player.name} is expanding")

        # 1) Ask turn player where expansion should originate from, or if they are done with expansion
        owned_territories = copy.deepcopy(self.owned_territories(player))
        owned_territories.append("done")     
        expand = self.input_territory_key_from_list(f"Enter 'done' to end expand phase or a territory to expand from {owned_territories} >> ", owned_territories)

        if expand == 'done':
            return False
        
        try:
            source_territory = self.territories[expand]
            if source_territory.occupant == player.name:
                if source_territory.occpying_troops > 1:
                    #Player owns the territory and has more than 1 troop
                    print(f"{player.name} is expanding from {source_territory.name}")
                else:
                    #Player owns the territory but only has 1 troop
                    print(f"{player.name} only has 1 troop in {source_territory.name}, cannot expand from here")
                    return True
            else:
                #Player does not own the territory, cannot expand from here
                print(f"{player.name} does not own {source_territory.name}")
                return True
        except KeyError:
            print("Invalid territory entered")
            return True
        
        # 2) Ask turn player where the expansion should move, or cancel
        candidate_territories = copy.deepcopy(source_territory.neighbors)
        candidate_territories.append("cancel")
        selected_target = self.input_territory_key_from_list(f"Expand to >> {source_territory.neighbors} >> ", candidate_territories)

        if selected_target == "cancel":
            return True 

        try:
            target_territory = self.territories[selected_target]

            if target_territory.occupant != player.name and target_territory.occupant == None:
                #Player does not own the territory and the territory is unoccupied
                troops_to_move = int(input(f"Enter number of troops to move to {target_territory.name} (max {source_territory.occpying_troops - 1} )>> "))
                print(f"{player.name} is moving {troops_to_move} troops from {source_territory.name} to {target_territory.name}")
                self.move_troops_to_unoccupied_territory(player, source_territory, target_territory, troops_to_move)
                return True

            elif target_territory.occupant == player.name:
                #Player owns the territory
                print(f"{player.name} already owns {target_territory.name}")
                return True

            elif target_territory.occupant != player.name:
                #Attacking into an occupied territory
                max_attack_troops = min(source_territory.occpying_troops - 1, MAX_ATTACKING_TROOPS)

                valid_troops = False
                while not valid_troops:
                    try:
                        attacking_troops = int(input(f"Enter number of troops to attack into {target_territory.name} (max {max_attack_troops} )>> "))
                        if attacking_troops > max_attack_troops or attacking_troops <= 0:
                            print(f"Entered invalid number of troops: {attacking_troops}")
                        else:
                            valid_troops = True
                    except ValueError as e:
                        print("invalid input, try again")
                
                attacking_troops = min(attacking_troops, max_attack_troops)
                defending_troops = min(target_territory.occpying_troops, MAX_DEFENDING_TROOPS)


                attacking_rolls = self.roll6(attacking_troops)
                defending_rolls = self.roll6(defending_troops)

                print(f"Raw attacking rolls: {attacking_rolls}")
                print(f"Raw defending rolls: {defending_rolls}")

                attacking_rolls.sort(reverse = True)
                defending_rolls.sort(reverse = True)

                #Remove attacking Rolls until there are the same number of attacking/defending rolls
                while len(attacking_rolls) > len(defending_rolls):
                    attacking_rolls.pop(-1)

                print(f"Final attacking rolls: {attacking_rolls}")
                print(f"Final defending rolls: {defending_rolls}")

                #Pay the butcher's bill
                attacking_troops_lost = 0
                defending_troops_lost = 0

                number_of_battles = len(attacking_rolls)

                for i in range(number_of_battles):
                    if attacking_rolls[i] > defending_rolls[i]:
                        defending_troops_lost += 1
                    else:
                        attacking_troops_lost += 1

                print(f"Attackers Lost: {attacking_troops_lost}")
                print(f"Defenders Lost: {defending_troops_lost}")

                source_territory.remove_troops(attacking_troops_lost)
                remaining_troops = target_territory.remove_troops(defending_troops_lost) #If remove troops takes the territory down to zero, it becomes "un-occupied"

                #Expand into the newly concured territory
                if (remaining_troops == 0):
                    #get how many troops to move (minimum the number surviving the attack)
                    minimum_of_troops_moving = attacking_troops - attacking_troops_lost
                    maximum_of_troops_moving = source_territory.occpying_troops - 1
                    troops_to_move = int(input(f"How many troops to move into new territory, minimum: {minimum_of_troops_moving}, maximum: {maximum_of_troops_moving} >> "))
                    self.move_troops_to_unoccupied_territory(player, source_territory, target_territory, troops_to_move)
  
        except KeyError:
            print("Invalid territory entered")
            return True

        return True
    
    def run_game(self):
        """
        Players is a dictionary of the player objects
        Board.territories is a dictionary of the territory objects
        """
        turn_idx = 0
        game_over = False

        while not game_over:
            #Start of a turn
            current_player = self.get_turn_player(turn_idx)
            print(f"Start of {current_player.name}'s turn")

            #Recruit
            new_troops = self.recruit(current_player)

            #Place new troops
            while new_troops > 0:
                new_troops = self.place_troops_in_occupied_territory(current_player, new_troops)

            #Expand
            expand = True
            while expand:
                expand = self.expand(current_player)

            #Maneuver

            #End of turn
            turn_idx += 1

