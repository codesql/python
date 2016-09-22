import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20.1
PAD_WIDTH = 8
HALF_PAD_WIDTH = 4
HALF_PAD_HEIGHT = 40
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = float(HEIGHT / 2)
paddle2_pos = float(HEIGHT / 2)
paddle1_vel = 0.0
paddle2_vel = 0.0
score1 = 0
score2 = 0
random_direction = 0

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    #ball start in the middle
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #ball_vel = [horizon, verticle]
    if direction == "right":
        ball_vel = [random.randrange (120, 240)/60, random.randrange (60, 180)/60]
    else:
        ball_vel = [-random.randrange (120, 240)/60, -random.randrange (60, 180)/60]
        
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    #resetting everything to 0
    paddle1_pos = float(HEIGHT / 2)
    paddle2_pos = float(HEIGHT / 2)
    paddle1_vel = 0.0
    paddle2_vel = 0.0    
    score1 = 0
    score2 = 0
    
#create randomize direction
    global random_direction
    random_direction = random.randrange(0, 2)
    print random_direction
    if random_direction == 0:
        direction = "left"
    elif random_direction == 1:
        direction = "right"
    print "Test" ,direction
    spawn_ball(direction)
      
# define event handlers
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    """https://class.coursera.org/interactivepython1-003/wiki/pong_tips note#4
    if paddle1_pos >= HALF_PAD_HEIGHT:
    paddle1_pos += paddle1_vel
    """

    #move as button is pressed, if bar hits top the 0, reset it to a bar size which is around 40, 
    #if it hits the bottom at 400, reset it a bar size which is 400-40=360, which out this, the
    #bar still stuck at the edge. Could have substitute the variables but I liked it that way .. 
    paddle1_pos += paddle1_vel
    if paddle1_pos <= 0:
        paddle1_pos = 40
    if paddle1_pos >= 400:
        paddle1_pos = 360
    
    paddle2_pos += paddle2_vel
    if paddle2_pos <= 0:
        paddle2_pos = 40
    if paddle2_pos >= 400:
        paddle2_pos = 360
    

    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    #canvas.draw_line((10, 20), (30, 40), 12, "White")
    #paddle1 from left side
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "Blue")     
    #paddle2 on right side
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "Red")  
    
    # update ball position
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] *= -1
    #ball hit the paddles and bounces back with an acceleration of 10% each time, else, the ball hit the edge and score increment by 1 each time. 
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] > paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            score2 += 1
            spawn_ball(True)
            
    if ball_pos[0] >= (WIDTH - 1) - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] > paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            score1 += 1
            spawn_ball(False)
    #control ball verticle
    ball_pos[0] += ball_vel[0]
   
    #control ball horizontal movements
    ball_pos[1] += ball_vel[1]
    
    # draw ball and scores
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    canvas.draw_text(str(score1), (WIDTH*0.25,30), 40, "Blue")
    canvas.draw_text(str(score2), (WIDTH*0.75,30), 40, "Red")

def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 8
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -vel
    
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = vel
    
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -vel
    
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = vel

def keyup(key):
    global paddle1_vel, paddle2_vel
    """ Using keyup to prevent the bar from moving nonstop when pressed once """    

    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0    
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_canvas_background('Green')
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)
frame.add_label('')
frame.add_label('       Instructions    ')
frame.add_label('')
frame.add_label('-------------------------------------')
frame.add_label ('Control Left Blue bar with "w" or "s"')
frame.add_label('-------------------------------------')
frame.add_label ('Control Right Red bar with "Arrow Up" or "Arrow Down"')


# start frame
frame.start()
new_game()
