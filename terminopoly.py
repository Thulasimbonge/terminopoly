import os
import random
import pickle

#dice to roll
#the dice rolls and returns a number stored in a list
def dice():
    roll_skip = input("Press enter to roll dice or s to skip: ")
    dice_rolls = []
    while roll_skip != "s":
        dice = random.randint(1,6)
        dice_rolls.append(dice)
        if dice == 6:
            roll_skip
        else:
            break
    return dice_rolls


#players and their info is stored in a dictionary
PLAYERS = {}

#function for creating player
def create_players(name):
    PLAYERS[name] = {
        'account': 500,
        'position': 0,
        'condition':"free",
        'sentence': 0,
        'get out of jail': 0
    }


#locations on the board 
LOCATIONS = {
    0: {
        "name": "Begin",
        "owner": '',
        "rent": 0,
        "price": 0,
    },
    1:{
        "name": "Python Hotel",
        "owner": '',
        "rent": 10,
        "price": 20,
    },
    2: {
        "name": "Chance",
        "owner": '',
        "rent": 0,
        "price": 0,
    },
    3: {
        "name": "OOP-sy B&B",
        "owner": '',
        "rent": 10,
        "price": 20,
    },
    4: {
        "name": 'Jail',
        "owner": '',
        "rent": 0,
        "price": 0,
    },
    5: {
        "name": "CSS Heights",
        "owner": '',
        "rent": 20,
        "price": 30,
    },
    6: {
        "name": "Community Chest",
        "owner": '',
        "rent": 0,
        "price": 0,
    },
    7: {
        "name": "JS Inn",
        "owner": '',
        "rent": 30,
        "price": 40,
    },
    8: {
        "name": "Free Parking",
        "owner": '',
        "rent": 0,
        "price": 0,
    },
    9: {
        "name": "Memory Space",
        "owner": '',
        "rent": 40,
        "price": 50,
    }, 
    10: {
        "name": "Chance",
        "owner": '',
        "rent": 0,
        "price": 0,
    },
    11: {
        "name": "RAM House",
        "owner": '',
        "rent": 50,
        "price": 60,
    },
    12: {
        "name": "Go straight to jail",
        "owner": '',
        "rent": 0,
        "price": 0,
    },
    13: {
        "name": "Cache de Cookie",
        "owner": '',
        "rent": 60,
        "price": 70,
    },
    14: {
        "name": "Community Chest",
        "owner": '',
        "rent": 0,
        "price": 0,
    },
    15: {
        "name": "ROM-ance Inn",
        "owner": '',
        "rent": 70,
        "price": 80,
    },
}

#saving game in list and adding extension
def save_the_game():
    save_name = input("Enter name to save the game: ")
    print("Saving game as",save_name)
    save_name += ".tem"

    #file will close and game will be saved
    info_of_game = [PLAYERS, LOCATIONS]
    file = open(save_name, "wb")

    #writing name to the info of the game
    pickle.dump(info_of_game,file)
    file.close()
    print("The game has been saved")

#loading a saved game in a list
def load_the_game():
    saved_games = []
    
    #each location in folder that has tem extension is fetched and saved into saved games list
    for folder_location in os.listdir(os.getcwd()):
        if folder_location[-1:-4:-1] == 'met':
            saved_games.append(folder_location)
    
    #user must select the saved game using a number
    if saved_games:
        print("User must select a game saved:")
        number = 1
        for game in saved_games:
            print(str(number)+". "+game)
        press_number = int(input("Please enter the number of the saved game:"))

        global LOCATIONS
        global PLAYERS
        print("Loading the saved game")
        file = open(saved_games[press_number - 1], 'rb')
        info_of_game = pickle.load(file)
        file.close()

        #the info of the game (saved players and locations dictionaries) is loaded and game is continued
        PLAYERS = info_of_game[0]
        LOCATIONS = info_of_game[1]
        game_position()
    else:
        print("No games have been saved. Game is now exiting...")



#by accessing the players from the PLAYERS dictionary, we ask them to roll dice

