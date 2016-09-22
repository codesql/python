# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """Function converting name to number"""
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else: 
        return name + " is unknown. Please try again"
    
def number_to_name(num):
    """Function to convert number to name"""
    if num == 0:
        return "rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "lizard"
    elif num == 4:
        return "scissors"
    else :
        return str(num) + " is not within the range of 0 to 4 range. Please try again. "

def rpsls(player_choice): 
    print ''
    print "Player chooses " + player_choice
    comp_number = random.randrange(0,4)
    print "Computer chooses " + number_to_name(comp_number)
    player_choice_num = name_to_number(player_choice)
    game_diff= (player_choice_num - comp_number) % 5
    if game_diff == 0:
        print 'Player and computer tie!'
    elif game_diff in [1,2]:
        print 'Player wins!'
    else:
        print 'Computer wins!'
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


