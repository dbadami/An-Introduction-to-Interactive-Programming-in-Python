# implementation of card game - Memory

import simplegui
import random

index_card1 = 0 
index_card2 = 0

# helper function to initialize globals
def init():
    global deck_of_cards, exposed, state, index_card1, index_card2,moves
    moves = 0
    l.set_text("Moves = 0")
    state = 0
    exposed = [False for x in range(16)]
    index_card1 = 0
    index_card2 = 0
    deck_of_cards = []
    cards1 = [x for x in range(8)]
    cards2 = [x for x in range(8)]
    cards1.extend(cards2)
    deck_of_cards.extend(cards1)
    random.shuffle(deck_of_cards)
    pass  
     
# define event handlers
def mouseclick(pos):
    global state, index_card1, index_card2, deck_of_cards, moves
    list(pos)
    if exposed[pos[0]//50] == False:
        exposed[pos[0]//50] = True
        if state == 0:
            state=1
            index_card1 = pos[0]//50
        elif state ==1:
            state= 2
            index_card2 = pos[0]//50
            moves+=1
            l.set_text("Moves = "+str(moves))
        else:
            if deck_of_cards[index_card1] == deck_of_cards[index_card2]:
                exposed[index_card2] = True
                exposed[index_card1] = True
            else:
                exposed[index_card2] = False
                exposed[index_card1] = False
            index_card1 = pos[0]//50
            state = 1
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck_of_cards, exposed, state, global_list
    for x in range(len(deck_of_cards)):
        if exposed[x] == True:
            canvas.draw_text(str(deck_of_cards[x]), [25+50*x-15, 75], 50, "White")
        elif exposed[x] == False:
            canvas.draw_polygon([[50*x,0], [50+50*x,0], [50+50*x,100], [50*x, 100]], 1 ,"Blue", "Orange")
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")


# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric