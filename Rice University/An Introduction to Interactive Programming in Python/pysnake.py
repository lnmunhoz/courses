import simplegui
import math
import random

WIDTH = 310
HEIGHT = 310
game_state = 'Stopped'
score = 0

class Square:
    def __init__(self, position, color):
        self.position = position
        self.color = color
             
    def draw(self, canvas):
        canvas.draw_polygon([(self.position[0] - 10 // 2, self.position[1]),
                             (self.position[0] + 10  // 2, self.position[1])], 
                              10, self.color)  
    
class Snake:
    def __init__(self, head_position):
        self.current_direction = 'right'
        self.velocity = [10, 0]
        self.squares = [Square(head_position, 'Yellow'),
                        Square([head_position[0] - 10, head_position[1]], 'Yellow'),
                        Square([head_position[0] - 20, head_position[1]], 'Yellow')]
        
    def draw(self, canvas): 
        for square in self.squares:
            square.draw(canvas)
          
    def update(self):
        if game_state == 'Playing':
            for i in range(len(self.squares) - 1, 0, -1):
                self.squares[i].position = [self.squares[i - 1].position[0],
                                            self.squares[i - 1].position[1]]
            
            self.squares[0].position[0] += self.velocity[0]
            self.squares[0].position[1] += self.velocity[1]
                         
    def move(self, direction):
        
        if direction == "left" and self.current_direction != 'right':
            self.velocity = [-10, 0]     
            self.current_direction = direction
        
        elif direction == "right" and self.current_direction != 'left':
            self.velocity = [10, 0]
            self.current_direction = direction
       
        elif direction == "up" and self.current_direction != 'down':
            self.velocity = [0, -10]
            self.current_direction = direction
       
        elif direction == "down" and self.current_direction != 'up':
            self.velocity = [0, 10]
            self.current_direction = direction
                       
    def eat(self, food):
        food_list.remove(food)
        self.squares.append(Square(self.squares[-1].position, 'Yellow'))
 
def random_points():
    x = 10 * random.randint(1, 30) + 5
    y = 10 * random.randint(1, 30) + 5
  
    if [x, y] in [square.position for square in snake.squares]:
        return random_points()
    else:
        return [x, y]
        
def spawn_food():    
    food = Square(random_points(), 'White')
    food_list.append(food)
    
def process_game():
    global game_state, score
    
    if game_state == 'Playing':
        
        # eat food
        for food in food_list:
           if snake.squares[0].position == food.position:
               snake.eat(food)
               score += 1
               spawn_food()
                    
        # if head's collide with squares
        for i in range(len(snake.squares) - 1, 0, -1):
            if snake.squares[0].position == snake.squares[i].position:
                snake.squares[0].color = 'Red'
                snake.squares[i].color = 'Red'
                game_state = 'Finishing'
                                  
        # if head goes out of bounds
        if snake.squares[0].position[0] > WIDTH or snake.squares[0].position[0] < 0:
            game_state = 'Finishing'
        elif snake.squares[0].position[1] > HEIGHT or snake.squares[0].position[1] < 0:
            game_state = 'Finishing'
    
    elif game_state == 'Finishing':
        if len(snake.squares) > 0:
            snake.squares.pop()
        else:
            game_state = 'Stopped'
        
        
def draw_handler(canvas):
    
    # game
    if game_state == 'Playing' or game_state == 'Finishing':
        snake.draw(canvas)
        for food in food_list:
            food.draw(canvas) 
    
    # static screen    
    elif game_state == 'Stopped':
        canvas.draw_text('pysnake', [95, HEIGHT / 2], 30, 'Yellow', 'monospace')
        canvas.draw_text('press spacebar to play!', [20, 185], 20, 'White', 'monospace')
        canvas.draw_text('developed by: lnmunhoz', [85, 300], 10, 'White', 'monospace')
        
        if score != 0:
            canvas.draw_text('last score: ' + str(score), [75, 250], 20, 'White', 'monospace')
    

def timer_handler():
    snake.update()
    process_game()
        
def start_game():
    global snake, food_list, game_state, score
    
    score = 0
    game_state = 'Playing'
    snake = Snake([WIDTH / 2, HEIGHT / 2])
    food_list = []
    spawn_food()
      
def keydown_handler(key):
    
    if key == simplegui.KEY_MAP["space"]:
        if game_state == 'Stopped':
            start_game()
    
    if key == simplegui.KEY_MAP["left"]:
        snake.move('left')
    if key == simplegui.KEY_MAP["right"]:
        snake.move('right')
    if key == simplegui.KEY_MAP["up"]:
         snake.move('up')
    if key == simplegui.KEY_MAP["down"]:
        snake.move('down')

          
snake = Snake([WIDTH / 2, HEIGHT / 2])
food_list = []

timer = simplegui.create_timer(50, timer_handler)
timer.start()

frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)

frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown_handler)
frame.start()