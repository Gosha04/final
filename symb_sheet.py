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

def stat_gen():
    while True:
        stat_list = []
        for i in range(8):
            stat_list.append(dice(3,6))
        for i in stat_list:
            if i < 5 or i > 15:
                stat_list.pop(i)
                stat_list.insert(i, dice(3,6))
                i = i-1
        print (stat_list)
        reset = input("If you are unhappy with these values please enter (y/n)")
        match reset:
            case "y":
                continue
            case "n":
                break
    return stat_list
            
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