# implementation of card game - Memory

import simplegui
import random
import math


CARD_POS = { 1 : [(0, 0), (0, 100), (50, 100),(50,0)],
            2 : [(50, 0), (50, 100), (100, 100),(100,0)],
            3 : [(100, 0), (100, 100), (150, 100),(150,0)],
            4 : [(150, 0), (150, 100), (200, 100),(200,0)],
            5 : [(200, 0), (200, 100), (250, 100),(250,0)],
            6 : [(250, 0), (250, 100), (300, 100),(300,0)],
            7 : [(300, 0), (300, 100), (350, 100),(350,0)],
            8 : [(350, 0), (350, 100), (400, 100),(400,0)],
            9 : [(400, 0), (400, 100), (450, 100),(450,0)],
            10 : [(450, 0), (450, 100), (500, 100),(500,0)],
            11 : [(500, 0), (500, 100), (550, 100),(550,0)],
            12 : [(550, 0), (550, 100), (600, 100),(600,0)],
            13 : [(600, 0), (600, 100), (650, 100),(650,0)],
            14 : [(650, 0), (650, 100), (700, 100),(700,0)],
            15 : [(700, 0), (700, 100), (750, 100),(750,0)],
            16 : [(750, 0), (750, 100), (800, 100),(800,0)],
            }


# helper function to initialize globals
def init():
    global state, mem_deck, exposed,last_2_cards, tries
    state = 0
    tries = 0
    mem_deck= range(8)
    mem_deck.extend(mem_deck)
    random.shuffle(mem_deck)
    exposed = [False] * 16
    last_2_cards = [None,None]
     
# define event handlers
def click(pos):
    global CARD_POS, exposed, mem_deck, last_2_cards, state, tries
    # add game state logic here
    for key, val in CARD_POS.items():
        if(not exposed[key-1]):
            if(pos[0]  < val[3][0] and pos[0] > val[0][0] and pos[1] < val[2][1] and pos[1] > val[0][1]):
                if state == 0:
                    state = 1
                    exposed[key-1] = True    
                    last_2_cards[0] = key-1
                    tries = tries + 1
                    print key-1
                elif state == 1:
                    state = 2
                    exposed[key-1] = True    
                    last_2_cards[1] = key-1
                    print key-1
                else:
                    tries = tries + 1
                    if(mem_deck[last_2_cards[0]] == mem_deck[last_2_cards[1]]):
                        last_2_cards = [None,None]
                    else:
                        exposed[last_2_cards[0]] = False
                        exposed[last_2_cards[1]] = False
                    last_2_cards = [key-1,None]    
                    state = 1    
                    exposed[key-1] = True    
                
        else:
            print key-1
            print "Already exposed, ignore"            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global CARD_POS,exposed,mem_deck, label,  tries
    x = 25
    label.set_text("Moves = " + str(tries))
    for key, val in CARD_POS.items():
        if exposed[key-1]:
            canvas.draw_text(str(mem_deck[key-1]),(x + ((key-1) * 50),50), 12, "Red")
        else:	
            canvas.draw_polygon(CARD_POS[key], 2, "White", "Green")

            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
