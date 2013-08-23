# template for "Stopwatch: The Game"

import time
import simplegui
# define global variables

cur_time = 0
total_tries = 0
success_tries = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def Start():
    global cur_time
    timer.start()
def Stop():
    global cur_time, total_tries, success_tries
    if timer.is_running():
        if int((cur_time / 100) % 10) == 0:
            success_tries +=1
        total_tries += 1
        timer.stop()
    
def Reset():
    global cur_time, success_tries, total_tries
    timer.stop()
    cur_time = 0
    success_tries = 0
    total_tries = 0

def format(t):
    tenthseconds = int((t / 100) % 10)
    seconds = int((t / 1000) % 60)
    minutes = int((t / 60000 ) % 60)
    

    tenthseconds =  str(tenthseconds)
    if seconds < 10:
        seconds = '0' + str(int(seconds))
    else:
        seconds = str(int(seconds))
    minutes = str(int(minutes))
    
    abc =  minutes + ':' + seconds + '.' + tenthseconds
    return abc

def format_tries():
    global total_tries, success_tries
    return  str(success_tries) + '/' + str(total_tries)
# define event handler for timer with 0.1 sec interval

def timer_handler1():
    global cur_time
    cur_time += 100
    
# define draw handler

def draw(canvas):
    global cur_time
    canvas.draw_text(format(cur_time), [50,112], 48, "Red")
    canvas.draw_text(format_tries(), [270,20],20, "Green")

    
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 200)
frame.add_button("Start", Start)
frame.add_button("Stop" ,Stop)
frame.add_button("Reset", Reset)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler1)


# register event handlers


# start frame

frame.start()


# Please remember to review the grading rubric

