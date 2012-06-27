##           A Simple Text Adventure
##                  Version 0.2
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

## TODO LIST - Global list of tasks (when I remember to update them!)
##
##  - Add a list of possible solutions or phrases that will lead to traps
##  - Fix the calling of the prompt function. It kind of works, but breaks the
##   game somehow. Find out why
##  - Write a function to look for "open door" in phrase. Then call that.
##  - Make the open door phrase smarter so it can handle any formatted string
##   containing the letters open door
##  - Insead of dog_moved, dwarf_moved, etc. could I make a general it_moved
##   function which is set to false at the beginning of a room?
##  - Place all text in another file and call what is needed. I think this will
##    make it cleaner.
##  - Indent text by four characters to make it easier to read on screen
##  - Trailing new line on all blocks of text
##  - Add pauses to some of the text for a pause effect. Mainly because I can.
##  - Having "if axe in" keyword check in two rooms produces a bug since the
##    code reads top-down. Perhaps add an axe_got boolean in dwarf room to 
##    make the program read the second "axe" in the dragon room
##  X Make a single runction for the raw input prompt and call that each time
##  X Find out how to call the exit_game function and have the game exit properly
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
    print "\n\tYou wake in a dimly lit room."
    print "\tThere is a door in front of you."
    print "\tAn inscription reads \"Welcome to my incredibly complicated maze\""
    print "\tType \"Open door\" if you dare!\n"
    
    next = raw_input("> ")

#BUG - Typing gibberish no longer leads to death? Why?
    
    if next == "open" or "Open":
        dog_room()
    elif "exit" in next:            
        exit_game()
    else:
        dead("You cannot follow a simple instruction!")

# Room 2 - Dog gnawing on bone room
def dog_room():

    print "\n\tYou enter the next room. The door locks behind you."
    print "\tYou see a large dog in front of another door."
    print "\tHe is gnawing on a bone."
    print "\tThe only way through that door is to move him first."
    print "\tBut how?\n"

    dog_moved = False

    while True:
        next = raw_input("> ")
        
        if next == "call dog":
            print "The dog bounds over to you, knocks you flat, and unconcious"
            start()
        elif next == "taunt dog":
            dead("Your excessive waving annoyed the dog and he attacked you.")
        elif next == "take bone":
            print "\n\tIn a moment of madness, you snatch the bone from the dog."
            print "\tBefore he rips you to shreds, you throw the bone and shout"
            print "\t\"Fetch!\""
            print "\tThe dog bounds eagerly after the bone.\n"
            
            dog_moved = True
        elif next == ("open door" or "Open door") and dog_moved:
            dwarf_room()
        elif next == "exit":            
            exit_game()
        else:
            dead("\t...is the wrong command.\n")
        
# Room 3 - Dwarf room
def dwarf_room():
#TODO - Add some intro text about being stared up
    print "\n\tYou look around the new room as the sounds of the slamming door"
    print "\techos behind you."
    print "\tYou see a dwarf guarding the next door."
    print "\tHe, she, er, it, is looking at you intently."
    print "\tYou get the feeling the dwarf is trying to stare you up. (dwarves"
    print "\tare not able to stare down many people; even most animals are"
    print "\tout of the question)\n"
    print "\tYou need to wipe that stare of it's face.\n"
    
    
    dwarf_moved = False
    
    while True:
        next = raw_input("> ")

        if "talk" in next:
            print "\n\tYou try to reason with the dwarf."
            print "\tUnfortunately, your drarfish is very rusty and you"
            print "\tinsult it."
            print "\tThe dwarf walks over and smacks you in the head with the
            print "\nside of the axe."
            print "\tAs you lose conciousness you think to yourself how lucky"
            print "\tyou are that the flat side and not the sharp side connected"
            print "\twith your noggin.\n"
            start()
        elif "push" in next:
            dead("Despite being half your size, pushing dwarfs around is never a good idea.")
        elif "take axe" in next:
            print "\n\tEmboldened by your perfomance in the last room, you"
            print "\tsnatch the axe from the grasp of the dwarf."
            print "\tThis upsets the dwarf."
            print "\tA lot."
            print "\tYou feel like a bully, but only for the moment."
            print "\tBecause, the door is clear. And you have an axe."
            print "\t..." # insert delay here
            print "\tNo, you are not going to do \"a Shining\" on the door." 
            
            dwarf_moved = True
        elif next == ("open door" or "Open door") and dwarf_moved:
            dragon_room()
        #elif next != ("open door" or "Open door") and dwarf_moved:
         #   dead("Why did you have to go and say that?")            
        elif next == "exit":            
            exit_game()
        else:
            dead("You typed something I don't understand\n")            
            
# Room 4 - Dragon room
def dragon_room():
# TODO - Intro text. Dragon asleep. On gold. How will you move it.
    print "You are in the dragon room\n"

    dragon_moved = False
    while True:
        next = raw_input("> ")

        if next == "noise":
            # dragon annoyed
            # dragon slaps you into unconciousness
            # you will have visions of those claws coming at you for ever
            start()
        elif "slap" in next:
            print "You slap the dragon"
            dead("In return, the dragon casually sends out a flame whch toasts you alive!")
        elif next == "chop":
            #dragon sees axe
            #dragon gets scared
            #dragon runs away
            print "DEBUG - Dragon has moved"
            dragon_moved
        elif next == "open door":
            freedom()
        elif next == "gold open door":
            freedom_gold()
        elif next == "exit":            
            exit_game()
        else:
            dead("\tYou typed something I don't understand\n")
            
# Room 5 - Exit room
def freedom():
    print "You are free!"

    exit_game()
def freedom_gold():
    print "You are free. And you have gold."

    exit_game()
    
# Dead - Tell person they are dead and quit game
def dead(cause):
    print cause, "Now you are dead\n"
    exit(0)
    
# Exit - Quit game
def exit_game():
    print "Thanks for playing!\n"
    exit(0)

#Start - Calls the start function
start()

# Hint - Brings up some ideas to help the user out
# Cheat - Brings up solution to room


