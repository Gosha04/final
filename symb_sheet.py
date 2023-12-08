import math

# Some of the player dict items are lists and strings, this was made to add a list to the player dict regardless
# Easy fix, dunno if its the most elegant
def add_to_list(list_stuff, stuff):
    list_stuff = list(list_stuff)
    if type(stuff) == str:
        list_stuff.append(stuff)
    elif type(stuff) == list:
        list_stuff += stuff
    return list_stuff

# Finds a word in a txt file and returns true/false
def find_word(file, word):
    try:
        with open(file, 'r') as f:
            for line in f:
                if word in line:
                    return True
        return False
    except FileNotFoundError:
        print(f"File '{file}' not found.")
        return False 

# Writes to a txt file
def write_to_file(text):
    with open ("character_sheet.txt", "w") as f:
        f.write(text + "\n")

# Takes the player class and opens the corresponding ability file
def shorten(word):
    new_word=str(word.lower())
    return new_word[:3]+"_ab.txt"

# Reads and prints a file until a paragraph break is detected
def read_till_break(file, start=1):
    line_number = 1
    with open(file, 'r') as f:
        for line in file:
            if line_number >= start:
                if line.strip() == '':
                    break
                print(line.strip())  # Process or print the line content
            line_number += 1
    return line_number

# Assigns player stats
def assign_stat():
    # 2 lists for the 2 types of stats
    stats = ["Accurate", "Cunning", "Discrete", "Persuasive", "Quick", "Resolute", "Strong", "Vigilant"]
    derived = ["Toughness", "Pain Threshold", "Defense", "Corruption Threshold", "Abomination Threshold"]
    # Pre-determined array used for generation
    att_list = [5, 7, 9, 10, 10, 11, 13, 15]
    der_val = []
    # Empty dict we'll append to shortly
    assigned_stats = {}

    # Goes through every stat and has the user set it
    for stat in stats:
        print('''
        Here are some tips:
            -Most attacks use Accurate (some Abilities change that).																
            -Initiative order is mainly determined by Quick.																
            -Weapon damage is fixed and is not modified by Strong or any other Attributes.																
            -Mystical Powers usually use Resolute.																
''')
        
        print(f"This is your available array: {att_list}")
        print(f"Please set your {stat}")

        while True:
            try:
                value = int(input("Use an integer: "))
                if value in att_list:
                    assigned_stats[stat] = value
                    att_list.remove(value)
                    break
                else:
                    print("Invalid input or attribute already assigned, please try again.")
            except ValueError:
                print("You've entered a non-integer, please try again") 

    # Sets user armor level, equipment isn't really used here since we didn't want to transcribe a large amount of arrays
    # Long story short: it would add unnecessary depth and is highly dependent on what rulebook the user wants to use
    while True:
        impede = 0
        armor = input("What type of armor would you like? (light, medium, heavy)")
        if armor == "light":
            impede = -2
            break
        elif armor == 'medium':
            impede = -3
            break
        elif armor == 'heavy':
            impede = -4
            break
        else:
            print("Please enter a valid armor type")

    # Generates the value list for derived stats
    der_val.append(int(assigned_stats['Strong'] if assigned_stats['Strong'] >= 10 else 10))
    der_val.append(int(math.ceil(assigned_stats['Strong']/2)))
    der_val.append(int(assigned_stats['Quick'] - impede))
    der_val.append(int(math.ceil(assigned_stats['Resolute']/2)))
    der_val.append(int(assigned_stats['Resolute']))
    print(der_val)

    # Populates the assigned_stats dict
    for i in range(len(derived)):
        assigned_stats[derived[i]] = der_val[i]

    return assigned_stats, armor  

