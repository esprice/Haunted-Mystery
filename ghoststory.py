import random
from random import choice
from turtle import *
import pygame
import owltalk
import second_floor
import third_floor
import roof
import doll
import albert
import guests_hotel
import time

pygame.init()

# Set up the display
window_width = 800
window_height = 600
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Fogcrest Hotel Adventure')

# Load the background image
bg_image = pygame.image.load('images/lobby1.jpg')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Define font
font = pygame.font.SysFont(None, 36)

def draw_dialog(surface, rect, text):
    pygame.draw.rect(surface, BLACK, rect)
    pygame.draw.rect(surface, WHITE, rect, 2)
    
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(topleft=(rect.x + 10, rect.y + 10))
    surface.blit(text_surf, text_rect)

def get_text_input(prompt):
    input_box = pygame.Rect(50, 500, 700, 32)
    user_text = ''
    active = True
    clock = pygame.time.Clock()

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_text
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        
        game_display.fill((30, 30, 30))
        game_display.blit(bg_image, (0, 0))
        draw_dialog(game_display, pygame.Rect(50, 450, 700, 100), prompt)
        
        txt_surface = font.render(user_text, True, WHITE)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        game_display.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(game_display, WHITE, input_box, 2)
        
        pygame.display.flip()
        clock.tick(30)

def display_message(lines):
    y_offset = 50
    for line in lines:
        text_surf = font.render(line, True, WHITE)
        game_display.blit(text_surf, (50, y_offset))
        y_offset += 40

def start_adventure():
    adventure_text = [
        "Welcome to Fogcrest Hotel!",
        "You find yourself standing in the middle of a grand lobby.",
        "Above you is a beautiful crystal chandelier.",
        "Then you notice something swirling around the lights.",
        "IT'S a GHOST!",
        "Do you want to run left, right, or try to talk to the ghost?"
    ]
    
    while True:
        game_display.fill((30, 30, 30))
        game_display.blit(bg_image, (0, 0))
        display_message(adventure_text)
        pygame.display.flip()
        
        choice = get_text_input("What would you like to do? Turn left, turn right, or talk to the ghost? ").lower()
        
        if choice in ["left", "turn left", "go left"]:
            left_path()
            break
        elif choice in ["right", "turn right", "go right"]:
            right_path()
            break
        elif choice in ["talk to the ghost", "talk to ghost", "ghost"]:
            talk_to_ghost()
            break
        else:
            adventure_text.append("You're new here, I get it. This old spooky hotel can be a little disconcerting.")
            adventure_text.append("Rest assured, there's nothing to be worried about. Let's try this again.")

def left_path():
    print("You chose to go left down a long hallway leading to the back of the hotel.")
    print("After walking for a while, you encounter eerie music coming from behind a stained glass door.")
    print("Do you want to walk through the door or turn back?")
    
    choice = input("Will you choose to open the door or turn back:  ").lower()
    
    if choice in ["door", "open door", "open", "enter"]:
        stained_glass_door()
    elif choice == "turn back":
        lobby()
    else:
        print("You ran into a wall. How about trying again?")
        left_path()
        
def stained_glass_door():
    print("The door opens with a loud CREEEEEEEEK. Inside, the room is pitch dark.")
    print("From the darkness you see two glowing yellow eyes.")
    print("More and more eyes begin to appear. Then a voice calls out...")
    print("Whoooooo?")
    
    choice = input("Do you run away or try to find a light switch?").lower()
    
    if choice in ["run away", "run"]:
        run_hallway()
    elif choice in ["light", "light switch", "turn on the light"]:
        ballroom_light()
    elif choice in ["lobby", "check in"]:
        lobby()
    else:
        print("That scared, hum? How about you take a step back out into the hallway and catch your breath?")
        stained_glass_door()
    
def run_hallway():
    print("You return to the hallway and immediately stumble over a strange old doll.")
    print("The doll looks up at you with glowing red eyes and asks, 'mama?'")
    choice = input("Do you pick up the doll or walk away, hoping that it won't follow you?").lower()
    
    if choice in ["walk away", "run away", "run", "continue", "ignore"]:
        doll_no_talk()
    elif choice in ["talk", "talk to doll", "doll", "kick doll", "kick", "pick up doll"]:
        doll_yes_talk()
    else:
        print("I guess you're not good with children. It's for the best, anyway. You step over the doll and hurry back towards the lobby.")
        lobby()
        
