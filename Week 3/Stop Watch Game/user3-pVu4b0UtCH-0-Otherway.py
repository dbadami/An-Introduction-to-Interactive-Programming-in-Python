# template for "Stopwatch: The Game"
import simplegui
import math
import random

# define global variables
time = 0
games_played = 0
games_won = 0
games_lost = 0
tracker = 0
formatted_time = "Click Start!"

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global formatted_time
    A = t//600
    B = (t%600)//100
    C = (t%100)//10
    D = (t%10)
    formatted_time = str(A)+":"+str(B)+str(C)+"."+str(D)
    return formatted_time

# define event handlers for buttons; "Start", "Stop", "Reset"
    
def start():
    global tracker
    timer.start()
    tracker +=1
   
def stop():
    global games_won, games_played, tracker
    if tracker > 0:
        timer.stop()
        games_played+=1
        if (time%10)==0:
            games_won +=1
        tracker = 0

def reset():
    global games_played, games_won, games_lost, time
    timer.stop()
    games_played = 0
    games_won = 0 
    games_lost = 0 
    time = 0
    format(time)

def draw_time(canvas):
    global formatted_time
    canvas.draw_text(formatted_time, [50,100], 20, "White")

def draw_win(canvas):
    global games_won, games_played
    games_won_string = str(games_won)
    games_played_string = str(games_played)
    score = games_won_string+"/"+games_played_string
    canvas.draw_text(score, [140, 20], 20, "Green")

def draw(canvas):
    draw_win(canvas)
    draw_time(canvas)
    
# define event handler for timer with 0.1 sec interval
def stop_watch():
    global time
    time += 1
    return format(time)

# create frame
frame = simplegui.create_frame("Stop Watch Game!", 200, 200)
timer = simplegui.create_timer(100, stop_watch)

# register event handlers
frame.set_draw_handler(draw)
button1 = frame.add_button("Start", start)
button2 = frame.add_button("Stop", stop)
button3 = frame.add_button("Reset", reset)

# start timer and frame
frame.start()



# remember to review the grading rubric