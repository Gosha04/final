import random


# Write a function that reads data the user inputs into a file

 
def stats_to_file(line):
    with open ("stats.txt", "a") as f:
        f.write(line + "\n")
 
 
def display_ab(ability):
    # TODO Error handling for strings and later list
    ability = ability + ".txt"
    ability = open(ability, "r")
    desc = ability.read()
    desc.close()
    return desc

def display_class(role):
    role = open(f"{role}.txt", "r")
    print(role.read)

def dice(num_dice, die_type):
    results = []
    for i in range(num_dice):
        results.append(random.randint(1,die_type))
    return results

print(dice(6, 20))

def assign_stat(att_list):
    stats = ["Accurate", "Cunning", "Discreet", "Persuasive", "Quick", "Resolute", "Strong", "Vigilant"]
    assigned_stats = {}
    for stat in stats:
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
    return assigned_stats


att_list = stat_gen()

def assign_stat(att_list):
    stats = ["Accurate", "Cunning", "Discreet", "Persuasive", "Quick", "Resolute", "Strong", "Vigilant"]
    for stat in stats:
        print (att_list + "\nThis is your availible array, please use them to set your attributes")
        print(f"Please set your {stat}")
        while True:
            try:
                value = int(input("Use an integer"))
                if value in att_list:
                    break
            except:
                print("You've entered a non-integer, please try again")
        


       
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