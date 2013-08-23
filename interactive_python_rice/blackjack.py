# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        result = 'Hand contains'
        for card in self.hand:
            result += ' ' + card.get_suit() + card.get_rank() 
        return result
        
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        aces = 0
        hand_value = 0
        for card in self.hand:
            card_value = VALUES[card.get_rank()]
            if(card_value == 1):
                aces +=1
            hand_value += card_value
        if aces == 0:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
        
    def draw(self, canvas, pos):
        count = 0
        X=0
        for card in self.hand:
            if (in_play) and (self == dealer_hand) and (count == 0):
                count = 1
                card_loc = (CARD_BACK_CENTER[0], 
                            CARD_BACK_CENTER[1])
                X += CARD_BACK_CENTER[0] + pos[0] + 10
                Y = CARD_BACK_CENTER[1] + pos[1]            
                canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [X,Y], CARD_BACK_SIZE)
            else:
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(card.rank), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(card.suit))
                X += CARD_CENTER[0] + pos[0] + 10
                Y = CARD_CENTER[1] + pos[1]            
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [X,Y], CARD_SIZE)
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        init_list = [(s,r) for s in SUITS for r in RANKS]
        for tup in init_list:
            self.cards.append(Card(tup[0],tup[1]))

    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck
        random.shuffle(self.cards)
        
    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
    def __str__(self):
        # return a string representing the deck
        result = 'Deck contains'
        for card in self.cards:
            result += ' ' + card.get_suit() + card.get_rank()
        return result


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer_hand, player_hand, score

    if(in_play):
        score -=1
        outcome = "Player loses, game was in progress"
    else:
        outcome = ""
    # global deck 
    deck = Deck()

    # your code goes here
    deck.shuffle()
    
    # give 2 cards to dealer
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
        
    # give 2 cards to player
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    in_play = True

def hit():
    global deck, player_hand, in_play, score, outcome
    # if the hand is in play, hit the player
    if in_play and player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())
    else:
        outcome = "You have already busted, Dealer won!"
        return 
    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21:
        outcome = "You have busted, Dealer wins!"
        score -=1
        in_play = False
        
def stand():
    global deck, player_hand, dealer_hand, in_play, score, outcome
    
    if in_play == False:
        return
    
    in_play = False
    if player_hand.get_value() > 21:
        outcome = "You have already busted, Dealer won!"
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())

    # assign a message to outcome, update in_play and score
    if dealer_hand.get_value() > 21:
        outcome = "Dealer has busted, You win!"
        score +=1
    else:
        if player_hand.get_value() <= dealer_hand.get_value():
            outcome = "Dealer wins!"
            score -=1
        else:
            outcome = "Player wins!"
            score +=1

           
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, score, dealer_hand, player_hand, start
    start = False
    card = Card("S", "A")
    canvas.draw_text('Blackjack             Score: ' + str(score), [250,40], 30, "Red")
    if outcome != '':
        canvas.draw_text('Outcome: ' + outcome, [100,400], 24, "Black")
    canvas.draw_text("DEALER CARDS", [30,80], 24, "Black")
    if in_play:
        canvas.draw_text("PLAYER CARDS   Hit or Stand?", [30,230], 24, "Black")
    else:
        canvas.draw_text("PLAYER CARDS   New deal?", [30,230], 24, "Black")
        

    dealer_hand.draw(canvas, [30,100])
    player_hand.draw(canvas, [30,250])
    

##  init -  start the deal        
deal()        
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric
