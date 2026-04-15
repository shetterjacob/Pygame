'''CY300 Project
Title: Danger Noodle
Names: CDTs James Callaway and Jacob Shetter
file: danger_noodle.py
'''
import pgzrun
import random
from enum import Enum
from collections import deque
from itertools import islice

from pygame.transform import flip, rotate

''' 
Citations:
Snake image and source code:

Pope, Daniel. "pgzero -> examples -> snake". Github. 2017 https://github.com/lordmauve/pgzero/tree/master/examples/snake

We used this source as the basic snake game to which we added configurations. Easy difficulty is very similar to this documentation.

Image for stationary obstacles:
"Platformer Art: Extended Enemies". Kenny. 2020.  https://kenney.nl/assets/platformer-art-extended-enemies

Image for boss:
"Bullet Bill" YAWD. 2020. https://ya-webdesign.com/explore/vector-bullet-bill/

Image for moving obstacle:
"Green Shell". Fandom. 2020. https://supersmashbros.fandom.com/wiki/Green_Shell

Image for powerup:
"Star". Clipart. 2020. https://www.clipartkey.com/view/TTwwmR_super-mario-fire-power/
'''
#These are global variables that will later be modified
invulnerability = False
difficulty = ''
TILE_SIZE = 24   #This sets up the size of each individual tile (don't alter)

TILES_W = 30   #This sets up the amount of tiles in the width
TILES_H = 25   #This sets up the amount of tiles in the length

WIDTH = TILE_SIZE * TILES_W  #this sets up the screen
HEIGHT = TILE_SIZE * TILES_H

def screen_rect(tile_pos):
    """This function sets up the screen that will later be drawn.
    It uses the tiles earlier defined in order to create dimenstions of a 
    rectangle."""
    x, y = tile_pos
    return Rect(TILE_SIZE * x, TILE_SIZE * y, TILES_W, TILES_H)

class Direction(Enum):
    ''' This function sets up the code that will later be 
    tied to the direction keys of the keyboard.
    '''
    RIGHT = (1, 0)
    UP = (0, -1)
    LEFT = (-1, 0)
    DOWN = (0, 1)

    def opposite(self):
        '''This method defines the opposite direction.'''
        x, y = self.value
        return Direction((-x, -y))

class Crashed(Exception):
    """This fucntion raises the case where the snake has run into either itself or 
    one of the created obstacles"""
    
class Power_up:
    def __init__(self):
        '''This function defines the initial 
        position and size of the powerup class.'''
        self.pos = (0,0)
        self.length = 1
        
    def draw(self):
        '''This function draws the powerup to 
        a location described in the previous function'''
        screen.blit(images.powerup, screen_rect(self.pos))
        
def place_powerup():
    """This function randomly places each powerup somewhere that isn't currently occupied.
    It generates coordinates at random until they that are not on
    top of the snake or an apple.
    """
    if len(snake) == TILES_W * TILES_H:
        raise ValueError("No empty spaces!")
    while True:
        pos = (
            random.randrange(TILES_W),
            random.randrange(TILES_H)
            )

        if pos not in snake:
            if pos != obstacle.pos:
                if pos != apple.pos:
                    powerup.pos = pos
                return

def no_powerup():
    '''This function moves the powerup off screen.'''
    powerup.pos = 10000,100000

class Obstacle:
    '''This class is used for the creation of obstacles in the 
    difficulties of medium and hard.'''
    def __init__(self):
        '''This function defines the initial 
        position and size of the obstacle class.'''
        self.pos = (0,0)
        self.length = 1
        
    def draw(self):
        '''This function draws the obstacle class to 
        a location described in the previous function'''
        screen.blit(images.obstacle, screen_rect(self.pos))
        
    
def place_obstacle(obstacle):
    """This function randomly places each obstacle somewhere that isn't currently occupied.
    It generates coordinates at random until they that are not on
    top of the snake.
    """
    if len(snake) == TILES_W * TILES_H:
        raise ValueError("No empty spaces!")
    while True:
        pos = (
            random.randrange(TILES_W),
            random.randrange(TILES_H)
            )

        if pos not in snake:
            obstacle.pos = pos
            return  obstacle.pos
            
