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

def display_ab(ability):
    # TODO Error handling for strings and later list
    ability = ability + ".txt"
    with open (ability, "r") as f:
        desc = f.read()
    return desc

def display_class(role):
    with open (f"{role}.txt", "r") as f:
        print(f.read())

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

print(assign_stat())    

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
    "Human Ambrian" : {
        "Free Starting Boon" :["Contacts", "Privileged"],
        "Starting Burden" : None,
        "Unlocked Monstrous Trait" : None
    },
     "Human Barbarian" : {
        "Free Starting Boon" :["Contacts", "Bushcraft"],
        "Starting Burden" : "None",
        "Unlocked Monstrous Trait" : "None"
    },
    "Changeling" : {
        "Free Starting Boon" : "Long-Lived",
        "Starting Burden" : "None",
        "Unlocked Monstrous Trait" : "Shapeshift"
    },
    "Ogre" : {
        "Free Starting Boon" : "Long-Lived",
        "Starting Burden" : "Pariah",
        "Unlocked Monstrous Trait" : "Robust"
    },
    "Goblin" : {
        "Free Starting Boon" : "None",
        "Starting Burden" : ["Short-Lived", "Pariah"],
        "Unlocked Monstrous Trait" : "Survival Instinct"
    }
}