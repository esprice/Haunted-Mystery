import random

def balthazar_meet():
    print("Well, well, well, what do we have here? A new plaything for my amusement?")
    print("You look lost. Need a guide through this maze of shadows? Too bad, I'm not in the helping mood.")
    
def balthazar_clues1():
    answers = ["Poking your nose where it doesn't belong, are we? Be careful, curiosity killed the cat. And you... are not a cat.", 
               "Looking for clues? Ha! You'll only find misery and despair in this place.", 
               "You're as dense as a fog bank", 
               "Oh, did I just knock over that vase? My, my, how clumsy of me. Better clean up the mess before someone trips.",
               "Purr-haps you should look elsewhere... or not at all.", "Meow-ve along, nothing to see here.", "The clues are hidden in plain sight... but you're too blind to see.", "You're getting close... to falling into my trap.", "Meow-aybe you should just give up now... while you still can."]
    random_option = random.choice(answers)
    print(random_option)
    balthazar_clues1()
    choice = input()

def balthazar_clues2():
    #blocking clues
    answers = ["Trying to get past me? Good luck with that. I don't move for anyone, especially nosy little clerks.",
	"This path is closed. Find another way, if you can.",
	"Oh, you want to go through here? What's the magic word? Too bad, it doesn't exist."]
    random_option = random.choice(answers)
    print(random_option)
    balthazar_clues2()
    choice = input() 

def balthazar_clues3():
    #Congrats
    answers = ["So, you've made it this far. Impressive, but futile. The end is near, and it's not what you expect.",
	"You think solving this mystery will bring peace? Ha! This place is cursed, and so are you now.",
	"Go ahead, unveil the truth. But remember, some secrets are better left buried."]    
    random_option = random.choice(answers)
    print(random_option)
    balthazar_clues3()
    choice = input() 

def balthazar_riddle_key():
    #To get the first key to room 201
    print("I have keys but can't open locks. You'll be locked in a room of confusion!")
    choice = input("What is your answer?").lower()
    
    if choice in ["keyboard" or "Keyboard" or "computer keyboard" or "computer keys"]:
        give_first_key()
    else:
        print("It's a simple riddle, human. Try again.")
        balthazar_riddle_key()

def give_first_key():
    # first door opens 
    print("The door opens with a loud creek. Someone really aught to lubricate the hinges.")
    print("Within the room, there are several pieces of furniture, including a bed, a dresser, and an old desk.")
    print("There is a unusual little wooden box sitting on the desk. Would you like to look closer or investigate the dresser?" )
    choice = input("Check the DESK or investigate the DRESSER?").lower()
    
    if choice == "Desk" or "the desk" or "check the desk":
        checkDesk()
    elif choice == "Dresser" or "the dresser" or "check the dresser":
        check_dresser()
    else:
        print("Let's try this again.")
        give_first_key()
def check_dresser():
    pass
def checkDesk():
    pass