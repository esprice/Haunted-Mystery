import random





#Owl talk
 
def answer_owl():
    print('"Read my beak, get out!"')
    print("Oh, my. What a nasty bird!")
    print("Maybe it's best you leave. As owls go, he's quite foul!")
    choice = input("What would you like to do, leave or harass owl?").lower()
    
    if choice == "leave":
        run_hallway()
    elif choice == "harass owl" or "insult owl" or "owl" or "stay" or "remain in ballroom" or "remain":
        answer_owl2()

def answer_owl2():
    answers = ["Your memory is as short as a hummingbird's attention span", 
               "You're as sneaky as a raccoon in a trash can. Get out!", 
               "You're as dense as a fog bank", 
               "Seriously, I know a flock of ravens who'd love to visit your car, and I'm not afraid to call them."]
    random_option = random.choice(answers)
    print(random_option)
    answer_owl2()
    choice = input("What a birdbrain! Perhaps it's best to leave him be. Would you like to explore the hallway more or return to the lobby?")

    if choice == "hallway" or "return to hallway" or "leave":
        run_hallway()
    elif choice == "lobby" or "return to lobby" or "front desk":
        lobby()
def answer_owl_snarky():
    #When the owl is being a wise-ass
    answers = ["Hoot hoot, humans are so predictable. They think they're hunting for clues, but really they're just chasing their own tails.",
                "Wisdom is not about seeing everything, but about seeing beyond the obvious. Look again, detectives.",
                "The truth is hidden in plain sight, but you need eyes that can see in the dark.",
                "Don't be fooled by the ghosts of the past. The real monsters are the ones still breathing.",
                "A murder in a haunted hotel? How trite. But I suppose it's a good thing I'm here to keep things interesting.",
                "You're looking for motives? Ha! Humans are always motivated by the same things: fear, greed, and the desire to fly (but that's just me).",
                "The dead can't speak, but the walls can. Listen to the whispers, detectives.",
                "I've seen it all from my perch. The living are just as dead as the ghosts they fear.",
                "Uncover the truth, but be warned: it may be more terrifying than the ghosts that haunt these halls."]
    random_option = random.choice(answers)
    print(random_option)
    answer_owl_snarky()
