##           A Simple Text Adventure
##                  Version 0.1
##
##      Author: SheyMouse - June 2012
##
##  Exercise 36 from Learn Python the Hard Way by Z. A.Shaw
##              http://learnpythonthehardway.org
##
##  A simple text adventure which takes a player linearly through a set of
##  rooms.
##  Each room has an obstacle to get past, with one solution, one failure to
##  take you back to the beginning, and a second fail to kill you.
##
##  This looks like a "My first game" adventure. That's because it is. Do not
##  expect Zork on the first attempt.
##
################################################################################

## TODO LIST - Global list which I would like to do in the future
##
## X Make a single runction for the raw input prompt and call that each time
## - Fix the calling of the prompt function. It kind of works, but breaks the
##   game somehow. Find out why
## - Write a function to look for "open door" in phrase. Then call that.
## X Find out how to call the exit_game function and have the game exit properly
## - Make the open door phrase smarter so it can handle any formatted string
##   containing the letters open door
## - Insead of dog_moved, dwarf_moved, etc. could I make a general it_moved
##   function which is set to false at the beginning of a room?
##
################################################################################

#Import quit
from sys import exit

# Prompt - put the raw input prompt wherever I need it
##- calling prompt kind of works, but breaks the game somehow. Find out why
##def prompt():
##    prompt = raw_input("> ")

# Room 1 - Intro room
def start():
    print "You are in a dimly lit room."
    print "There is a door in front of you."
    print "An inscription reads \"Welcome to my incredibly complicated maze\""
    print "Type \"Open door\" if you dare!\n"
    
    next = raw_input("> ")
    
    if next == "open door" or "Open door":
        dog_room()
    else:
        dead("You cannot follow a simple instruction!")

# Room 2 - Dog gnawing on bone room
def dog_room():
#TODO - Add some intro text
    print "You are in the dog room"

    dog_moved = False

    while True:
        next = raw_input("> ")
        
        if next == "call dog":
            print "The dog bounds over to you, knocks you flat, and unconcious"
            start()
        elif next == "taunt dog":
            dead("Your excessive waving annoyed the dog and he attacked you.")
        elif next == "take bone":
            #tease dog
            # throw bone
            print "DEBUG TEXT - Dog moved"
            dog_moved = True
        elif next == ("open door" or "Open door") and dog_moved:
            dwarf_room()
        elif next != ("open door" or "Open door") and dog_moved:
            dead("Why did you have to go and say that")
        elif next == "exit":            
            exit_game()
        else:
            dead("You typed something I don't understand")
        
# Room 3 - Dwarf room
def dwarf_room():
#TODO - Add some intro text about being stared up
    print "You are in the dwarf room"

    dragon_moved = False
    
    while True:
        next = raw_input("> ")

        if "talk" in next:
            print "You try to reason with the dwarf."
            print "Unfortunately, your drarfish is very rusty and you insult her."
            print "She walks over and smacks you in the head with the side of her axe."
            print "As you lose conciousness you think to yourself how lucky you are that"
            print "that she used the flat side and not the sharp side"
            start()
        elif "push" in next:
            dead("Yeah, not a good idea pushing someone half your size around.")
        elif "axe" in next:
            # take axe
            # dwarf upset and runs away
            print "DEBUG TEXT - Dwarf moved"
            dragon_moved = True
        elif next == ("open door" or "Open door") and dragon_moved:
            dragon_room()
        elif next != ("open door" or "Open door") and dragon_moved:
            dead("Why did you have to go and say that")            
        elif next == "exit":            
            exit_game()
        else:
            dead("You typed something I don't understand")            
            
# Room 4 - Dragon room
def dragon_room():
# TODO - Intro text. Dragon asleep. On gold. How will you move it.
    print "You are in the dragon room"

    dragon_moved = False
    while False:
        next = raw_input("> ")

        if next == "noise":
            # dragon annoyed
            # dragon slaps you into unconciousness
            # you will have visions of those claws coming at you for ever
            start()
        elif "slap" in next:
            dead("The dragon casually send out a flame whch toasts you alive!")
        elif "axe" in next:
            #dragon sees axe
            #dragon gets scared
            #dragon runs away
            print "DEBUG - Dragon has moved"
            dragon_moved
        elif next == "open door":
            freedom()
        elif next == "gold open door":
            freedom()
        elif next == "exit":            
            exit_game()
        else:
            dead("You typed something I don't understand")
            
# Room 5 - Exit room
def freedom():
    print "You are free!"

    exit_game()
    
# Dead - Tell person they are dead and quit game
def dead(cause):
    print cause, "\nNow you are dead"
    exit(0)
    
# Exit - Quit game
def exit_game():
    print "Thanks for playing!\n"
    exit(0)

#Start - Calls the start function
start()

# Hint - Brings up some ideas to help the user out
# Cheat - Brings up solution to room


