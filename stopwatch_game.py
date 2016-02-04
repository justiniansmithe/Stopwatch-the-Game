# template for "Stopwatch: The Game"

import simplegui
import random

# define global variables

message = "Python is Fun!"
time = 0
position = [50, 50]
width = 300
height = 200
interval = 100
is_stopped = False
is_started = False
is_reset = False
tries = 0
count = 0
score = str(int(count))

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    global display, minutes, seconds, milliseconds, scoreboard, tries
    minutes = time / 600
    seconds = time % 600 / 10
    milliseconds = time % 10
    
    
    if seconds < 10:
        seconds = "0" + str(seconds)
        
    display = str(minutes) + ":" + str(seconds) + "." + str(milliseconds)
    
    time = display
    
    if is_reset == True:
        time = 0
          
        
    scoreboard = str(score) + " / " + str(tries)
    
    return display
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global time, is_started, is_reset, score
    
    if score == None:
        score = 0
        
    is_started = True
    is_reset = False
    

def stop():
    global time, is_started, tries, display, score, scoreboard, milliseconds
    #format(time)
    is_started = False
    is_reset = False
    #update_score()
    
    tries = tries + 1
    
    
    if milliseconds == 0:
        score = int(score) + 1
        
    scoreboard = str(score) + " / " + str(tries)
    


def reset():
    global time, is_reset, is_started, score, tries
    is_reset = True
    #format(0)
    score = 0
    tries = 0
    time=0
    update_score()

    
def update_score():
    #global score, tries, time
    #if time % 100 == 0 and is_started == False:
    #    score = score + '1'
        
        
    scoreboard = str(score) + " / " + str(tries)
    return scoreboard

# define event handler for timer with 0.1 sec interval
    
def tick():
    global time, is_started
    
    if is_reset == True:
        display = format(0)
        #reset()
        
    if is_started == True:
        time = time + 1
        format(time)
        #update_score()
        


# define draw handler
def draw(canvas):
    canvas.draw_text(display, position, 50, "White")
    canvas.draw_text(scoreboard, [150,200], 50, "Green")



format(time)

# create frame
frame = simplegui.create_frame("Stopwatch, bitches", width, height)

# register event handlers
text = frame.add_button("Start", start, 150)
text = frame.add_button("Stop", stop, 150)
text = frame.add_button("Reset", reset, 150)


frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric

'''
print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(1325)
print format(4567)
print format(5999)
print format(0) 
print format(11)
print format(321)
print format(613)
print format(0)'''