def ballroom_light():
    print("You switch on the lights, illuminating a grand ballroom.")
    print("In the middle of the ballroom, you see a chandelier, similar to the one in the lobby.")
    print("Perched near the top of the chandelier is a hand-sized white owl.")
    print('"Whooo? the owl hoots. The sight of the owl causes you to giggle"')
    print('"What do you want already?" the owl calls out')
    choice = input("Do you answer the owl or turn off the light?").lower()

def right_path():
    print("You come to the check-in counter where a strange ghostly white man in a hotel uniform greets you.")
    print("The name tag on his uniform reads: Albert.")
    print("Do you want to check in to the hotel, have a seat in the lobby, or continue to the lobby doors?")
    
    choice = input("Would you like a room for the night, to take a seat, or to continue exploring?").lower()
    
    if choice in ["check in", "check-in", "front counter", "talk to Albert", "room", "room for the night"]:
        albert_check_in()
    elif choice in ["sit", "take a seat", "sit down"]:
        sit()
    elif choice in ["continue", "lobby doors", "walk away", "lobby"]:
        lobby()
    else:
        print("I know this old hotel can be confusing. Don't wander off too far.")
        right_path()

def albert_check_in():
    print(f"Goooood evening, {name}. Welcome to the Juniper. How can I assist you?")
    choice = input("Would you like a room for the night or would you like to explore more?").lower()
    
    if choice in ["I want to check in", "check in", "room", "room key", "a room, please", "a room"]:
        hotel_room()
    elif choice in ["look around", "look around more", "explore", "wonder", "explore more", "explore hotel"]:
        lobby()
    else:
        print("Not sure where you want to go? Why not play it safe and explore the lobby?")
        lobby()
    
def talk_to_ghost():
    print("The ghost stops dead in his tracks and looks down at you.")
    print("The ghost says in a deep, groaning voice: Helllllllo!")
    print("Welcome to the Juniper. My name is Gossamer.")
        
    name = input("What is your name?   ")
    print(f"Nice to meet you {name}. Feel free to explore the hotel.")
    print("I'm sure you'll meet many other of my phantom friends here.")
    print("Don't be alarmed. We're all dying to meet you.")
    print("You look tired. I suggest booking a room for the night.")
    print("Talk to Albert at the front desk. He'll find you a room for the night.")
        
    choice = input("Type 'talk to Albert' or 'explore':  ").lower()
    
    if choice in ["talk to Albert", "check-in", "check in", "front desk"]:
        right_path()
    elif choice in ["explore", "look around", "wander around", "wander", "see what's around", "walk around"]:
        lobby()
    else: 
        print("You stumble over luggage in the middle of the walkway. Unfortunately, you're not a ghost... yet, and stumble over the luggage. Try again")
        talk_to_ghost()

def lobby():
    print("You look around the lobby. There is a beautiful antique burgundy sofa near the front windows.")
    print("There's a black baby grand piano in the corner of the lobby playing music.")
    choice = input("Why not relax on the sofa and listen to the music? Or would you rather explore more? relax or explore?").lower()

    if choice in ["relax", "chill"]:
        relax()
    elif choice in ["explore", "look around", "wander around", "wander", "see what's around", "walk around"]:
        pub1()
    else:
        print("Maybe you're already too relaxed? Let's try this again. Choose relax or explore. ")
        lobby()
        
def relax():
    print("You take a seat on the sofa. The velvet is soft and smells of cheese puffs.")
    print("You glance over at the piano and realize it's playing on its own.")
    print("Is it another ghost or a fancy player piano?")
    choice = input("You either say 'Hello' or quickly 'leave'.").lower()
    
    if choice in ["hello", "hi", "anyone there?", "are you a ghost?"]:
        hello()
    elif choice == "leave":
        pub1()
    else:
        print("That's an interesting choice, however not one that's available.")
        relax()

def hello():
    print("You meekly whisper hello towards the piano, but hear nothing.")
    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image at position (0, 0)
    game_display.blit(bg_image, (0, 0))

    # Update the display
    pygame.display.update()

pygame.quit()

# Start the adventure
start_adventure()

   
