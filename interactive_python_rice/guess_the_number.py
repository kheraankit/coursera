# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random 
import simplegui
import math

# initialize global variables used in your code

no_of_retries = 0
secret_number = 0
game_type = 100 

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number, no_of_retries, game_type
    secret_number = random.randrange(0, 100)
    no_of_retries = calc_no_retries(101)
    print ""
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is ", no_of_retries
    game_type = 100

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number, no_of_retries, game_type
    secret_number = random.randrange(0, 1000)
    no_of_retries = calc_no_retries(1001)
    print ""
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is ", no_of_retries
    game_type = 1000

def calc_no_retries(no):
    """ Calcutes the no_of_retries based on min-max range  """
    return math.ceil(math.log(no,2))

def has_tries_left():
    global no_of_retries
    
    if(no_of_retries == 0):
        return False
    else:
        return True
def restart_game():
    global game_type
    
    if(game_type == 100):
        range100()
    else:
        range1000()

    
def get_input(guess):
    # main game logic goes here	
    global secret_number, no_of_retries, game_type
    no_of_retries -= 1
    print ""
    print "Guess was ", guess
    print "Number of remaining guesses is ", no_of_retries

    if guess != None and guess != "":
        guess_int = int(guess)

        if(secret_number == guess_int):
           print "Correct!"
           restart_game()
        elif(secret_number < guess_int):
            has_tries = has_tries_left()
            if(has_tries == False):
                print "You ran out of guesses. The number was ", secret_number
                restart_game()
            else:
                print "Lower!"
        else:
            has_tries = has_tries_left()
            if(has_tries == False):
                print "You ran out of guesses. The number was ", secret_number
                restart_game()
            else:
                print "Higher!"
    else:
        print "Invalid Input! Try again with valid positive integer no"
            

# Calling range100 to start the game first time a user clicks run	    
range100()   


# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements

frame.add_button("Range: 0 - 100", range100, 200)

frame.add_button("Range: 0 - 1000", range1000, 200)

frame.add_input("Enter a guess", get_input, 200)


# start frame

frame.start()

# always remember to check your completed program against the grading rubric

