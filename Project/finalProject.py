import pgzrun
import random  #used to randomly generate asteroid starting location

ship = Actor('ship3.png', center = (400, 500))    #Actors defined.               
laser = Actor('redlaser.png', center = (ship.x, ship.y))        
invisible_laser = Actor('invisable_laser.png')                  
ship_explosion = Actor('explosion_one.png')                                 
Bolt = Actor('bolt_gold.png', center = (400,-50))                                                                        
enemy_ship = Actor('millennium_falcon.png', center = (400,-60))
enemy_laser = Actor('redlaser.png', center = (enemy_ship.x, enemy_ship.y))

big_asteroid = Actor('big_meteor.png', center = (600, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png')                                                               
medium_asteroid = Actor('meteor_med.png', center = (50, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (500, -50))
explosion_two = Actor('explosion_two.png')
small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (700, -50))

def draw_laser(i):                  #allows for rapid fire of laser. 
    list[i].draw()                  #When spacebar is hit (line 243), this function is called. It appends laser actors to be drawn later
    animate(list[i], pos = (ship.x +0, ship.y -1000))   #shoots the laser from players ship            

list =[]                            #Actors drawn on screen
def draw():   
    global score
    global boss
    global enemy_health                                           
    screen.clear()
    screen.blit('space_background.png', (0,0))  #This module has a stary background.
    
    ship.draw()
    global list
    for i in range(len(list)):
        draw_laser(i)
                                   
    big_asteroid.draw()
    big_asteroid_two.draw()
    medium_asteroid.draw()
    medium_asteroid_two.draw()
    small_asteroid.draw()
    small_asteroid_two.draw()
    Bolt.draw()
    enemy_laser.draw()
    enemy_ship.draw()

    if score >=250 and boss == True:    #When the conditions are met, the bosses health is drawn and updated
        screen.draw.text(str('Enemy Health'), color = 'red', center = (400,25), fontname = 'walkway_black', fontsize =30)
        screen.draw.text(str(enemy_health), color = 'red', center = (400,50), fontname = 'walkway_black', fontsize =30)                                           #score system
    
    color = 'green' #If score is postive, score is green, when negative, it is red.
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    global Bolt_speed
    if ship.image == 'explosion_one.png':   #When ship is destroyed, a 'game over' menu + game over music. 
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
        Bolt_speed = 0.5                    #Perks and enemy ship reset 
        Bolt.pos = (400,-50)
        enemy_ship.pos = (400,-60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))  #The score of the game
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:  #This version has a menu. Game variable is a method of control. 
        ship.center = (400, 500)  #When game is being played, game == true, and menu is not displayed.
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
                                                
    if menu == True:  #If menu variable is true, display instructions
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():            #functions that reset asteroids to top of screen, and changes image to a rock
    num = random.randint(50,450)      #There are a total of six asteroids in the game. Once destroyed they reset.
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)  #When asteroids are destroyed, they are re drawn at top of screen at random location

def big_asteroid_two_normal():
    num = random.randint(50,450)
    big_asteroid_two.image = 'big_meteor.png'
    big_asteroid_two.center = (num + 100, -50)

def medium_asteroid_normal():
    num = random.randint(50,450)
    medium_asteroid.image = 'meteor_med.png'
    medium_asteroid.center = (num, -50)
    
def medium_asteroid_two_normal():
    num = random.randint(50,500)
    medium_asteroid_two.image = 'meteor_med.png'
    medium_asteroid_two.center = (num, -50)
    
def small_asteroid_normal():
    num = random.randint(50,450)
    small_asteroid.image = 'meteor_small.png'
    small_asteroid.center = (num, -50)
    
def small_asteroid_two_normal():
    num = random.randint(50,450)
    small_asteroid_two.image = 'meteor_small.png'
    small_asteroid_two.center = (num, -50)

def ship_normal():
    ship.image = 'ship3.png'  
                                                #Explosions defined for each asteroid and ship. Sounds included
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     
    
def update_big_asteroid_two_explode():
    sounds.largebang.play()
    big_asteroid_two.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_two_normal, 0.01)
    
def update_medium_asteroid_explode():
    sounds.mediumbang.play()
    medium_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_normal, 0.01)
    
def update_medium_asteroid_two_explode():
    sounds.mediumbang.play()
    medium_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_two_normal, 0.01)
    
def update_small_asteroid_explode():
    sounds.smallbang.play()
    small_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_normal, 0.01)
    
def update_small_asteroid_two_explode():
    sounds.smallbang.play()
    small_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_two_normal, 0.01)

def update_ship_explode():   
    global game                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                  
                                                                                
def game_restart():                 
    ship.image = 'ship3.png' 
    game = False
                                #updates
def update_game():
    global game  #Controls status of game. Game in play == True. "Global" allows information from the game to 
    global ship_image #be processed by the program in real time.
    global score #allows for update of score in real time.
    global menu  #allows for control of status of menu.

    if keyboard.a:    #Press 'a' key to start game. Changes status of game to True, running the program.                                                                      
        game = True
        ship.image = 'ship3.png'
        score = 0
    if keyboard.B:    #Press 'b' for menu
        menu = True
    if keyboard.C:    #Press 'c' to remove menu
        menu = False

