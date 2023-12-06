import random
import math

# 2 or 3 Traits
# 2 Novice Traits, 1 Adept
 
def stats_to_file(line):
    with open ("stats.txt", "a") as f:
        f.write(line + "\n")
 
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

# def display_ab(ability):
#     # TODO Error handling for strings and later list
#     ability = ability + ".txt"
#     with open (ability, "r") as f:
#         desc = f.read()
#     return desc


# def dice(num_dice, die_type):
#     result = 0
#     for i in range(num_dice):
#         result += random.randint(1, die_type)
#     return result

# def stat_gen():
#     while True:
#         stat_array = []
#         check = []
#         for i in range(8):
#             stat_array.append(dice(3, 6))
#         for stat in stat_array:
#             if stat < 5 or stat > 15:
#                 stat_array[stat_array.index(stat)] = dice(3, 6)
#             elif stat == 15:
#                 check.append(stat)
#                 if len(check) > 1:
#                     print("Too many invalid values, rerolling")
#                     continue
#         print(f'Here is your stat array: \n{stat_array}')
#         user = input("Would you like to reroll? (y/n)")
#         match user:
#             case 'y':
#                 continue
#             case 'n':
#                 break
#             case _:
#                print("Unknown option selected. We will continue")
#     return stat_array

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

stuff = assign_stat()
attributes = stuff[0]
armor = stuff[1]
print(attributes)    

def pick(dict):
    if dict == classes:
        while True:
            archetype = input("""Here you will select your archetype
              1. Warrior
              2. Rogue
              3. Hunter
              4. Mystic""")
            if archetype in classes.keys():
                player["Archetype"] = archetype
                break
            else: 
                print("You have entered an invalid archetype. Please try again")
        occupations = classes[archetype]["Archetypes"] 
        print("\n".join(occupations)) 
        while True:
            occupation = input(f"{classes[archetype]}")
            if occupation in occupations:
                player["Archetype"]["Occupation"] = occupation
                break
            else: 
                print("You have entered an invalid occupation. Please try again")


def spend_xp():
    xp = 50
    print(f'''
    In the following section you will be able to spend 50 xp on various traits and abilities.
    Each boon, ability, and mystic power is worth 10 xp at its base level.
    You will also be able to purchase burdens which will provide 5 xp per burden. 
          
    Now we'll remind you as to your traits and attributes below:
    Attributes: {attributes}
    Armor: {armor}
    Boons: #TODO
''')

classes = {
    "Warrior": {
        "Archetypes": ["Berserker", "Duelist", "Captain", "Knight", "Sellsword", "Tattooed Warrior", "Weapon Master"],
        "Abilities": "war_ab.txt"
    },
    "Mystic": {
        "Archetypes": ["Clan Witch", "Ordo Magica Wizard", "Self-Taught Mystic", "Sorcerer", "Theurg of Prios"],
        "Abilities": "mys_ab.txt"
    },
    "Rogue": {
        "Archetypes": ["Charlatan", "Guild Thief", "Former Cultist", "Sapper", "Thug", "Treasure-Hunter"],
        "Abilities": "rog_ab.txt"
    },
    "Hunter": {
        "Archetypes": ["Bounty Hunter", "Guide", "Monster Hunter", "Scout", "Ranger", "Trailblazer", "Witchhunter"],
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

player = {}