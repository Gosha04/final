import random
import math

# Write a function that reads data the user inputs into a file

 
def stats_to_file(line):
    with open ("stats.txt", "a") as f:
        f.write(line + "\n")
 
 
def display_ab(ability):
    # TODO Error handling for strings and later list
    ability = ability + ".txt"
    with open (ability, "r") as f:
        desc = f.read()
    return desc

def display_class(role):
    with open (f"{role}.txt", "r") as f:
        print(f.read())

def dice(num_dice, die_type):
    results = []
    for i in range(num_dice):
        results.append(random.randint(1, die_type))
    return results

def stat_gen():
    while True:
        stat_array = []
        check = []
        for i in range(8):
            stat_array.append(dice(3, 6))
        for stat in stat_array:
            if stat < 5 or stat > 15:
                stat_array[stat_array.index(stat)] = dice(3, 6)
            elif stat == 15:
                check.append(stat)
                if len(check) > 1:
                    print("Too many invalid values, rerolling")
                    continue
        print(f'Here is your stat array: \n{stat_array}')
        user = input("Would you like to reroll? (y/n)")
        match user:
            case 'y':
                continue
            case 'n':
                break
            case _:
               print("Unknown option selected. We will continue")
    return stat_array

def assign_stat(att_list):
    stats = ["Accurate", "Cunning", "Discreet", "Persuasive", "Quick", "Resolute", "Strong", "Vigilant"]
    derived = ["Toughness", "Pain Threshold", "Defense", "Corruption Threshold", "Abomination Threshold"]
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
                if value in att_list and stat not in assigned_stats.values():
                    assigned_stats[stat] = value
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

    der_val.append(assigned_stats['Strong'] if assigned_stats['Strong'] >= 10 else 10)
    der_val.append(math.ceil(assigned_stats['Strong']/2))
    der_val.append(assigned_stats['Quick'] - impede)
    der_val.append(math.ceil(assigned_stats['Resolute']/2))
    der_val.append(assigned_stats['Resolute'])
    for i in derived:
        assigned_stats[derived[i]] = der_val[i]

    return assigned_stats, armor
      
classes : {
    "Warrior" : {
        "Archetypes" : "warrior.txt"
    },
    "Mystic" : {
        "Archetypes" : "mystic.txt"
    },
    "Rouge" : {
        "Archetypes" :  "rouge.txt"
    },
    "Hunter" : {
        "Archetypes" : "hunter.txt"
    }
}

races = {
    "Human Ambrian" : {
        "Free Starting Boon" : "Contacts or Privileged",
        "Starting Burden" : "None",
        "Unlocked Monstrous Trait" : "None"
    },
     "Human Barbarian" : {
        "Free Starting Boon" : "Contacts or Bushcraft",
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
        "Starting Burden" : "Short-Lived, Pariah",
        "Unlocked Monstrous Trait" : "Survival Instinct"
    }
}