# Class dictionary, contains subtypes as well
classes = {
    "Warrior": {
        "Occupations": ["Berserker", "Duelist", "Captain", "Knight", "Sellsword", "Tattooed Warrior", "Weapon Master"],
        "Abilities": "war_ab.txt"
    },
    "Mystic": {
        "Occupations": ["Clan Witch", "Ordo Magica Wizard", "Self-Taught Mystic", "Sorcerer", "Theurg of Prios"],
        "Abilities": "mys_ab.txt"
    },
    "Rogue": {
        "Occupations": ["Charlatan", "Guild Thief", "Former Cultist", "Sapper", "Thug", "Treasure-Hunter"],
        "Abilities": "rog_ab.txt"
    },
    "Hunter": {
        "Occupations": ["Bounty Hunter", "Guide", "Monster Hunter", "Scout", "Ranger", "Trailblazer", "Witchhunter"],
        "Abilities": "hunt_ab.txt"
    }
}

# Race dict, contains starting traits for each race
races = {
    "Human Ambrian": {
        "Boon": ["Contacts", "Privileged"],
        "Burden": None,
        "Monstrous Trait": None
    },
    "Human Barbarian": {
        "Boon": ["Contacts", "Bushcraft"],
        "Burden": None,
        "Monstrous Trait": "None"
    },
    "Changeling": {
        "Boon": "Long-Lived",
        "Burden": None,
        "Monstrous Trait": "Shapeshift"
    },
    "Ogre": {
        "Boon": "Long-Lived",
        "Burden": "Pariah",
        "Monstrous Trait": "Robust"
    },
    "Goblin": {
        "Boon": None,
        "Burden": ["Short-Lived", "Pariah"],
        "Monstrous Trait": "Survival Instinct"
    },
    "Elf": {
        "Boon": "Long-lived",
        "Burden": "Pariah",
        "Monstrous Trait": None
    },
    "Dwarf": {
        "Boon": ["Absolute Memory", "Earth Bound", 'Retribution'], 
        "Burden": "Pariah",
        "Monstrous Trait": None
    },
    "Abducted Human": {
        "Boon": "Bushcraft",
        "Burden": "Runaway",
        "Monstrous Trait": None
    },
    "Troll": {
        "Boon": "Long-lived",
        "Burden": "Paraih",
        "Monstrous Trait": ["Armored", "Natural Weapon", "Regeneration", "Robust"]
    }
}

