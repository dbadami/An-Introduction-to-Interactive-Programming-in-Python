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
player_score = 0
hit_state = False
stand_state = False
aces = []

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
        self.hand = []
        pass	
    
    def __str__(self):
        if self.hand:
            dv1 = ""
            for x in range(len(self.hand)):
                dv1+=str(self.hand[x])+" "      
        else:
            dv1 = "There are no cards in your hand!"
        return dv1	

    def add_card(self, card):
        self.hand.append(card)
        pass

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        global aces
        aces = []
        value = 0
        for card in self.hand:
            value+=VALUES[card.get_rank()]

            if card.get_rank() == 'A': #Something is wrong in this step.
                aces.append(True)
            else:
                aces.append(False)
                
        if True in aces:
            if value+10<=21:
                value+=10
            else:
                value+=0
      
        return value

    def busted(self):
        if self.get_value()>21:
            return True
        else:
            return False
        pass
                
    def draw(self, canvas,p):
        for card in self.hand:
            card.draw(canvas, [10+75*self.hand.index(card),p])    
        pass
    
# define deck class
class Deck:
    def __init__(self):
        self.card_deck = [Card(suit,rank) for suit in SUITS for rank in RANKS]
        pass	# replace with your code
    
    def __str__(self):
        if self.card_deck:
            response = ""
            for card in self.card_deck:
                response += str(card)+" "
        else:
            response = "No cards in the deck."
        return response
            
    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.card_deck)
        pass	

    def deal_card(self):
        return self.card_deck.pop()
   
#define event handlers for buttons
def deal():
    global outcome, in_play, player_score, hit_state, stand_state, aces
    
    playerhand.get_value()
    dealerhand.get_value()
    
    if in_play == True:
        if hit_state:
            player_score-=1
        
    hit_state = False
    stand_state = False
    
    playerhand.__init__()
    dealerhand.__init__()
    
    deckofcards.__init__()
    deckofcards.shuffle()
    
    for x in range(2):
        playerhand.add_card(deckofcards.deal_card())
    for x in range(2):
        dealerhand.add_card(deckofcards.deal_card())
        
    print "Player: "+str(playerhand.get_value())
    print "Dealer: "+str(dealerhand.get_value())
    print aces
     
    outcome = "Hit or stand?"
    in_play = True

def hit():
    global in_play, outcome, player_score, hit_state, stand_state
    hit_state = True
    if in_play:
        playerhand.add_card(deckofcards.deal_card())
        
        if playerhand.busted():
            in_play = False
            outcome = "You have busted!"
            player_score-=1
            stand_state = True
            
        elif playerhand.get_value()==21:
            in_play = False
            player_score+=1
            outcome = "You have won the game!"
            stand_state=True
        else:
            outcome = "Hit or stand?"
            
    else:
        outcome = "New deal?"
    
    print "Player: "+playerhand.__str__()
    print "Player: "+str(playerhand.get_value())
    print outcome
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign an message to outcome, update in_play and score
       
def stand():
    global in_play, outcome, player_score, stand_state
    if in_play:
        stand_state = True
        while dealerhand.get_value()<17:
            dealerhand.add_card(deckofcards.deal_card())
    
        if dealerhand.busted():
            outcome = "Dealer has busted!"
            player_score+=1
        elif dealerhand.get_value()>=playerhand.get_value() or dealerhand.get_value()==21:
            outcome =  "Dealer wins the game!"
            player_score-=1
        elif dealerhand.get_value()<playerhand.get_value():
            outcome =  "Player wins this round!"
            player_score+=1
        in_play = False
        
    else:
        outcome = "New deal?"
        
    print "Dealer: "+dealerhand.__str__()
    print "Dealer: "+str(dealerhand.get_value())
    print outcome
    
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global outcome, player_score, stand_state
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", (235, 50), 30, "White")
    canvas.draw_text("Dealer's Hand", (10, 145), 20, "White")
    canvas.draw_text("Player's Hand", (10, 445), 20, "White")
    canvas.draw_text(outcome, [10,325], 30, "White")
    canvas.draw_text("Player Score: "+str(player_score), [10,375], 30, "White")
    playerhand.draw(canvas,450)
    dealerhand.draw(canvas,150)
    
    if not stand_state:
        card_loc_back = (CARD_BACK_CENTER[0], 
                        CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc_back, CARD_BACK_SIZE, [121.5,200], CARD_BACK_SIZE)
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deckofcards = Deck()
playerhand = Hand()
dealerhand = Hand()

# get things rolling
frame.start()
deal()

# remember to review the gradic rubric