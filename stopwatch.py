# template for "Stopwatch: The Game"

# define global variables
import simplegui
import random

interval = 100
ticker=0 # ticker to keep track of game attempted
time = '0:00.0'
t=0
game_cnt=0
win_cnt=0
milliseconds =0 


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """format function and breaking down to msec, sec, min then put them to a A:BC:D format"""
    global time, milliseconds
    milliseconds = t % 10
    sec = (t - milliseconds) / 10
    minutes = sec // 60
    seconds = sec % 60
    if seconds >=10:
        time = str(minutes) + ':' + str(seconds) + '.' +str(milliseconds)
    else:
        time = str(minutes) + ':0' + str(seconds) + '.' +str(milliseconds)
    

# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global ticker
    # increment ticker everytime the game start either one of the following works
    #ticker+=1
    ticker=1
    timer.start()
    #print "test timer started"

def Stop():
    """ stop and start recording successful click
        The following are for gaming and win/lose count
    """
    #game_cnt and win_cnt in recording the number of game and winning counts
    global ticker, game_cnt, win_cnt, milliseconds
    #print "Test 1 : ", timer.is_running()
    
    game_cnt = game_cnt + ticker
    #if milliseconds hits 0, x:xx:0, that is a winning condition AND if the timing is running, start recording the winning count
    # the timer.is_running()==True is the key here where player won once and keep pressing Stop and keep winning. The is_running() is to make sure a start() has been triggered to win
    if milliseconds == 0 and timer.is_running()==True:
        win_cnt += 1
        #print "Test 2: ", timer.is_running()
    #Having the stop here will solve the bug issue where player, won the game once then keep pressing stop, stop, stop
    
    if timer.is_running()==True:
        timer.stop()
    #once stopped, set the ticker back to 0
    ticker = 0
    #print "test timer stopped"

    
def Reset():
    """Reset function"""
    global t, time, game_cnt, win_cnt, ticker
    timer.stop()
    #resetting everything back to 0 before starting over
    game_cnt=win_cnt=ticker=t=0
    format(t)
    #timer.start()
    #print "timer reset"



# define event handler for timer with 0.1 sec interval
def tick():
    """standard clock ticking function implementation"""
    global t
    t = t + 1
    #print "test"+ str(t)
    format(t)
       
# define draw handler
def draw(canvas):
    #pretty standard placement of where the time and game/win text
    #canvas first drawn will be time = 0:00:0
    canvas.draw_text(time, (100, 100), 60, 'Yellow')
    canvas.draw_text(str(win_cnt) + '/' + str(game_cnt),(350, 20), 20, "Green")
    
# create frame
"""standard frame and buttons creation"""
frame=simplegui.create_frame("StopWatch " , 400, 400)
frame.add_button("Start", Start, 200)
frame.add_button("Stop", Stop, 200)
frame.add_button("Reset", Reset, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
#timer.stop() #question states, make sure the game start at stop state
# Please remember to review the grading rubric
