# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
CENTER_PADDLE_POS = HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = 0
paddle2_pos = 0
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
paddle_acc = 3
max_acc = 45


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    # generates a random velocity
    x_vel = random.randrange(120, 240) / 60
    y_vel = random.randrange(60, 180) / 60
   
    ball_vel = [x_vel, -y_vel]
   
    # check direction
    ball_vel[0] = x_vel if direction == RIGHT else -x_vel
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    direction = random.randint(0, 1)
    paddle1_pos = CENTER_PADDLE_POS
    paddle2_pos = CENTER_PADDLE_POS
    score1 = 0
    score2 = 0
    spawn_ball(LEFT) if direction == 0 else spawn_ball(RIGHT)
 
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # check if the ball colides with the gutter
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        # and if the paddle is in his way
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            
            # updates the ball_vel
            if ball_vel[0] > -max_acc and ball_vel[0] < max_acc:
                ball_vel[0] *= 1.1
        else:
            # updates the score and spawn the ball
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT: 
            ball_vel[0] = - ball_vel[0]
            if ball_vel[0] > -max_acc and ball_vel[0] < max_acc:
                ball_vel[0] *= 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
    elif ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
        
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    c.draw_line((HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), PAD_WIDTH, 'White')
    c.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), PAD_WIDTH, 'White')
    
    # draw scores
    c.draw_text(str(score1), [200, 80], 40, "White", 'serif')
    c.draw_text(str(score2), [370, 80], 40, "White", 'serif')   
     
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= paddle_acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += paddle_acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= paddle_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += paddle_acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += paddle_acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= paddle_acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel += paddle_acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= paddle_acc


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)

# start frame
new_game()
frame.start()