def laser_system():     #The ship shoots with noise. 
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60))) #Actors appended to a list. This enables rapid drawing of lasers on screen.
    
def update_ship():      #Ship moves left and right with left and right arrow keys.
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def bolt_perk():       #This function, when called, releases a lightning bolt that floats down screen.
    Bolt.draw()
    Bolt.y += Bolt_speed

def enemy():           #When function is called, enemy ship appears.
    animate(enemy_ship, pos = (enemy_ship.x, enemy_ship.y + 200))

def enemy_attack():    #When function called, enemy ship shoots laser.
    animate(enemy_laser, pos = (enemy_ship.x, enemy_ship.y + 1000))

score = 0    #Starting score.
speed = 0.5  #starting asteroid speed.
Bolt_speed = 1
game = False #starting status of game, menu, and boss. When True, game starts, menu appears, boss appears respectively.
menu = False 
boss = False
enemy_health = 50   #starting enemy health.                                                 
def update():       #main game loop.
    global speed   
    global Bolt_speed
    global score 
    global game 
    global list
    global boss   
    global enemy_health

    update_game()
    if game == True:              #asteroid updates.             
        big_asteroid.angle += 1   #While game is ongoing, asteroids spin, and move at a velocity set by the variable "Speed".
        big_asteroid.y += speed
        big_asteroid_two.angle +=1
        big_asteroid_two.y += speed
        medium_asteroid.angle += 1
        medium_asteroid.y += speed
        medium_asteroid_two.angle += 1
        medium_asteroid_two.y += speed
        small_asteroid.angle += 1
        small_asteroid.y += speed
        small_asteroid_two.angle += 1
        small_asteroid_two.y += speed
        update_ship()

        if score > 550:             #Perk and boss requirements.
            bolt_perk()
            
        if score in range(250,253):  
            boss = True
            enemy()

        if score >=250 and boss == True:
            enemy_attack()

        if score >=250 and boss == True:   
            speed = 0
            big_asteroid.pos = (600, -100)
            big_asteroid_two.pos = (300, -100)                                                                 
            medium_asteroid.pos = (50, -100)
            medium_asteroid_two.pos = (500, -100)
            small_asteroid.pos = (150, -100)
            small_asteroid_two.pos= (700, -100)
            
        if enemy_laser.y > 800 and score > 250 and boss == True:   #reset enemy laser to enemy ship. Drawn underneath ship.
            enemy_laser.pos = (enemy_ship.x, enemy_ship.y)
            enemy_attack()
            sounds.fire.play()
            
    if keyboard.space:                            #when spacebar is hit, laser_system function appends laser actor to list.
        clock.schedule_unique(laser_system, 0.05) #0.05 restricts user from holding down space bar to spray and pray.

    for item in list:    #Item == laser actors from list. When laser hits any of the six asteroids or boss, they explode.

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1                   #Score and asteroid speed increases when asteroids hit
            speed += 0.01          
            
        if item.colliderect(big_asteroid_two):
            update_big_asteroid_two_explode()
            score +=1
            speed += 0.01

        if item.colliderect(medium_asteroid):
            update_medium_asteroid_explode()
            score +=1
            speed += 0.01

        if item.colliderect(medium_asteroid_two):
            update_medium_asteroid_two_explode()
            score +=1
            speed += 0.01

        if item.colliderect(small_asteroid):
            update_small_asteroid_explode()
            score +=1
            speed += 0.01

        if item.colliderect(small_asteroid_two):
            update_small_asteroid_two_explode()
            score +=1
            speed += 0.01

        if item.colliderect(enemy_ship) and score >=250 and boss == True:
            enemy_health -= 0.1   #When enemy boss hit by laser, the enemy's health decreases slightly

        if item.colliderect(enemy_ship) and score >=250 and enemy_health <=0 and boss == True:
            enemy_ship.center = (400, -60)
            enemy_laser.center = (400,-60)
            boss = False
            score += 10
            speed += 0.5
            enemy_health = 50
            screen.clear()

        if item.y <= -100:  #This statement is very important. Once lasers are drawn and animated, the actors are deleted from the screen.   
            del list[0]     #If actors where not deleted, the game would begin to lag very quickly.

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two) or ship.colliderect(enemy_laser):
        update_ship_explode() #When ship is hit by asteroid or enemy laser, game resets by calling the following functions.
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= [] 
        screen.clear()

    if ship.colliderect(Bolt):   #If ship contacts perk, asteroid speed resets. Bolt perk resets.
        speed = 0.5
        Bolt.pos = (400,-50)
        Bolt_speed = 0

    if big_asteroid.y > 650:       #The following statements reset the asteroids when they get past the ship off screen.
        big_asteroid_normal()      #Points removed from score.
        score -= 14

    if big_asteroid_two.y > 650:
        big_asteroid_two_normal()
        score -= 14
    
    if medium_asteroid.y > 650:
        medium_asteroid_normal()
        score -= 14

    if medium_asteroid_two.y > 650:
        medium_asteroid_two_normal()
        score -= 14

    if small_asteroid.y > 650:
        small_asteroid_normal()
        score -= 14

    if small_asteroid_two.y > 650:
        small_asteroid_two_normal()
        score -= 14    

    if ship.x < 50:        #The final two statements prevent the player from going off screen.
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  

pgzrun.go()