def game_position():
    position_you_cannot_buy = ["Jail", "Go straight to jail", "Community Chest", "Chance", "Free Parking", "Begin"] 
    while True:
        for player in PLAYERS.keys():
            print(player, "roll the dice")

            #create a new local dice_rolls variable which will store the call for dice function
                #allowing player to roll the dice
            dice_rolls = dice()
            
            #for each dice roll, it must show the player and their money in their account
            for dice_roll in dice_rolls:
                print(player+"'s account is WTC"+str(PLAYERS[player]['account']))

                #players_position variable by taking the dice roll number and adding it to the player position
                players_position = PLAYERS[player]['position'] + dice_roll
                PLAYERS[player]['position'] += dice_roll

                # if players position > 15 then don't show and also gives player money
                if players_position > 15:
                    free_money = 200
                    PLAYERS[player]['account'] += free_money
                    PLAYERS[player]['position'] -= 15
                    print("You have passed begin, you receive WTC"+str(free_money))

                print(player,"is now on position"+"'"+LOCATIONS[PLAYERS[player]['position']]['name']+"'" )

                #variable assigned for location where player landed
                position_player_landed_on = LOCATIONS[PLAYERS[player]['position']]

                #conditions for landing on community chest, chance and jail
                if position_player_landed_on['name'] == 'Community Chest':
                    random_choices = ["Bank owes you", "You owe the bank"]
                    random_choice = random_choices[random.randint(0,1)]
                                        
                    if random_choice == "Bank owes you":
                        amount_bank_pays_player = 50
                        PLAYERS[player]['account'] += amount_bank_pays_player
                        print(player, "The bank paid you WTC"+str(amount_bank_pays_player))

                    if random_choice == "You owe the bank":
                        amount_player_pays_bank = 50
                        PLAYERS[player]['account'] -= amount_player_pays_bank
                        print(player, "you paid the bank WTC"+str(amount_player_pays_bank))
                
                if position_player_landed_on['name'] == "Chance":
                    random_choices = ["Get out of jail free card", "Go straight to jail"]
                    random_choice = random_choices[random.randint(0,1)]

                    if random_choice == "Get out of jail free card":
                        print(player, "you got a get out of jail free card")
                        PLAYERS[player]['get out of jail'] += 1

                    if random_choice == "Go straight to jail":
                        print(player, "go straight to jail")
                        PLAYERS[player]['position'] = 4

                if position_player_landed_on['name'] == 'Free Parking':
                    pass

                if position_player_landed_on['name'] == 'Go straight to jail':
                    print(player, "go straight to jail")
                    PLAYERS[player]['position'] = 4
                    print(player, "now you have entered jail")

                if position_player_landed_on['name'] == "Jail":
                    print(player, "you are now in  jail")
                    PLAYERS[player]['condition'] = 'jail'
                    PLAYERS[player]['sentence'] = 3

                    if PLAYERS[player]['get out of jail'] > 0:
                        PLAYERS[player]['get out of jail'] -= 1
                        print(player, "you have used your get out of jail free card ")
                    else:
                        print("You must now roll the dice and get a 6 to get out. You will move 6 places but won't be able to roll again. You have 3 attempts ")
                        for sentence in range(1, PLAYERS[player]['sentence']+1):
                            roll_dice_to_get_out = dice()
                            if 6 in roll_dice_to_get_out:
                                PLAYERS[player]['condition'] = 'free'
                                PLAYERS[player]['sentence'] = 0
                                print(player, "you are now out of jail")
                                PLAYERS[player]['position'] += 1
                                print("Your new position is now", LOCATIONS[PLAYERS[player]['position']]['name'])
                                break
                        
                            if sentence == PLAYERS[player]['sentence']:
                                pay_get_out_of_jail = 200
                                PLAYERS[player]['account'] -= pay_get_out_of_jail
                                PLAYERS[player]['position'] += 1
                                print(player, "you paid WTC"+str(pay_get_out_of_jail),"to get out of jail")

                #check if player is the owner so they don't pay themselves
                if position_player_landed_on['owner'] == '' and position_player_landed_on['name'] not in position_you_cannot_buy: # add another condition later
                    buy = input("Do you want to buy "+position_player_landed_on['name']+" for WTC"+str(position_player_landed_on['price'])+"? (Y/N)")
                    if buy.upper() == "Y":
                        LOCATIONS[PLAYERS[player]['position']]['owner'] = player
                        PLAYERS[player]['account'] -= LOCATIONS[PLAYERS[player]['position']]['price']
                        print(player, "your account is now WTC"+str(PLAYERS[player]['account']))
                elif position_player_landed_on['owner'] != '' and position_player_landed_on['owner'] != player and position_player_landed_on['name'] not in position_you_cannot_buy: # add another condition later
                    rent = LOCATIONS[PLAYERS[player]['position']]['rent']
                    PLAYERS[player]['account'] -= rent
                    print(player, "You have paid WTC"+str(rent),"to",LOCATIONS[PLAYERS[player]['position']]['owner'])

        want_continue = input("Do you want to continue? (Y/N): ")
        if want_continue.upper() == 'Y':
            pass
        elif want_continue.upper() == 'N':
            want_save = input("Do you want to save the game? (Y/N): ")
            if want_save.upper() == "Y":
                save_the_game()
                break
            else:
                print("Ending game")
                break


#load saved game or new game
def play():
    ask_player = input("Do you want to load saved game or new game?(S/N): ")
    if ask_player.upper() == "S":
        load_the_game()

    else:
        add_player = input("Do you want to add a player?(Y/N): ")
        while add_player.upper() == "Y":
            enter_name = input("Please enter your name: ")
            create_players(enter_name)
            add_player = input("Do you want to add a player?(Y/N): ")
        game_position()
play()