# Main function
def __main__():
    # Starting player dictionary
    player = {"Corruption": 0, "Boons": [], 'Burdens': [], 'Abilities': [], 'Monstrous Traits': [], 'Archetype':'', 'Occupation':''}
    # Attribute dictionary
    attributes ={}
    # Function that picks race and class, has to be in main because it makes the errors go away
    #  If it ain't broken don't fix it type deal
    # Takes either race dict or class dict as param
    def pick(dict):
        # Class selection
        if dict == classes:
            # Checks if the selected archetype is availible
            while True:
                archetype = input("""Here you will select your class
                Warrior
                Rogue
                Hunter
                Mystic\n""")
                if archetype in classes.keys():
                    player["Archetype"] = archetype
                    break
                else: 
                    print("You have entered an invalid archetype. Please try again")
            occupations = classes[archetype]["Occupations"] 
            print("\n".join(occupations)) 
            
            # Same thing for subclasses
            while True:
                occupation = input()
                if occupation in occupations:
                    player["Occupation"] = occupation
                    break
                else: 
                    print("You have entered an invalid occupation. Please try again")

        # Race Selection
        elif dict == races:
            race_list = "\n".join(races.keys())
            # Similiar in function to class selection
            # Displays race info first and asks user to confirm
            while True:
                print(f"Here are your availible races: \n{race_list}")
                race = input()
                if race in races.keys():
                    print(races[race])
                    user = input("Would you like to select this race? (y/n)")   

                    while True:
                        if user == "y":
                            player["Race"] = race
                            break
                        elif user == "n":
                            break
                        else:
                            print("You have entered an invalid option, try again.")
                            break
                    if user == "y":
                        break
                    else: 
                        continue
                            
                else:
                    print("You have entered an invalid race. Please try again.")

            # Appends everything to corresponding dict items
            player["Boons"] = races[race]['Boon']
            player["Burdens"] = races[race]['Burden']
            player['Monstrous Traits'] = races[race]['Monstrous Trait']

    # Also has to be in main for the same reason as pick()
    def spend_xp():
        xp = 50
        print(f'''
        In the following section you will be able to spend 50 xp on various traits and abilities.
        Each boon, ability, and mystic power is worth 10 xp at its base level.
        You will also be able to purchase burdens which will provide 5 xp per burden. 
            
        Now we'll remind you as to your traits and attributes below:
        Attributes: {attributes}
        Armor Type: {armor}
        Boons: {player["Boons"]}
        Burdens: {player["Burdens"]}
        Monstrous Traits {player["Monstrous Traits"]}

        First we'll who which boons you can take, each is 10 xp. We recommend 1 or 2.
    ''')
        with open('boons.txt', 'r') as f:
            print(f.read())

        # User selects boons, checks if boon exists and then appends it to player["Boons"]
        # If the user already has it or it doesn't exist then loop
        # Buy boons till quit
        while xp > 0:
            boon_pick = input("\nPlease select a boon: ")
            if boon_pick == '':
                print("Moving on.")
                break
            elif find_word('boons.txt', boon_pick) and boon_pick not in player["Boons"]:
                player["Boons"].append(boon_pick)
                xp -= 10
                print(f"{boon_pick} added to your boons.")
                print(f"You have {xp} XP remaining.")
            elif boon_pick in player["Boons"]:
                print("You already have this boon. Please select another.")
            else:
                print("This boon doesn't exist. Please try again.")
            
            if xp == 0:
                print("You've run out of XP. Moving on.")
                break
            
            user = input("If you wish to stop buying boons, press 'y'. Otherwise, press anything: ")
            if user.lower() == 'y':
                break

        print("\nIf you've run out of xp, don't worry. By taking a burden you can gain 5 xp. \nTake as many as you like")
        with open ('burdens.txt', 'r') as f:
            print(f.read())

        # Exact same thing for burdens
        while True:
            burd_pick = input("\nPlease select a burden: ")
            if burd_pick == '':
                print("Moving on.")
                break
            elif find_word('burdens.txt', burd_pick) and burd_pick not in player["Burdens"]:
                player["Burdens"].append(burd_pick)
                xp += 5
                print(f"{burd_pick} added to your burdens.")
                print(f"You have {xp} XP remaining.")
            else:
                print("This burden doesn't exist or you already have it. Please try again.")

            user = input("If you wish to stop buying burdens, press 'y'. Otherwise, press anything: ")
            if user.lower() == 'y':
                break
        
        print(f"Almost done! Using your remaining {xp}xp buy some abilities, worth 10 each. \nKeep in mind mystics get 1 more bonus section")
        file_name = shorten(str(player["Archetype"]))
        print(file_name)
        with open(f'{file_name}', 'r') as f:
            print(f.read())

        # Exact same thing for classes with their corresponding abilities
        while xp > 0:
            ab_pick = input("\nPlease select an ability: ")
            if ab_pick == '':
                print("Moving on.")
                break
            elif find_word(f'{file_name}', ab_pick) and ab_pick not in player["Abilities"]:
                player["Abilities"].append(ab_pick)
                xp -= 10
                print(f"{ab_pick} added to your abilities.")
                print(f"You have {xp} XP remaining.")
            else:
                print("This ability doesn't exist or you already have it. Please try again.")

            if xp == 0:
                print("You've run out of XP. Moving on.")
                break

            user = input("If you wish to stop buying abilities, press 'y'. Otherwise, press anything: ")
            if user.lower() == 'y':
                break 
            
            # Special magic section for mystic class
            if player["Archetype"] == "Mystic":
                print("\nWelcome to the special Mystic power section, each is worth 10 xp. \nUnless you are are a 'Self-Taught Mystic' you will be forced to stick with your occupations powers.")   
                match player["Occupation"]:
                    case "Theurgy":
                        read_till_break("mys_ab.txt", 22)
                    case "Sorcerer":
                        read_till_break("mys_ab.txt", 43)
                    case "Clan Witch":
                        read_till_break('mys_ab.txt', 53)
                    case "Ordo Magica Wizard":
                        read_till_break('mys_ab.txt', 73)
                    case "Self-Taught Mystic":
                        read_till_break("mys_ab.txt", 22)
                        read_till_break("mys_ab.txt", 43)
                        read_till_break('mys_ab.txt', 53)
                        read_till_break('mys_ab.txt', 73)

            while xp > 0:
                pow_pick = input("\nPlease select a power: ")
                if pow_pick == '':
                    print("Moving on.")
                    break
                elif find_word(f'{file_name}', pow_pick) and pow_pick not in player["Abilities"]:
                    player["Abilities"].append(pow_pick)
                    xp -= 10
                    player['Corruption'] += 1
                    print(f"{pow_pick} added to your abilities.")
                    print(f"You have {xp} XP remaining.")
                else:
                    print("This power doesn't exist or you already have it. Please try again.")

                if xp == 0:
                    print("You've run out of XP. Moving on.")
                    break

                user = input("If you wish to stop buying powers, press 'y'. Otherwise, press anything: ")
                if user.lower() == 'y':
                    break 
        return xp
    
    print('''Welcome to the Symbaroum Character Creator!
         Using this program you can easily create a character for any session and any table. 
         Though do keep in mind: while most general character bits are included here,
         you will still need the core rulebook should you wish for your character to work mechanically.
         That being said, you'll be ready to go in no time at all. Have fun!''')
    
    # Class everything and runs the main chunk of the program
    print("\nFirst lets select your race, shall we?")
    pick(races)
    print("\nAnd now for class")
    pick(classes)

    # Splits assign_stat() returns into varaibles
    print(f"\nLets breifly go over what you have so far: {player} \nOnwards we go: attributes and armor coming up!")
    stuff = assign_stat()
    attributes = stuff[0]
    armor = stuff[1].capitalize
    print(f'\nPhew, almost done. All we have left to do is traits and abilities. Choose wisely!')

    # If it ain't broke don't fix it 2: if it is broke and the solution is weird, roll with it
    # Assigns all traits to a list var and then adds everything up via add_to_list
    boons = list(player['Boons'])
    player["Boons"] = []
    add_to_list(player["Boons"], boons)
    burdens = player['Burdens']
    player["Burdens"] = []
    add_to_list(player["Burdens"], burdens)
    abs = player['Abilities']
    player["Abilities"] = []
    add_to_list(player["Abilities"], abs)

    xp = spend_xp()
    input(player["Abilities"])
    print("\nNow that we're done, we'll compile all you're info into a file")
    
    # This is whats going to get written to character_sheet.txt
    text = f'''~*~*~ Character Sheet ~*~*~

--Personal Info--
Race: {player["Race"]}
Archetype: {player["Archetype"]}
Occupation: {player["Occupation"]}

--Attributes--
Accurate: {attributes["Accurate"]}  Cunning: {attributes["Cunning"]} 
Discrete: {attributes["Discrete"]}  Persuasive: {attributes["Persuasive"]}
Quick: {attributes["Quick"]}    Resolute: {attributes["Resolute"]}
Strong: {attributes["Strong"]}  Vigilant: {attributes["Vigilant"]}
Toughness: {attributes["Toughness"]}    Pain Threshold: {attributes["Pain Threshold"]}
Defense: {attributes["Defense"]}    Corruption Threshold: {attributes["Corruption Threshold"]}
Abomination Threshold: {attributes["Abomination Threshold"]}    Corruption: {player["Corruption"]}

--Armor--
Armor Level: {armor}

--Traits and Abilities--
Boons: {player["Boons"]}
Burdens: {player["Burdens"]}
Abilities: {player["Abilities"]}
Monstrous Traits: {player["Monstrous Traits"]}

Your remaining experience: {xp}

All you have to do now is use the core rules to flesh out your character and add equipment.

Have fun!
'''
    # Writes to file
    write_to_file(text)
    with open('character_sheet.txt', 'r') as f:
        print(f"\n{f.read}")

# Call main
__main__()


