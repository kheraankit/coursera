
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random


# helper functions

def number_to_name(number):
    """ 
    This function accepts a 'number' as a key and
    return the corresponding value 'name'
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Unrecognized number:" + str(number)
    
def name_to_number(name):
    """ 
    This function accepts 'name' as a key and
    return the corresponding value 'number'
    """

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
        print "Unrecognized name:" + name

def print_results(winning_number,computer_name,player_name):
    """
    This function pretty prints the results 
    """
    print "Player chooses " + player_name
    print "Computer chooses " + computer_name
    
    # 0-player_wins 1-computer_wins 2-tie
    if(winning_number == 0):
        print "Player wins!"
    elif(winning_number == 1):
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    print ""
        
def rpsls(name): 
    """
    This function accepts the player's choice as a function 
    argument and generates a random choice for computer, plays
    the Rock-paper-scissors-lizard-Spock game [Player vs Comptuer] 
    and prints the results
    """
    
    # holds the results. 0-player_wins 1-computer_wins 2-tie
    winning_number = 0
    
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # compute difference of player_number and comp_number modulo five
    if(comp_number != None and player_number != None):
        
        diff_number = (comp_number - player_number) % 5
       
        if diff_number > 0  and diff_number <=2:
            winning_number = 1
        elif diff_number > 2:
            winning_number = 0
        else:
            #  difference is zero, tie between computer and player
            winning_number = 2
        
        # convert comp_number to name using number_to_name
        computer_name = number_to_name(comp_number)
        
        # print results
        print_results(winning_number,computer_name,name)
    else:
        print comp_number,player_number
        
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



