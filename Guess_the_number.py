# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

x =0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    x = random.randrange(1,100)
    return x
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     =
    x = random.randrange(1,1000)
    return x
    

    
def input_guess(guess):
    # main game logic goes here	
    
#create window(s)
    f = simplegui.create_frame("Guess the number " , 200, 200)

#create control elements for window
    f.add_button("Range is [0, 100]", range100, 200)
    f.add_button("Range is [0, 1000]", range1000, 200)
    f.add_put(" Enter a guess" , get_input, 200)

# create frame


# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