class Moving_Obstacle:
    '''This class defines the moving obstacle for the hard setting.'''
    def __init__(self, pos=(10, random.randrange(0,TILES_H))):
        '''This fucntion defines the obstacles' starting poistions and the direction of movement.
        '''
        self.pos = pos
        self.dir = Direction.LEFT
        self.length = 1
        x, y = pos

    def lastdir(self):
        '''This mthod prevents the obstacle from moving off the screen.'''
        return self.pos[0][1]

    def move(self):
        '''This method describes how the obstacles move in the environment.'''
        dx= .5
        px, py = self.pos
        px = (px + dx) % TILES_W

        self.pos = px, py
     
    def draw(self):
        '''This function draws the obstacle class to 
        a location described in the previous function'''
        screen.blit(images.shell, screen_rect(self.pos))
   
class Snake:
    '''This class defines the individual components of the snake and how they interact. 
    The snake is separated into segments and the segments have animation that allow the snake 
    to move as individual pieces while still appearing as a whole.'''
    def __init__(self, pos=(TILES_W // 2, TILES_H // 2)):
        '''This fucntion defines the snakes initial position in the center of the screen and also
        appends a portion of the snake for when the snake consumes an apple.
        '''
        self.pos = pos
        self.dir = Direction.LEFT
        self.length = 4
        self.tail = deque(maxlen=self.length)

        x, y = pos
        for i in range(self.length):
            p = (x + i, y)
            segment = p, self.dir
            self.tail.append(segment)

    @property
    def lastdir(self):
        '''This method prevents the snake from moving in the opposite direction.'''
        return self.tail[0][1]

    def move(self):
        '''This method describes how the snake moves and 
        what happens with the movement of a new segment.
        This function also raises the crashed exception if
        the snake runs into itself, an obstacle or a boss.'''
        dx, dy = self.dir.value
        px, py = self.pos
        px = (px + dx) % TILES_W
        py = (py + dy) % TILES_H

        self.pos = px, py
        segment = self.pos, self.dir
        self.tail.appendleft(segment)
        for t, d in islice(self.tail, 1, None):
            if invulnerability == False:
                if t == self.pos:
                    raise Crashed(t)
                if difficulty == 'medium':
                    if self.pos == obstacle.pos:
                        raise Crashed(t)
                    if self.pos == obstacle2.pos:
                        raise Crashed(t)
                    if self.pos == obstacle3.pos:
                        raise Crashed(t)
                    if self.pos == obstacle4.pos:
                        raise Crashed(t)
                    if self.pos == obstacle5.pos:
                        raise Crashed(t)
                if difficulty == 'hard':
                    if self.pos == moving.pos:
                        raise Crashed(t)
                    if self.pos == moving2.pos:
                        raise Crashed(t)
                    if self.pos == moving3.pos:
                        raise Crashed(t)
                    if self.pos == moving4.pos:
                        raise Crashed(t)
                    if self.pos == moving5.pos:
                        raise Crashed(t)
                    if self.pos == boss.pos:
                        raise Crashed(t)
                        
    def invincible(self):
        '''This method is similar to above except there is no way for the snake 
        to die.'''
        dx, dy = self.dir.value
        px, py = self.pos
        px = (px + dx) % TILES_W
        py = (py + dy) % TILES_H

        self.pos = px, py
        segment = self.pos, self.dir
        self.tail.appendleft(segment)
        
    def __len__(self):
        '''This method defines the length of the snake and keeps
        it consistent as it grows.'''
        return self.length

    def __contains__(self, pos):
        '''This method contains every coordinate that the snake is in.'''
        return any(p == pos for p, d in self.tail)

    def grow(self):
        '''This method defines how the snake grows.'''
        self.length += 1
        self.tail = deque(self.tail, maxlen=self.length)

    def draw(self):
        '''This method creates a filled rectangle that exists behind the image of the snake.'''
        for pos in self.tail:
            screen.draw.filled_rect(screen_rect(pos), 'green')

class SnakePainter:
    '''This class defines how the snake interacts inside the pygame zero environment.'''
    
    def __init__(self):
        '''This method defines how the segments of the snake deal with the overall movement.'''
        right, up, left, down = (d.value for d in Direction)
        straight = images.snake_straight
        corner = images.snake_corner
        corner2 = flip(corner, True, False)
        self.tiles = {
            # Straight sections in each direction
            (right, right): straight,
            (up, up): rotate(straight, 90),
            (left, left): rotate(straight, 180),
            (down, down): rotate(straight, 270),

            # Corner sections in the anticlockwise direction
            (right, up): corner,
            (up, left): rotate(corner, 90),
            (left, down): rotate(corner, 180),
            (down, right): rotate(corner, 270),

            # Corner sections in the clockwise direction
            (left, up): corner2,
            (up, right): rotate(corner2, -90),
            (right, down): rotate(corner2, -180),
            (down, left): rotate(corner2, -270),
        }

        head = images.snake_head
        self.heads = {
            right: head,
            up: rotate(head, 90),
            left: rotate(head, 180),
            down: rotate(head, 270),
        }

        tail = images.snake_tail
        self.tails = {
            right: tail,
            up: rotate(tail, 90),
            left: rotate(tail, 180),
            down: rotate(tail, 270),
        }

    def draw(self, snake):
        '''This method combines the segments of the snake.'''
        for i, (pos, dir) in enumerate(snake.tail):
            if not i:
                # draw head
                tile = self.heads[snake.dir.value]
            elif i >= len(snake.tail) - 1:
                # draw tail
                nextdir = snake.tail[i - 1][1]
                tile = self.tails[nextdir.value]
            else:
                nextdir = snake.tail[i - 1][1]
                key = dir.value, nextdir.value
                try:
                    tile = self.tiles[key]
                except KeyError:
                    tile = self.tiles[dir.value, dir.value]

            r = screen_rect(pos)
            screen.blit(tile, r)

class Apple:
    '''This class defines the apple that the snake eats.'''
    def __init__(self):
        '''This method gives the apple an intitial position'''
        self.pos = 0, 0

    def draw(self):
        '''This method draws the apple'''
        screen.blit(images.apple, screen_rect(self.pos))

class Boss:
    """Creates a class for a bullet boss that spawns on hard"""
    def __init__(self):
        ''''This method defines the direction and initial position of the boss'''
        self.pos =  0, TILES_H
        self.dir = Direction.RIGHT
        
    def draw(self):
        '''This method draws the boss'''
        screen.blit(images.bullet, screen_rect(self.pos))
    
    def move(self):
        '''This method describes how the boss moves and 
        resets its y coordinate once it leaves the screen.'''
        dx, dy = self.dir.value
        px, py = self.pos
        px = (px + dx) % TILES_W
        py = (py + dy) % TILES_H
        self.pos = px, py
        if px == (TILES_W-1):
            self.pos = 0, random.randrange(TILES_H)
        

#This variable attaches the keyboard buttons to what they should do
KEYBINDINGS = {
    keys.LEFT: Direction.LEFT,
    keys.RIGHT: Direction.RIGHT,
    keys.UP: Direction.UP,
    keys.DOWN: Direction.DOWN,
}
#defines the class of all obstacles, the boss, the apple and the snake
powerup = Power_up()
obstacle = Obstacle() 
obstacle2 = Obstacle()
obstacle3 = Obstacle()
obstacle4 = Obstacle()
obstacle5 = Obstacle()
moving = Moving_Obstacle()
moving2 = Moving_Obstacle()
moving3 = Moving_Obstacle()
moving4 = Moving_Obstacle()
moving5 = Moving_Obstacle()

snake = Snake() #makes snake part of its class
snake.alive = True #sets the value of snake being alive to true

snake_painter = SnakePainter() #makes the snake painter part of its class

apple = Apple() #makes apple part of its class

boss = Boss() #creates a boss

def place_apple():
    """This function randomly generates coordinates and if the coordinates are 
    not at the same location as the snake or an obstacle the apple is placed there.
    """
    if len(snake) == TILES_W * TILES_H:
        raise ValueError("No empty spaces!")

    while True:
        pos = (
            random.randrange(TILES_W),
            random.randrange(TILES_H)
        )

        if pos not in snake:
            if pos != obstacle.pos or obstacle2.pos or obstacle3.pos or obstacle4.pos or obstacle5.pos:
                apple.pos = pos
                return


def on_key_down(key):
    '''This function defines what happens on the action of pressing the key down.'''
    if not snake.alive:
        return

    dir = KEYBINDINGS.get(key)
    if dir and dir != snake.lastdir.opposite():
        snake.dir = dir
        return


def tick():
    '''This function keeps the clock of the game moving if the snake is still alive 
    and does nothing if the snake is not alive. It also calls the invulnerability 
    method if the snake eats a powerup and moves all of the pieces to the game.'''
    global invulnerability
    if invulnerability == False:
        if not snake.alive:
            return
        try:
            snake.move()
            if difficulty == 'easy':
                no_powerup()
            if difficulty == 'hard':
                boss.move()
                moving.move()
                moving2.move()
                moving3.move()
                moving4.move()
                moving5.move()
        except Crashed:
            snake.alive = False
            stop()
        else:
            if snake.pos == apple.pos:
                sounds.yum.play()
                snake.grow()
                start()
                place_apple()
            if difficulty == 'medium' or 'hard':
                if snake.pos == powerup.pos:
                    music.play_once('invulnerable.wav')
                    no_powerup()
                    clock.schedule(uninvulnerability,10)
                    clock.schedule(place_powerup,15)
                    invulnerability = True

    else:
        snake.invincible()
        if snake.pos == apple.pos:
                sounds.yum.play()
                snake.grow()
                start()
                place_apple()    
                
def uninvulnerability():
    '''This function resets the invulnerability to false
    and restarts the normal game music.'''
    global invulnerability 
    music.play('music.wav')
    invulnerability = False

def start():
    """This function sets and updates the clock of the game. The clock
    gets faster for each time the snake eats an apple and changes its interactions
    based on the chosen difficulty of the game.
    """
    if difficulty == 'easy':
        interval = max(0.1, 0.4 - 0.02 * (len(snake) - 3))
        clock.unschedule(tick)
        clock.schedule_interval(tick, interval)


    if difficulty == 'medium':
        interval = max(0.1, 0.4 - 0.04 * (len(snake) - 3))
        clock.unschedule(tick)
        clock.schedule_interval(tick, interval)

    if difficulty == 'hard':
        interval = max(0.1, 0.4 - 0.1 * (len(snake) - 3))
        clock.unschedule(tick)
        clock.schedule_interval(tick, interval)


def stop():
    """This function stops the clock of the game and will be called
    when the snake is dead. It also plays the gameover noise."""
    music.play_once('gameover.wav')
    clock.unschedule(tick)


def draw():
    '''This fucntion takes all of the variables created and combines them into the pygame 
    zero game board. The board changes based on the difficulty.'''
    global invulnerability
    screen.clear()
    screen.fill((0,171,255))
    if difficulty == '':
        screen.draw.text("EASY", color = 'white', center = (WIDTH/6,HEIGHT/2))
        screen.draw.text('MEDIUM', color = 'white', center = (WIDTH/2,HEIGHT/2))
        screen.draw.text('HARD', color = 'white', center = (WIDTH-80,HEIGHT/2))
        
    if difficulty != '':
        snake_painter.draw(snake)
        apple.draw()
    if invulnerability == True:
        screen.draw.text('INVULNERABLE',color='white',center=(WIDTH/2, HEIGHT/12))

    if difficulty == 'easy':
        pass
    
    if difficulty == 'medium':
        powerup.draw() #draws power up
        obstacle.draw() #draws obstacle
        obstacle2.draw()
        obstacle3.draw()
        obstacle4.draw()
        obstacle5.draw()

        
    if difficulty == 'hard':
        powerup.draw()
        moving.draw() #draws moving obstacle
        moving2.draw()
        moving3.draw()
        moving4.draw()
        moving5.draw()
        boss.draw() #draws boss on screen


    screen.draw.text(
        'Apples: %d' % (len(snake)-4),
        color='white',
        topright=(WIDTH - 5, 5)
    )

    if not snake.alive:
        screen.draw.text(
            "You died!",
            color='white',
            center=(WIDTH/2, HEIGHT/2)
        )

#places all of the obstacles and the initial powerup
place_obstacle(obstacle)
place_obstacle(obstacle2)
place_obstacle(obstacle3)
place_obstacle(obstacle4)
place_obstacle(obstacle5)
place_obstacle(moving)
place_obstacle(moving2)
place_obstacle(moving3)
place_obstacle(moving4)
place_obstacle(moving5)
place_powerup()
place_apple()

def on_mouse_down(pos):
    '''This function allows you to select your desired 
    game difficulty before starting.'''
    global difficulty
    pos = pos[0]//TILE_SIZE, pos[1]//TILE_SIZE
    easy = [(4,11),(4,12),(5,11),(5,12)]
    medium = [(13,11),(13,12),(14,11),(14,12),(15,11),(15,12),(16,11),(16,12)]
    hard = [(25,11),(25,12),(26,11),(26,12)]
    if pos in easy:
       difficulty = 'easy'
       start()
    if pos in medium:
       difficulty = 'medium'
       start()
    if pos in hard:
       difficulty = 'hard'
       start()

#plays background music
music.play('music.wav')

pgzrun.go()