import math

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

def write_to_file(text):
    with open ("character_sheet.txt", "w") as f:
        f.write(text + "\n")
 
def shorten(word):
    list_word = list(word)
    new_word = ''.join(list_word[0:3])
    new_word = new_word.lower()
    return new_word+"_ab.txt"

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

def assign_stat():
    stats = ["Accurate", "Cunning", "Discreet", "Persuasive", "Quick", "Resolute", "Strong", "Vigilant"]
    derived = ["Toughness", "Pain Threshold", "Defense", "Corruption Threshold", "Abomination Threshold"]
    att_list = [5, 7, 9, 10, 10, 11, 13, 15]
    der_val = []
    assigned_stats = {}

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

    der_val.append(int(assigned_stats['Strong'] if assigned_stats['Strong'] >= 10 else 10))
    der_val.append(int(math.ceil(assigned_stats['Strong']/2)))
    der_val.append(int(assigned_stats['Quick'] - impede))
    der_val.append(int(math.ceil(assigned_stats['Resolute']/2)))
    der_val.append(int(assigned_stats['Resolute']))
    print(der_val)

    for i in range(len(derived)):
        assigned_stats[derived[i]] = der_val[i]

    return assigned_stats, armor

# stuff = assign_stat()
# attributes = stuff[0]
# armor = stuff[1].capitalize    

def pick(dict):
    if dict == classes:
        while True:
            archetype = input("""Here you will select your class
              Warrior
              Rogue
              Hunter
              Mystic""")
            if archetype in classes.keys():
                player["Archetype"] = archetype
                break
            else: 
                print("You have entered an invalid archetype. Please try again")
        occupations = classes[archetype]["Occupations"] 
        print("\n".join(occupations)) 

        while True:
            occupation = input()
            if occupation in occupations:
                player["Occupation"] = occupation
                break
            else: 
                print("You have entered an invalid occupation. Please try again")

    elif dict == races:
        race_list = "\n".join(races.keys())
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

    player["Boons"] = races[race]['Boon']
    player["Burdens"] = races[race]['Burden']
    player['Monstrous Traits'] = races[race]['Monstrous Trait']
                
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
    with open(f'{shorten(player["Archetype"].key)}', 'r') as f:
        print(f.read())

    while xp > 0:
        ab_pick = input("\nPlease select an ability: ")
        if ab_pick == '':
            print("Moving on.")
            break
        elif find_word(f'{shorten(player["Archetype"].key)}', ab_pick) and ab_pick not in player["Abilities"]:
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

        if player["Archetype"].key == "Mystic":
            print("\nWelcome to the special Mystic power section, each is worth 10 xp. \nUnless you are are a 'Self-Taught Mystic' you will be forced to stick with your occupations powers.")   
            match player["Archetype"]["Occupation"]:
                case "Theurgy":
                    read_till_break("mys_ab.txt", 22)
                case "Sorcerer":
                    read_till_break("mys_ab.txt", 22)
                case "Clan Witch":
                    read_till_break('mys_ab.txt', 53)
                case "Ordo Magica Wizard":
                    read_till_break('mys_ab.txt', 73)
                case "Self-Taught Mystic":
                    read_till_break("mys_ab.txt", 22)
                    read_till_break("mys_ab.txt", 22)
                    read_till_break('mys_ab.txt', 53)
                    read_till_break('mys_ab.txt', 73)

        while xp > 0:
            pow_pick = input("\nPlease select a power: ")
            if pow_pick == '':
                print("Moving on.")
                break
            elif find_word(f'{shorten(player["Archetype"].key)}', pow_pick) and pow_pick not in player["Abilities"]:
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

player = {"Corruption":0}

def __main__():
    print('''Welcome to the Symbaroum Character Creator!
         Using this program you can easily create a character for any session and any table. 
         Though do keep in mind: while most general character bits are included here,
         you will still need the core rulebook should you wish for your character to work mechanically.
         That being said, you'll be ready to go in no time at all. Have fun!''')
    
    print("\nFirst lets select your race, shall we?")
    pick(races)
    print("And now for class")
    pick(classes)
    print(f"Lets breifly go over what you have so far: {player} \nOnwards we go: attributes and armor coming up!")
    stuff = assign_stat()
    attributes = stuff[0]
    armor = stuff[1].capitalize
    print(f'Phew, almost done. All we have left to do is traits and abilities. Choose wisely!')
    xp = spend_xp()
    print("Now that we're done, we'll compile all you're info into a file")
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
    write_to_file(text)


__main__()


