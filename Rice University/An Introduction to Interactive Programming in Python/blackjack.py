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
outcome = "Hit or Stand?"
outcome_color = "Yellow"
alert_message = ""
score = 0
time = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

player_hand = None
dealer_hand = None
deck = None

# define card class
class Card:
    def __init__(self, suit, rank, face_up = True):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            self.face_up = face_up
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
        card_loc = ()
        if self.face_up:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            card_loc = (CARD_BACK_SIZE[0] / 2, CARD_BACK_SIZE[1] / 2)
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        return str([str(card) for card in self.cards])
    
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        cards = [card for card in self.cards if card.face_up]
        not_aces = [card for card in cards if card.get_rank() != 'A']
        aces = [card for card in cards if card.get_rank() == 'A']
        value = sum(VALUES[card.get_rank()] for card in not_aces)
        
        current_value = value
        for ace in aces: value += 11 if value + 11 <= 21 else 1
        if value > 21:
            value = current_value
            for ace in aces: value += 1
        return value
        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += 80
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop(0)
        return card
    
    def __str__(self):
        # return a string representing the deck
        return "Deck Contains: " + str([str(card) for card in self.cards])

#define event handlers for buttons
def deal():
    global outcome, outcome_color, in_play, deck, player_hand
    global dealer_hand, alert_message, time, score
    
    if in_play:
        time = 0
        alert_message = "Deal during match -1 point!"
        score -= 1
        timer.start()
    
    
    # your code goes here   
    in_play = True
    outcome_color = "Yellow"
    outcome = "Hit or Stand?"
    
    # initialize deck
    deck = Deck()
    deck.shuffle()  
        
    # initialize player
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    # initialize dealer
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.cards[0].face_up = False

def hit():
    global in_play, outcome, outcome_color, score
    
    # if the hand is in play, hit the player
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
        
        if player_hand.get_value() > 21:
            outcome_color = "Red"
            outcome = "You have busted! New deal?"
            score -= 1
            in_play = False
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, outcome, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:    
        dealer_hand.cards[0].face_up = True
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())        
            
        # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() < player_hand.get_value() or dealer_hand.get_value() > 21:
            outcome = "You win! New deal?"
            score += 1
        else:
            outcome = "You lose... New deal?"
            score -= 1
        in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    player_hand.draw(canvas, [30, 450])
    dealer_hand.draw(canvas, [30, 250])
    
    canvas.draw_text("Blackjack", [170, 50], 50, "White", "monospace")
    
    canvas.draw_text(alert_message , [60, 95], 30, "Red", "monospace")
    canvas.draw_text("Score: " + str(score), [30, 140], 35, "White", "monospace")
    canvas.draw_text(outcome, [30,190], 35, outcome_color, "monospace")
    
    canvas.draw_text("Player", [30, 440], 30, "Black", "monospace")
    canvas.draw_text("Dealer", [30, 240], 30, "Black", "monospace")
    
    canvas.draw_text("Player: " + str(player_hand.get_value()), [520, 570], 12, "White", "monospace")
    canvas.draw_text("Dealer: "+ str(dealer_hand.get_value()), [520, 590], 12, "White", "monospace")
    
def show_message():
    global alert_message, time
    time += 1
    
    # an alert message if the player deals during the match
    if time % 2 != 0:
        alert_message = ""
    else:
        alert_message = "Deal during match -1 point!"
        
    if time > 3:
        alert_message = ""
        timer.stop()
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# timer for messages
timer = simplegui.create_timer(1000, show_message)

# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
