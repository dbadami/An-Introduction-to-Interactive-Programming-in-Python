# Implementation of classic arcade game Pong

import simplegui
import math
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT/2]
paddle1_vel = [0,0]
paddle2_vel = [0,0]
score1=0
score2=0
ball_pos = [WIDTH/2, HEIGHT/2]
right=True

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    if right:
        ball_vel = [random.randrange(2,4),-random.randrange(1,4)]
    else:
        ball_vel = [-random.randrange(2,4),-random.randrange(1,4)]
    pass

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, right  # these are floats
    global score1, score2  # these are ints
    score1 = 0 
    score2 = 0 
    x = random.randint(1,2)
    if x == 1:
        right = True
    elif x == 2:
        right = False
    ball_init(right)
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    pass

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,right
    radius = 20
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1]+=paddle1_vel[1]   
    paddle2_pos[1]+=paddle2_vel[1] 
    
    if paddle1_pos[1]<HALF_PAD_HEIGHT:
        paddle1_pos[1]=HALF_PAD_HEIGHT
    elif paddle1_pos[1]>HEIGHT-HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT-HALF_PAD_HEIGHT
    
    if paddle2_pos[1]<HALF_PAD_HEIGHT:
        paddle2_pos[1]=HALF_PAD_HEIGHT
    elif paddle2_pos[1]>HEIGHT-HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT-HALF_PAD_HEIGHT
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    #Paddle 1
    c.draw_line((paddle1_pos[0], paddle1_pos[1]-HALF_PAD_HEIGHT), (paddle1_pos[0], paddle1_pos[1]+HALF_PAD_HEIGHT), PAD_WIDTH, "White")
    #Paddle 2
    c.draw_line((paddle2_pos[0], paddle2_pos[1]-HALF_PAD_HEIGHT), (paddle2_pos[0], paddle2_pos[1]+HALF_PAD_HEIGHT), PAD_WIDTH, "White")
   
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # update ball if it hits a paddle
    #Left Paddle
    if (ball_pos[0]<= PAD_WIDTH+radius): 
        if ((ball_pos[1]<= HALF_PAD_HEIGHT+paddle1_pos[1]) and (ball_pos[1]>=paddle1_pos[1]-HALF_PAD_HEIGHT)):
            ball_vel[0] = -ball_vel[0]*1.1
            ball_vel[1] = ball_vel[1]*1.1
        else:
            score2+=1
            right = True
            ball_init(right)
       
    #Right Paddle
    if (ball_pos[0]>= WIDTH-PAD_WIDTH-radius):
        if ((ball_pos[1]<= HALF_PAD_HEIGHT+paddle2_pos[1]) and (ball_pos[1]>=paddle2_pos[1]-HALF_PAD_HEIGHT)):
            ball_vel[0] = -ball_vel[0]*1.1
            ball_vel[1] = ball_vel[1]*1.1
        else:
            score1+=1
            right = False
            ball_init(right)
        
    # updating ball if it hits one of the top two sides
    if ball_pos[1] <=radius or ball_pos[1]>= (HEIGHT-1)-radius:
        ball_vel[1] = -ball_vel[1]
        
    # draw ball and scores
    c.draw_circle(ball_pos, radius, 1,  "White", "White")
    c.draw_text(str(score1), [WIDTH/2-37.5, 40], 25, "White")
    c.draw_text(str(score2), [WIDTH/2+25, 40], 25, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key==simplegui.KEY_MAP["S"]:
        paddle1_vel[1] += acc
    elif key==simplegui.KEY_MAP["W"]:
        paddle1_vel[1] -= acc
    
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acc
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel[1] = 0
    paddle2_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()
