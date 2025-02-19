#This is the progression from version 1 to the final verison.
#As I slowly figured out how to use the pygamezero syntax, I added new aspects to my program.
#I created all of this from scatch. No outside space shooter source code was used. 

import pgzrun
import random
#Version 1
''' 
ship = Actor('ship3.png', center = (400, 500))
laser = Actor('redlaser.png', center = (ship.x, ship.y-65))
thruster = 0.9


def draw():
    screen.clear()
    ship.draw()
    if keyboard.space:
        laser.draw()
        laser.y -=15
        if laser.y < 0:
            laser.center =(ship.x, ship.y-65)

def update():
    
    if keyboard.left:
        ship.x -= 10
    if keyboard.right:
        ship.x += 10
''' 
#Version 2
'''                                                            #this shoots a laser after a space bar is hit, but wont shoot again   
ship = Actor('ship3.png', center = (400, 500))
laser = Actor('redlaser.png', center = (ship.x, ship.y-65))
thruster = 0.9



def draw():
    screen.clear()
    ship.draw()
    laser.draw()
   

def update():
    if keyboard.space:
        animate(laser, pos = (ship.x +0, ship.y -1000))
        if laser.y < 200:
            laser.pos = (ship.x,ship.y)
'''       
#Version 3
'''                                                           #This module has a blank background, no noise. The ship moves and shoots.
ship = Actor('ship3.png', center = (400, 500))
laser = Actor('redlaser.png', center = (ship.x, ship.y-65))
thruster = 0.9



def draw():
    screen.clear()
    laser.draw()
    ship.draw()
    if keyboard.space:
        update_laser()

    
def update_laser(): 
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)  

def update_ship():
    if keyboard.left:
        ship.x -=10
    if keyboard.right:
        ship.x +=10

def update():
    update_laser()
    update_ship()
'''
#Version 4
'''
ship = Actor('ship3.png', center = (400, 500))                    #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))
thruster = 0.9

def draw():
    screen.clear()
    laser.draw()
    ship.draw()
    if keyboard.space:
        update_laser()

    
def update_laser(): 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)  

def update_ship():
    if keyboard.left:
        ship.x -=10
    if keyboard.right:
        ship.x +=10

def update():
    update_ship()
    if keyboard.space:
        update_laser()
'''
#Version 5
'''
ship = Actor('ship3.png', center = (400, 500))                    #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))          #This also draws one asteroid, and explodes when hit. But laser travels through
big_asteroid = Actor('big_meteor.png', center = (400, 100))       #and the explosion image stays
explosion_one = Actor('explosion_one.png')

def draw():
    screen.clear()
    laser.draw()
    ship.draw()
    big_asteroid.draw()
    if keyboard.space: 
        update_laser()

def update_laser(): 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)  

def update_ship():
    if keyboard.left:
        ship.x -=10
    if keyboard.right:
        ship.x +=10

def update_big_asteroid():
    big_asteroid.image = 'explosion_one.png'

def update():
    #big_asteroid.angle += 1
    update_ship()
    update_big_asteroid
    if keyboard.space:
        update_laser()
    if laser.collidepoint(big_asteroid.x,big_asteroid.y):
        update_big_asteroid()
'''
#Version 6
'''
ship = Actor('ship3.png', center = (400, 500))                    #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))          #This also draws one asteroid, and explodes when hit. But laser travels through
big_asteroid = Actor('big_meteor.png', center = (400, 100))       #the meteor changes back into a meteor after explosion, and responds at 100,100
explosion_one = Actor('explosion_one.png')

def draw():
    screen.clear()
    laser.draw()
    ship.draw()
    big_asteroid.draw()
    if keyboard.space: 
        update_laser()

def update_laser(): 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)  

def update_ship():
    if keyboard.left:
        ship.x -=10
    if keyboard.right:
        ship.x +=10

def big_asteroid_normal():
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (100,100)

def update_big_asteroid_explode():
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 1.0)
    

def update():
    #big_asteroid.angle += 1
    update_ship()
    #update_big_asteroid()
    if keyboard.space:
        update_laser()
    if laser.collidepoint(big_asteroid.x,big_asteroid.y):
        update_big_asteroid_explode()
'''
#Version 7
'''
ship = Actor('ship3.png', center = (400, 500))                    #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))          #This also draws one asteroid, and explodes when hit. But laser travels through
big_asteroid = Actor('big_meteor.png', center = (400, -50))       #the meteor changes back into a meteor after explosion, and responds at off screen
explosion_one = Actor('explosion_one.png')                        #the meteor moves and spins, but the laser only blows it up if it is dead center.

def draw():
    screen.clear()
    laser.draw()
    ship.draw()
    big_asteroid.draw()
    if keyboard.space: 
        update_laser()

def update_laser(): 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)  

def update_ship():
    if keyboard.left:
        ship.x -=10
    if keyboard.right:
        ship.x +=10

def big_asteroid_normal():
    
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (400, -50)

def update_big_asteroid_explode():
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 1.0)
    

def update():
    big_asteroid.angle += 1
    big_asteroid.y += 1
    update_ship()
    
    if keyboard.space:
        update_laser()
    if laser.collidepoint(big_asteroid.x,big_asteroid.y):
        update_big_asteroid_explode()
'''
#Version 8
'''
ship = Actor('ship3.png', center = (400, 500))                    #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))          #This also draws one asteroid, and explodes when hit. But laser travels through
big_asteroid = Actor('big_meteor.png', center = (400, -50))       #the meteor changes back into a meteor after explosion, and responds at off screen
explosion_one = Actor('explosion_one.png')                        #the meteor moves and spins. Laser blows in most of the places it hits.
                  
def draw():
    screen.clear()
    laser.draw()
    ship.draw()
    big_asteroid.draw()
    if keyboard.space: 
        update_laser()

def update_laser(): 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)  

def update_ship():
    if keyboard.left:
        ship.x -=10
    if keyboard.right:
        ship.x +=10

def big_asteroid_normal():
    
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (400, -50)

def update_big_asteroid_explode():
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 1.0)
    

def update():
    big_asteroid.angle += 1
    big_asteroid.y += 1
    update_ship()
    
    if keyboard.space:
        update_laser()
    if laser.collidepoint(big_asteroid.center) or laser.collidepoint(big_asteroid.midbottom) or laser.collidepoint(big_asteroid.bottomright) or laser.collidepoint(big_asteroid. bottomleft) or laser.collidepoint(big_asteroid.midright) or laser.collidepoint(big_asteroid.midleft) or laser.collidepoint(big_asteroid.topleft) or laser.collidepoint(big_asteroid.midtop) or laser.collidepoint(big_asteroid.topright):
        update_big_asteroid_explode()
'''
#Version 9
'''
ship = Actor('ship3.png', center = (400, 500))                    #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))          #This also draws one asteroid, and explodes (image and sound) when hit. Laser does not travel through asteroid
invisible_laser = Actor('invisable_laser.png')
big_asteroid = Actor('big_meteor.png', center = (400, 0))         #the meteor changes back into a meteor after explosion, and responds at off screen
explosion_one = Actor('explosion_one.png')                        #the meteor moves and spins. Laser blows in most of the places it hits.
                  
def draw():
    screen.clear()
    laser.draw()
    ship.draw()
    big_asteroid.draw()
    if keyboard.space: 
        update_laser()

def update_laser(): 
    laser.image = 'redlaser.png'
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)
    
def update_ship():
    if keyboard.left:
        ship.x -=10
    if keyboard.right:
        ship.x +=10

def big_asteroid_normal():
    
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (400, 0)

def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 1.0)
    
def update():
    big_asteroid.angle += 1
    big_asteroid.y += 1
    update_ship()
    
    if keyboard.space:
        update_laser()

    if laser.collidepoint(big_asteroid.center) or laser.collidepoint(big_asteroid.midbottom) or laser.collidepoint(big_asteroid.bottomright) or laser.collidepoint(big_asteroid. bottomleft) or laser.collidepoint(big_asteroid.midright) or laser.collidepoint(big_asteroid.midleft) or laser.collidepoint(big_asteroid.topleft) or laser.collidepoint(big_asteroid.midtop) or laser.collidepoint(big_asteroid.topright):
        update_big_asteroid_explode()
        laser.image = "invisable_laser.png"
'''
#Version 10
'''
ship = Actor('ship3.png', center = (400, 500))                 #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))       #This also draws one asteroid, and explodes (image and sound) when hit. Laser does not travel through asteroid
invisible_laser = Actor('invisable_laser.png')
big_asteroid = Actor('big_meteor.png', center = (400, -50))    #the meteor changes back into a meteor after explosion, and responds at a random spot off screen
explosion_one = Actor('explosion_one.png')                     #the meteor moves and spins. Laser blows in most of the places it hits. 
                                                               #BUGS: when ship moves before firing, laser stays in place.
def draw():                                                    #laser does not destroy asteroid everytime due to "holes" in asteroid sprite.
    screen.clear()
    laser.draw()
    ship.draw()
    big_asteroid.draw()
    if keyboard.space: 
        update_laser()

def update_laser(): 
    laser.image = 'redlaser.png'
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)
    
def update_ship():
    if keyboard.left:
        ship.x -=10
    if keyboard.right:
        ship.x +=10

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 1.0)
    
def update():
    big_asteroid.angle += 1
    big_asteroid.y += 1
    update_ship()
    
    if keyboard.space:
        update_laser()

    if laser.collidepoint(big_asteroid.center) or laser.collidepoint(big_asteroid.midbottom) or laser.collidepoint(big_asteroid.bottomright) or laser.collidepoint(big_asteroid. bottomleft) or laser.collidepoint(big_asteroid.midright) or laser.collidepoint(big_asteroid.midleft) or laser.collidepoint(big_asteroid.topleft) or laser.collidepoint(big_asteroid.midtop) or laser.collidepoint(big_asteroid.topright):
        update_big_asteroid_explode()
        laser.image = "invisable_laser.png"

    if big_asteroid.y > 650:
        big_asteroid_normal()
'''
#Version 11
'''
ship = Actor('ship3.png', center = (400, 500))                 #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))       #This also draws one asteroid, and explodes (image and sound) when hit. Laser does not travel through asteroid
invisible_laser = Actor('invisable_laser.png')
big_asteroid = Actor('big_meteor.png', center = (400, -50))    #the meteor changes back into a meteor after explosion, and responds at a random spot off screen
explosion_one = Actor('explosion_one.png')                     #the meteor moves and spins. Laser blows in most of the places it hits. 
                                                               #BUGS: laser does not destroy asteroid everytime due to "holes" in asteroid sprite.
def draw():                                                    
    screen.clear()
    laser.draw()
    ship.draw()
    big_asteroid.draw()
    if keyboard.space: 
        update_laser()

def update_laser(): 
    laser.image = 'redlaser.png'
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 1.0)
    
def update():
    big_asteroid.angle += 1
    big_asteroid.y += 1
    update_ship()
    
    if keyboard.space:
        update_laser()

    if laser.collidepoint(big_asteroid.center) or laser.collidepoint(big_asteroid.midbottom) or laser.collidepoint(big_asteroid.bottomright) or laser.collidepoint(big_asteroid. bottomleft) or laser.collidepoint(big_asteroid.midright) or laser.collidepoint(big_asteroid.midleft) or laser.collidepoint(big_asteroid.topleft) or laser.collidepoint(big_asteroid.midtop) or laser.collidepoint(big_asteroid.topright):
        update_big_asteroid_explode()
        laser.image = "invisable_laser.png"

    if big_asteroid.y > 650:
        big_asteroid_normal()
'''
#Version 12
'''
ship = Actor('ship3.png', center = (400, 500))                 #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))       #This also draws one asteroid, and explodes (image and sound) when hit. Laser does not travel through asteroid
invisible_laser = Actor('invisable_laser.png')
big_asteroid = Actor('big_meteor.png', center = (400, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    #the meteor changes back into a meteor after explosion, and responds at a random spot off screen
explosion_one = Actor('explosion_one.png')                     #the meteor moves and spins. Laser blows in most of the places it hits. 
                                                               
def draw():                                                    
    screen.clear()
    laser.draw()
    ship.draw()
    big_asteroid.draw()
    big_asteroid_two.draw()
    if keyboard.space: 
        update_laser()

def update_laser(): 
    laser.image = 'redlaser.png'
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

def big_asteroid_two_normal():
    num = random.randint(50,450)
    big_asteroid_two.image = 'big_meteor.png'
    big_asteroid_two.center = (num, -50)

def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 1.0)

def update_big_asteroid_two_explode():
    sounds.largebang.play()
    big_asteroid_two.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_two_normal, 1.0)
    
def update():
    big_asteroid.angle += 1
    big_asteroid.y += 1
    big_asteroid_two.angle +=1
    big_asteroid_two.y +=1
    update_ship()
    
    if keyboard.space:
        update_laser()

    if laser.colliderect(big_asteroid):
        update_big_asteroid_explode()
        laser.image = "invisable_laser.png"

    if laser.colliderect(big_asteroid_two):
        update_big_asteroid_two_explode()
        laser.image = "invisable_laser.png"

    if big_asteroid.y > 650:
        big_asteroid_normal()
'''
#Version 13
'''
ship = Actor('ship3.png', center = (400, 500))                 #This module has a blank background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #This also draws two asteroid, and explodes (image and sound) when hit. Laser does not travel through asteroid
invisible_laser = Actor('invisable_laser.png')
#define Actor: ship_explosion

big_asteroid = Actor('big_meteor.png', center = (400, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
explosion_one = Actor('explosion_one.png')                        #the meteors moves and spins. Laser blows at all places it hits. 

#define Actor: medium_asteriod
#define Actor: medium_asteroid_two
#define Actor: explosion_two

#define Actor: small_asteroid
#define Actor: small asteroid_two
#define Actor: explosion_three

                                                #Actors draw
def draw(): 
                                                        
    screen.clear()
    #screen.blit('space_background.png', (0,0))  
    laser.draw()
    ship.draw()
                                            
    big_asteroid.draw()
    big_asteroid_two.draw()
    #medium_asteriod.draw()
    #medium_asteroid_two.draw()
    #small_asteroid.draw()
    #small_asteroid_two.draw()

    if keyboard.space: 
        update_laser()
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))
 
                                                #Asteroid reset normal 
def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

def big_asteroid_two_normal():
    num = random.randint(50,450)
    big_asteroid_two.image = 'big_meteor.png'
    big_asteroid_two.center = (num + 100, -50)

def medium_asteroid_normal():
    #num = random.randint(50,450)
    #define image
    #define location
    pass

def medium_asteroid_two_normal():
    #num = random.randint(50,450)
    #define image
    #define location
    pass

def small_asteroid_normal():
    #num = random.randint(50,450)
    #define image
    #define location
    pass

def small_asteroid_two_normal():
    #num = random.randint(50,450)
    #define image
    #define location
    pass
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 1.0)

def update_big_asteroid_two_explode():
    sounds.largebang.play()
    big_asteroid_two.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_two_normal, 1.0)

def update_medium_asteroid_explode():
    #define sound
    #define explode image
    #clock reset to normal
    pass

def update_medium_asteroid_two_explode():
    #define sound
    #define explode image
    #clock reset to normal
    pass

def update_small_asteroid_explode():
    #define sound
    #define explode image
    #clock reset to normal
    pass

def update_small_asteroid_two_explode():
    #define sound
    #define explode image
    #clock reset to normal
    pass
                                                #updates
def update_laser(): 
    laser.image = 'redlaser.png' 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0:
        laser.pos = (ship.x,ship.y)

def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

score = 0                                       #main game loop
def update():
    global score     
                                                #asteroid updates
    big_asteroid.angle += 1
    big_asteroid.y += 1
    big_asteroid_two.angle +=1
    big_asteroid_two.y +=1
    #medium_asteroid.angle += 1
    #medium_asteroid.y += 1
    #medium_asteroid_two.angle += 1
    #medium_asteroid_two.y += 1
    #small_asteroid.angle += 1
    #small_asteroid.y += 1
    #small_asteroid_two.angle += 1
    #small_asteroid_two.y += 1
    update_ship()

    if keyboard.space:
        update_laser()

    if laser.colliderect(big_asteroid):
        update_big_asteroid_explode()
        laser.image = 'invisable_laser.png'
        score +=1
        #laser.opacity = 0.0

    if laser.colliderect(big_asteroid_two):
        update_big_asteroid_two_explode()
        laser.image = 'invisable_laser.png'
        score +=1
        #laser.opacity = 0.0   

    #if laser.colliderect(medium_asteroid):
        #update_medium_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        #score +=1

    #if laser.colliderect(medium_asteroid_two):
        #update_medium_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        #score +=1

    #if laser.colliderect(small_asteroid):
        #update_small_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        #score +=1

    #if laser.colliderect(small_asteroid_two):
        #update_small_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        #score +=1
       
    if big_asteroid.y > 650:
        big_asteroid_normal()
        score -= 14

    if big_asteroid_two.y > 650:
        big_asteroid_two_normal()
        score -= 14
    
    #if medium_asteroid.y > 650:
        #medium_asteroid_normal()
        #score -= 14

    #if medium_asteroid_two.y > 650:
        #medium_asteroid_two_normal()
        #score -= 14

    #if small_asteroid.y > 650:
        #small_asteroid_normal()
        #score -= 14

    #if small_asteroid_two.y > 650:
        #small_asteroid_two_normal()
        #score -= 14       
pgzrun.go()
'''
#Version 14
'''                                             #Trying to build menu. When spacebar is hit, ship is drawn. But doesnt move.
ship = Actor('ship3.png', center = (400, 500)) 
status = 0  
def draw():
    global status                                           
    
    #string = 'Menu'
    screen.draw.text(str('menu'), color ='green', center = (250,250))

    if keyboard.space:
        status += 1
    #screen.blit('space_background.png', (0,0))
     
    if status == 1:
        
        screen.clear()
        #string = ''
        ship.draw()
        
def update_ship():
    if keyboard.left:
        ship.x -=10
        
    if keyboard.right:
        ship.x +=10
        

def update():
    update_ship()
pgzrun.go()
'''
#Version 15
'''
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
invisible_laser = Actor('invisable_laser.png')                  #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#define Actor: ship_explosion                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed. 
big_asteroid = Actor('big_meteor.png', center = (400, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png') 
                                                                   
medium_asteroid = Actor('meteor_med.png', center = (200, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (250, -50))
explosion_two = Actor('explosion_two.png')

small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (425, -50))
#define Actor: explosion_three

                                                #Actors draw
def draw(): 
                                                        
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    laser.draw()
    ship.draw()
                                            
    big_asteroid.draw()
    big_asteroid_two.draw()
    medium_asteroid.draw()
    medium_asteroid_two.draw()
    small_asteroid.draw()
    small_asteroid_two.draw()

    if keyboard.space: 
        update_laser()
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))
 
                                                #Asteroid reset normal 
def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
    
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.25)
    

def update_big_asteroid_two_explode():
    sounds.largebang.play()
    big_asteroid_two.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_two_normal, 0.25)
    
def update_medium_asteroid_explode():
    sounds.mediumbang.play()
    medium_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_normal, 0.25)
    

def update_medium_asteroid_two_explode():
    sounds.mediumbang.play()
    medium_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_two_normal, 0.25)
    

def update_small_asteroid_explode():
    sounds.smallbang.play()
    small_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_normal, 0.25)
    

def update_small_asteroid_two_explode():
    sounds.smallbang.play()
    small_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_two_normal, 0.25)
    
                                                #updates
def update_laser(): 
    laser.image = 'redlaser.png' 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0 or laser.colliderect(big_asteroid) or laser.colliderect(big_asteroid_two) or laser.colliderect(medium_asteroid) or laser.colliderect(medium_asteroid_two):
        laser.pos = (ship.x,ship.y)

def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

score = 0 
speed = 0.5 
                              #main game loop
def update():
    global speed
    global score     
    #if score > 100:
        #speed += 0.25 
        #print(speed)
    #elif score > 200:
        #speed += 0.25
        #print(speed)                                           #asteroid updates
    big_asteroid.angle += 1
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

    if keyboard.space:
        update_laser()

    if laser.colliderect(big_asteroid):
        update_big_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0005
        #print(speed)
        #laser.opacity = 0.0

    if laser.colliderect(big_asteroid_two):
        update_big_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0005
        #print(speed)
        #laser.opacity = 0.0   

    if laser.colliderect(medium_asteroid):
        update_medium_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.00025
        #print(speed)

    if laser.colliderect(medium_asteroid_two):
        update_medium_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.00025

    if laser.colliderect(small_asteroid):
        update_small_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0001

    if laser.colliderect(small_asteroid_two):
        update_small_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0001
       
    if big_asteroid.y > 650:
        big_asteroid_normal()
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
pgzrun.go()
'''
#Version 16
'''
#ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise.
ship = Actor('millennium_falcon.png', center = (400, 500))      #This module has a menu, and it disappears once the game is started
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
invisible_laser = Actor('invisable_laser.png')                  #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#define Actor: ship_explosion                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed. 
big_asteroid = Actor('big_meteor.png', center = (400, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png') 
                                                                   
medium_asteroid = Actor('meteor_med.png', center = (200, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (250, -50))
explosion_two = Actor('explosion_two.png')

small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (425, -50))
#define Actor: explosion_three

                                                #Actors draw
def draw(): 
                                                        
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    laser.draw()
    ship.draw()
                                            
    big_asteroid.draw()
    big_asteroid_two.draw()
    medium_asteroid.draw()
    medium_asteroid_two.draw()
    small_asteroid.draw()
    small_asteroid_two.draw()

    if keyboard.space: 
        update_laser()
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    menu_pos_x = 400
    menu_pos_y = 400
    
    if game >=1:
        #menu_color = 'blue'
        menu_pos_x += 1000         #This 'removes' the menu screen one 'A' is pressed 
    

    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))
    screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (menu_pos_x, menu_pos_y-25))
    screen.draw.text(str('Press "A" to begin'), color = 'Yellow', center = (menu_pos_x, menu_pos_y))
                                                #Asteroid reset normal 
def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
    
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.25)
    

def update_big_asteroid_two_explode():
    sounds.largebang.play()
    big_asteroid_two.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_two_normal, 0.25)
    
def update_medium_asteroid_explode():
    sounds.mediumbang.play()
    medium_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_normal, 0.25)
    

def update_medium_asteroid_two_explode():
    sounds.mediumbang.play()
    medium_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_two_normal, 0.25)
    

def update_small_asteroid_explode():
    sounds.smallbang.play()
    small_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_normal, 0.25)
    

def update_small_asteroid_two_explode():
    sounds.smallbang.play()
    small_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_two_normal, 0.25)
    
                                                #updates
#def on_mouse_down(pos):                                        #This will be used to allow the user to select a ship
    #if ship.collidepoint(pos):
        #print('test')

def update_game():
    global game
    if keyboard.A:
        game +=1
        

def update_laser(): 
    laser.image = 'redlaser.png' 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0 or laser.colliderect(big_asteroid) or laser.colliderect(big_asteroid_two) or laser.colliderect(medium_asteroid) or laser.colliderect(medium_asteroid_two):
        laser.pos = (ship.x,ship.y)

def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

score = 0 
speed = 0.5 
game = 0                             #main game loop
def update():
    global speed
    global score 
    global game    
    #if score > 100:
        #speed += 0.25 
        #print(speed)
    #elif score > 200:
        #speed += 0.25
        #print(speed)
    update_game()
    if game >=1:                                           #asteroid updates
        big_asteroid.angle += 1
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

    if keyboard.space:
        update_laser()

    if laser.colliderect(big_asteroid):
        update_big_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0005
        #print(speed)
        #laser.opacity = 0.0

    if laser.colliderect(big_asteroid_two):
        update_big_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0005
        #print(speed)
        #laser.opacity = 0.0   

    if laser.colliderect(medium_asteroid):
        update_medium_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.00025
        #print(speed)

    if laser.colliderect(medium_asteroid_two):
        update_medium_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.00025

    if laser.colliderect(small_asteroid):
        update_small_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0001

    if laser.colliderect(small_asteroid_two):
        update_small_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0001
       
    if big_asteroid.y > 650:
        big_asteroid_normal()
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
pgzrun.go()
'''
#Version 17
'''
#ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise.
ship_image = 'millennium_falcon.png'                              #This version has a menu.
ship = Actor(ship_image, center = (400, 500))
#ship_image_one = 'millennium_falcon.png'
#ship_image_two = 'ship3.png'

laser = Actor('redlaser.png', center = (ship.x, ship.y))        #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
invisible_laser = Actor('invisable_laser.png')                  #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#define Actor: ship_explosion                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed. 
big_asteroid = Actor('big_meteor.png', center = (400, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png') 
                                                                   
medium_asteroid = Actor('meteor_med.png', center = (200, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (250, -50))
explosion_two = Actor('explosion_two.png')

small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (425, -50))
#define Actor: explosion_three

                                                #Actors draw
def draw(): 
                                                        
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    laser.draw()
    ship.draw()
                                            
    big_asteroid.draw()
    big_asteroid_two.draw()
    medium_asteroid.draw()
    medium_asteroid_two.draw()
    small_asteroid.draw()
    small_asteroid_two.draw()

    if keyboard.space: 
        update_laser()
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    menu_pos_x = 400
    menu_pos_y = 400
    
    if game >=1:
        #menu_color = 'blue'
        menu_pos_x += 1000         #This 'removes' the menu screen one 'A' is pressed 
    

    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))
    screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (menu_pos_x, menu_pos_y-25))
    screen.draw.text(str('Press "A" to begin'), color = 'Yellow', center = (menu_pos_x, menu_pos_y))
                                                #Asteroid reset normal 
def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
    
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.25)
    

def update_big_asteroid_two_explode():
    sounds.largebang.play()
    big_asteroid_two.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_two_normal, 0.25)
    
def update_medium_asteroid_explode():
    sounds.mediumbang.play()
    medium_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_normal, 0.25)
    

def update_medium_asteroid_two_explode():
    sounds.mediumbang.play()
    medium_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_two_normal, 0.25)
    

def update_small_asteroid_explode():
    sounds.smallbang.play()
    small_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_normal, 0.25)
    

def update_small_asteroid_two_explode():
    sounds.smallbang.play()
    small_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_two_normal, 0.25)
    
                                                #updates
#def on_mouse_down(pos):
    #global ship_image                                        #This will be used to allow the user to select a ship
    #if ship.collidepoint(pos):
        #ship_image == ship_image_two
        #print('test')

def update_game():
    global game
    global ship_image
    #if keyboard.A:
        #ship_image = 'millennium_falcon.png'
    #if keyboard.B:
        #ship_image = 'ship3.png'
    if keyboard.A:
        game +=1
        

def update_laser(): 
    laser.image = 'redlaser.png' 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0 or laser.colliderect(big_asteroid) or laser.colliderect(big_asteroid_two) or laser.colliderect(medium_asteroid) or laser.colliderect(medium_asteroid_two):
        laser.pos = (ship.x,ship.y)

def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

score = 0 
speed = 0.5 
game = 0                             #main game loop
def update():
    global speed
    global score 
    global game    
    #if score > 100:
        #speed += 0.25 
        #print(speed)
    #elif score > 200:
        #speed += 0.25
        #print(speed)
    update_game()
    if game >=1:                                           #asteroid updates
        big_asteroid.angle += 1
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

    if keyboard.space:
        update_laser()

    if laser.colliderect(big_asteroid):
        update_big_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0005
        #print(speed)
        #laser.opacity = 0.0

    if laser.colliderect(big_asteroid_two):
        update_big_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0005
        #print(speed)
        #laser.opacity = 0.0   

    if laser.colliderect(medium_asteroid):
        update_medium_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.00025
        #print(speed)

    if laser.colliderect(medium_asteroid_two):
        update_medium_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.00025

    if laser.colliderect(small_asteroid):
        update_small_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0001

    if laser.colliderect(small_asteroid_two):
        update_small_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0001
       
    if big_asteroid.y > 650:
        big_asteroid_normal()
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
pgzrun.go()
'''
#Version 18
'''
ship = Actor('ship3.png', center = (400, 500))                     #This module has a stary background. The ship moves and shoots with noise.
#ship_image = 'millennium_falcon.png'                              #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                     #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                          #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                      #the meteors moves and spins. Laser blows at all places it hits.
                                                                   #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))           #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  
ship_explosion = Actor('explosion_one.png')                                   
                                                                 
big_asteroid = Actor('big_meteor.png', center = (400, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png') 
                                                                   
medium_asteroid = Actor('meteor_med.png', center = (200, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (250, -50))
explosion_two = Actor('explosion_two.png')

small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (425, -50))
#define Actor: explosion_three

                                                #Actors draw
def draw(): 
                                                        
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    laser.draw()
    ship.draw()
                                            
    big_asteroid.draw()
    big_asteroid_two.draw()
    medium_asteroid.draw()
    medium_asteroid_two.draw()
    small_asteroid.draw()
    small_asteroid_two.draw()

    if keyboard.space: 
        update_laser()
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    menu_pos_x = 400
    menu_pos_y = 400

    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
    
    if game == True:                                                                                                         #game
        #menu_color = 'blue'
        menu_pos_x += 1000         #This 'removes' the menu screen one 'A' is pressed 
    

    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))
    if game == False:
        #ship.image = 'ship3.png'
        ship.center = (400, 500)

        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (menu_pos_x, menu_pos_y-25))
        screen.draw.text(str('Press "A" to begin'), color = 'Yellow', center = (menu_pos_x, menu_pos_y))
                                                #Asteroid reset normal 
def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
    #ship.center = (ship.x, 500))
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.25)
    

def update_big_asteroid_two_explode():
    sounds.largebang.play()
    big_asteroid_two.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_two_normal, 0.25)
    
def update_medium_asteroid_explode():
    sounds.mediumbang.play()
    medium_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_normal, 0.25)
    

def update_medium_asteroid_two_explode():
    sounds.mediumbang.play()
    medium_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_two_normal, 0.25)
    

def update_small_asteroid_explode():
    sounds.smallbang.play()
    small_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_normal, 0.25)
    

def update_small_asteroid_two_explode():
    sounds.smallbang.play()
    small_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_two_normal, 0.25)

def update_ship_explode():   
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    
    game = False  
    #clock.schedule_unique(game_restart, 3)                                                                                #Game
    print(game) 
    #update_game()
def game_restart():
    ship.image = 'ship3.png' 
    game = False
    print(game)
    
                                                #updates
#def on_mouse_down(pos):
    #global ship_image                                        #This will be used to allow the user to select a ship
    #if ship.collidepoint(pos):
        #ship_image == ship_image_two
        #print('test')

def update_game():
    global game
    global ship_image
    global score
    #ship.image = 'ship3.png'
    #if keyboard.A:
        #ship_image = 'millennium_falcon.png'
    #if keyboard.B:
        #ship_image = 'ship3.png'
    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png' 
        score = 0

def update_laser(): 
    laser.image = 'redlaser.png' 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0 or laser.colliderect(big_asteroid) or laser.colliderect(big_asteroid_two) or laser.colliderect(medium_asteroid) or laser.colliderect(medium_asteroid_two):
        laser.pos = (ship.x,ship.y)

def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

score = 0 
speed = 0.5 
game = False                             #main game loop                                       #Game
def update():
    global speed
    global score 
    global game    
    #if score > 100:
        #speed += 0.25 
        #print(speed)
    #elif score > 200:
        #speed += 0.25
        #print(speed)
    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

    if keyboard.space:
        update_laser()

    if laser.colliderect(big_asteroid):
        update_big_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0005
        #print(speed)
        #laser.opacity = 0.0

    if laser.colliderect(big_asteroid_two):
        update_big_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0005
        #print(speed)
        #laser.opacity = 0.0   

    if laser.colliderect(medium_asteroid):
        update_medium_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.00025
        #print(speed)

    if laser.colliderect(medium_asteroid_two):
        update_medium_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.00025

    if laser.colliderect(small_asteroid):
        update_small_asteroid_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0001

    if laser.colliderect(small_asteroid_two):
        update_small_asteroid_two_explode()
        #laser.image = 'invisable_laser.png'
        score +=1
        speed += 0.0001

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        #update_game()

    if big_asteroid.y > 650:
        big_asteroid_normal()
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
pgzrun.go()
'''
#Version 19
'''
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                                   
                                                                 
big_asteroid = Actor('big_meteor.png', center = (600, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png') 
                                                                   
medium_asteroid = Actor('meteor_med.png', center = (50, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (500, -50))
explosion_two = Actor('explosion_two.png')

small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (700, -50))

                                                #Actors draw
def draw(): 
                                                    
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    laser.draw()
    ship.draw()
                                            
    big_asteroid.draw()
    big_asteroid_two.draw()
    medium_asteroid.draw()
    medium_asteroid_two.draw()
    small_asteroid.draw()
    small_asteroid_two.draw()

    if keyboard.space: 
        update_laser()
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.25)
    
def update_big_asteroid_two_explode():
    sounds.largebang.play()
    big_asteroid_two.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_two_normal, 0.25)
    
def update_medium_asteroid_explode():
    sounds.mediumbang.play()
    medium_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_normal, 0.25)
    
def update_medium_asteroid_two_explode():
    sounds.mediumbang.play()
    medium_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_two_normal, 0.25)
    
def update_small_asteroid_explode():
    sounds.smallbang.play()
    small_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_normal, 0.25)
    
def update_small_asteroid_two_explode():
    sounds.smallbang.play()
    small_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_two_normal, 0.25)

def update_ship_explode():   
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    game = False
                                              #updates
#def on_mouse_down(pos):
    #global ship_image                                        #This will be used to allow the user to select a ship
    #if ship.collidepoint(pos):
        #ship_image == ship_image_two
        #print('test')

def update_game():
    global game
    global ship_image
    global score
    global menu
    #ship.image = 'ship3.png'
    #if keyboard.A:
        #ship_image = 'millennium_falcon.png'
    #if keyboard.B:
        #ship_image = 'ship3.png'
    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png' 
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def update_laser(): 
    laser.image = 'redlaser.png' 
    sounds.fire.play()
    animate(laser, pos = (ship.x +0, ship.y -1000))
    if laser.y < 0 or laser.colliderect(big_asteroid) or laser.colliderect(big_asteroid_two) or laser.colliderect(medium_asteroid) or laser.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two):
        laser.pos = (ship.x,ship.y)

def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

score = 0 
speed = 0.5 
game = False 
menu = False 
                           #main game loop                                       #Game
def update():
    global speed
    global score 
    global game    
    
    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

    if keyboard.space:
        update_laser()

    if laser.colliderect(big_asteroid):
        update_big_asteroid_explode()
        score +=1
        speed += 0.0005
        
    if laser.colliderect(big_asteroid_two):
        update_big_asteroid_two_explode()
        score +=1
        speed += 0.0005 

    if laser.colliderect(medium_asteroid):
        update_medium_asteroid_explode()
        score +=1
        speed += 0.00025

    if laser.colliderect(medium_asteroid_two):
        update_medium_asteroid_two_explode()
        score +=1
        speed += 0.00025

    if laser.colliderect(small_asteroid):
        update_small_asteroid_explode()
        score +=1
        speed += 0.0001

    if laser.colliderect(small_asteroid_two):
        update_small_asteroid_two_explode()
        score +=1
        speed += 0.0001

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  
pgzrun.go()
'''
#Version 20
'''
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #This version has a much faster laser.            
                                                                 
big_asteroid = Actor('big_meteor.png', center = (600, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png') 
                                                                   
medium_asteroid = Actor('meteor_med.png', center = (50, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (500, -50))
explosion_two = Actor('explosion_two.png')

small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (700, -50))

list =[]                                              #Actors draw
def draw(): 
                                                    
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
    ship.draw()
    global list
    for i in range(len(list)):
        #print('test')
        list[i].draw()
        animate(list[i], pos = (ship.x +0, ship.y -1000))
                                       
    big_asteroid.draw()
    big_asteroid_two.draw()
    medium_asteroid.draw()
    medium_asteroid_two.draw()
    small_asteroid.draw()
    small_asteroid_two.draw()

                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.05)     #originally 0.25
    
def update_big_asteroid_two_explode():
    sounds.largebang.play()
    big_asteroid_two.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_two_normal, 0.05)
    
def update_medium_asteroid_explode():
    sounds.mediumbang.play()
    medium_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_normal, 0.05)
    
def update_medium_asteroid_two_explode():
    sounds.mediumbang.play()
    medium_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(medium_asteroid_two_normal, 0.05)
    
def update_small_asteroid_explode():
    sounds.smallbang.play()
    small_asteroid.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_normal, 0.05)
    
def update_small_asteroid_two_explode():
    sounds.smallbang.play()
    small_asteroid_two.image = 'explosion_two.png'
    clock.schedule_unique(small_asteroid_two_normal, 0.05)

def update_ship_explode():   
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    game = False
                                              #updates
#def on_mouse_down(pos):
    #global ship_image                                        #This will be used to allow the user to select a ship
    #if ship.collidepoint(pos):
        #ship_image == ship_image_two
        #print('test')

def update_game():
    global game
    global ship_image
    global score
    global menu
    #ship.image = 'ship3.png'
    #if keyboard.A:
        #ship_image = 'millennium_falcon.png'
    #if keyboard.B:
        #ship_image = 'ship3.png'
    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png' 
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))


def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

score = 0 
speed = 0.5 
game = False 
menu = False 
                           #main game loop                                       #Game
def update():
    global speed
    global score 
    global game 
    global list   
    
    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.001
            
        if item.colliderect(big_asteroid_two):
            update_big_asteroid_two_explode()
            score +=1
            speed += 0.001

        if item.colliderect(medium_asteroid):
            update_medium_asteroid_explode()
            score +=1
            speed += 0.001

        if item.colliderect(medium_asteroid_two):
            update_medium_asteroid_two_explode()
            score +=1
            speed += 0.001

        if item.colliderect(small_asteroid):
            update_small_asteroid_explode()
            score +=1
            speed += 0.001

        if item.colliderect(small_asteroid_two):
            update_small_asteroid_two_explode()
            score +=1
            speed += 0.001

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        score = 0

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  
pgzrun.go()
'''
'''
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #THis module deletes all laser actors after each round to prevent lag            
#Bolt = Actor('bolt_gold.png')

big_asteroid = Actor('big_meteor.png', center = (600, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png') 
                                                                   
medium_asteroid = Actor('meteor_med.png', center = (50, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (500, -50))
explosion_two = Actor('explosion_two.png')

small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (700, -50))

def draw_laser(i):
    list[i].draw()
    animate(list[i], pos = (ship.x +0, ship.y -1000))                

list =[]                                              #Actors draw
def draw():                                              
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
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
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
        #score = 0
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     #originally 0.25 then 0.05
    
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
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    game = False
                                              #updates
def update_game():
    global game
    global ship_image
    global score
    global menu

    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png' 
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

score = 0 
speed = 0.5 
game = False 
menu = False 
                           #main game loop                                       #Game
def update():
    global speed
    global score 
    global game 
    global list   
    
    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.01          #originally 0.001
            
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

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= []  

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  
pgzrun.go()
'''
'''
score = 0
def on_mouse_down(pos):
    global score                  #need "global" in order to have information sent from window to program
    if alien.collidepoint(pos):
        score +=1                 #score wont work without 'global score'
    else:
        print('You Missed')
        score -=1
    print(score)

ghost = Actor('ghost')
ghost.opacity = 0.5
'''
'''
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #THis module deletes all laser actors after each round to prevent lag            
Bolt = Actor('bolt_gold.png', center = (400,-50))               #THis module also draws a Bold at score > 100. If ship touches bolt, asteroids slow down.

big_asteroid = Actor('big_meteor.png', center = (600, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png') 
                                                                   
medium_asteroid = Actor('meteor_med.png', center = (50, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (500, -50))
explosion_two = Actor('explosion_two.png')

small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (700, -50))

def draw_laser(i):
    list[i].draw()
    animate(list[i], pos = (ship.x +0, ship.y -1000))                

list =[]                                              #Actors draw
def draw():                                              
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
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
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'
    global Bolt_speed
    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
        Bolt_speed = 0.5
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
        #score = 0
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     #originally 0.25 then 0.05
    
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
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    game = False
                                              #updates
def update_game():
    global game
    global ship_image
    global score
    global menu

    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png' 
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def bolt_perk():
    Bolt.draw()
    Bolt.y += Bolt_speed

score = 0 
speed = 0.5 
Bolt_speed = 0.5
game = False 
menu = False 
                           #main game loop                                       #Game
def update():
    global speed
    global Bolt_speed
    global score 
    global game 
    global list   
    
    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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
        if score > 100:
            bolt_perk()

    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.01          #originally 0.001
            
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

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= [] 

    if ship.colliderect(Bolt):
        speed = 0.5
        Bolt.pos = (400,-50)
        Bolt_speed = 0

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  
pgzrun.go()
'''
'''
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #THis module deletes all laser actors after each round to prevent lag            
Bolt = Actor('bolt_gold.png', center = (400,-50))               #THis module also draws a Bold at score > 100. If ship touches bolt, asteroids slow down.
                                                                 #An enemy ship appears, but does not do anything yet
enemy_ship = Actor('millennium_falcon.png', center = (400,-60))
big_asteroid = Actor('big_meteor.png', center = (600, -50))
big_asteroid_two = Actor('big_meteor.png', center = (300, -50))    
explosion_one = Actor('explosion_one.png') 
                                                                   
medium_asteroid = Actor('meteor_med.png', center = (50, -50))
medium_asteroid_two = Actor('meteor_med.png', center = (500, -50))
explosion_two = Actor('explosion_two.png')

small_asteroid = Actor('meteor_small.png', center = (150, -50))
small_asteroid_two = Actor('meteor_small.png', center = (700, -50))

def draw_laser(i):
    list[i].draw()
    animate(list[i], pos = (ship.x +0, ship.y -1000))                

list =[]                                              #Actors draw
def draw():                                              
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
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
    enemy_ship.draw()
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    global Bolt_speed
    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
        Bolt_speed = 0.5
        Bolt.pos = (400,-50)
        enemy_ship.pos = (400,-60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
        #score = 0
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     #originally 0.25 then 0.05
    
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
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    game = False
                                              #updates
def update_game():
    global game
    global ship_image
    global score
    global menu

    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png' 
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def bolt_perk():
    Bolt.draw()
    Bolt.y += Bolt_speed

def enemy():
    animate(enemy_ship, pos = (enemy_ship.x, enemy_ship.y + 200))
    
#def enemy_manuever():
    #enemy_ship.pos = (ship.x, enemy_ship.y)
    #animate(enemy_ship, pos = (ship.x, enemy_ship.y))
        #enemy_ship.x + 1
        #animate(enemy_ship, pos = (enemy_ship.x - 50 , enemy_ship.y))

score = 0 
speed = 0.5 
Bolt_speed = 0.5
game = False 
menu = False 
                           #main game loop                                       #Game
def update():
    global speed
    global Bolt_speed
    global score 
    global game 
    global list   
    
    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

        if score > 100:
            bolt_perk()
        
        if score == 100:
            enemy()

    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.01          #originally 0.001
            
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

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= [] 

    if ship.colliderect(Bolt):
        speed = 0.5
        Bolt.pos = (400,-50)
        Bolt_speed = 0

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  
pgzrun.go()
'''
'''
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #THis module deletes all laser actors after each round to prevent lag            
Bolt = Actor('bolt_gold.png', center = (400,-50))               #THis module also draws a Bold at score > 100. If ship touches bolt, asteroids slow down.
                                                                 #An enemy ship appears, and shoots. lasers are harmless

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

def draw_laser(i):
    list[i].draw()
    animate(list[i], pos = (ship.x +0, ship.y -1000))                

list =[]                                              #Actors draw
def draw():                                              
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
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
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    global Bolt_speed
    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
        Bolt_speed = 0.5
        Bolt.pos = (400,-50)
        enemy_ship.pos = (400,-60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
        #score = 0
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     #originally 0.25 then 0.05
    
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
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    game = False
                                              #updates
def update_game():
    global game
    global ship_image
    global score
    global menu

    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png' 
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def bolt_perk():
    Bolt.draw()
    Bolt.y += Bolt_speed

def enemy():
    animate(enemy_ship, pos = (enemy_ship.x, enemy_ship.y + 200))

def enemy_attack():
    animate(enemy_laser, pos = (enemy_ship.x, enemy_ship.y + 1000))
    #enemy_ship.y += 1
    #if enemy_laser.y == 1000:
        #enemy_laser.y = enemy_ship.y
def enemy_left():
    animate(enemy_ship, pos = (enemy_ship.x +100, enemy_ship.y))
    #enemy_ship.x + 200
#def enemy_manuever():
    #enemy_ship.pos = (ship.x, enemy_ship.y)
    #animate(enemy_ship, pos = (ship.x, enemy_ship.y))
        #enemy_ship.x + 1
        #animate(enemy_ship, pos = (enemy_ship.x - 50 , enemy_ship.y))
def enemy_right():
    animate(enemy_ship, pos = (enemy_ship.x -200, enemy_ship.y))


score = 0 
speed = 0.5 
Bolt_speed = 0.5
game = False 
menu = False 
#boss = False                         #main game loop                                       #Game
def update():
    global speed
    global Bolt_speed
    global score 
    global game 
    global list   
    #global boss

    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

        if score > 100:
            bolt_perk()
        #if score >100:
            #boss = True
        
        #if boss == True:
            #enemy()
            #if enemy_ship.y >= 300:
                #boss = False
            #clock.schedule_unique(enemy_left , 1.0)
            
        if score == 100:   #250
            enemy()

        if score == 100:
            #for i in range(10):
            enemy_attack()

        if score ==100:   #250
            speed = 0
            big_asteroid.pos = (600, -100)
            big_asteroid_two.pos = (300, -100)                                                                 
            medium_asteroid.pos = (50, -100)
            medium_asteroid_two.pos = (500, -100)
            small_asteroid.pos = (150, -100)
            small_asteroid_two.pos= (700, -100)
            #enemy_left()
            #clock.schedule_unique(enemy_left , 1.0)
            #clock.schedule_unique(enemy_right , 4.0)
            #enemy_attack()
            
        if enemy_laser.y > 600:
            enemy_laser.pos = (enemy_ship.x, enemy_ship.y)
            enemy_attack()
            #clock.schedule_unique(enemy_attack, 1.0)

            #enemy_attack()

    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.01          #originally 0.001
            
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

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= [] 

    if ship.colliderect(Bolt):
        speed = 0.5
        Bolt.pos = (400,-50)
        Bolt_speed = 0

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  

pgzrun.go()
'''
'''
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #THis module deletes all laser actors after each round to prevent lag            
Bolt = Actor('bolt_gold.png', center = (400,-50))               #THis module also draws a Bold at score > 100. If ship touches bolt, asteroids slow down.
                                                                 #An enemy ship appears, and shoots. lasers destroy the user ship

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

def draw_laser(i):
    list[i].draw()
    animate(list[i], pos = (ship.x +0, ship.y -1000))                

list =[]                                              #Actors draw
def draw():                                              
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
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
                                               #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    global Bolt_speed
    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
        Bolt_speed = 0.5
        Bolt.pos = (400,-50)
        enemy_ship.pos = (400,-60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
        #score = 0
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     #originally 0.25 then 0.05
    
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
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    game = False
                                              #updates
def update_game():
    global game
    global ship_image
    global score
    global menu

    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png' 
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def bolt_perk():
    Bolt.draw()
    Bolt.y += Bolt_speed

def enemy():
    animate(enemy_ship, pos = (enemy_ship.x, enemy_ship.y + 200))

def enemy_attack():
    #sounds.fire.play()
    animate(enemy_laser, pos = (enemy_ship.x, enemy_ship.y + 1000))
    
#def enemy_left():
    #animate(enemy_ship, pos = (enemy_ship.x +100, enemy_ship.y))

#def enemy_right():
    #animate(enemy_ship, pos = (enemy_ship.x -200, enemy_ship.y))


score = 0 
speed = 0.5 
Bolt_speed = 0.5
game = False 
menu = False 
                         #main game loop                                       #Game
def update():
    global speed
    global Bolt_speed
    global score 
    global game 
    global list   
    

    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

        if score > 100:
            bolt_perk()
        #if score >100:
            #boss = True
        
        #if boss == True:
            #enemy()
            #if enemy_ship.y >= 300:
                #boss = False
            #clock.schedule_unique(enemy_left , 1.0)
            
        if score in range(100,103):   #250
            enemy()

        if score in range(100,103):
            #for i in range(10):
            sounds.fire.play()
            enemy_attack()

        if score ==100:   #250
            speed = 0
            big_asteroid.pos = (600, -100)
            big_asteroid_two.pos = (300, -100)                                                                 
            medium_asteroid.pos = (50, -100)
            medium_asteroid_two.pos = (500, -100)
            small_asteroid.pos = (150, -100)
            small_asteroid_two.pos= (700, -100)
            #enemy_left()
            #clock.schedule_unique(enemy_left , 1.0)
            #clock.schedule_unique(enemy_right , 4.0)
            #enemy_attack()
            
        if enemy_laser.y > 800 and score > 100:
            enemy_laser.pos = (enemy_ship.x, enemy_ship.y)
            enemy_attack()
            sounds.fire.play()
            
            #clock.schedule_unique(enemy_attack, 1.0)

            #enemy_attack()

    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.01          #originally 0.001
            
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

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two) or ship.colliderect(enemy_laser):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= [] 

    if ship.colliderect(Bolt):
        speed = 0.5
        Bolt.pos = (400,-50)
        Bolt_speed = 0

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  

pgzrun.go()
'''
'''
#ship = Actor('new_ship', center = (400, 500))
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #THis module deletes all laser actors after each round to prevent lag            
Bolt = Actor('bolt_gold.png', center = (400,-50))               #THis module also draws a Bold at score > 100. If ship touches bolt, asteroids slow down.
                                                                 #An enemy ship appears, and shoots. lasers destroy the user ship
                                                                #enemy ship takes damage. health is printed. 
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

def draw_laser(i):
    list[i].draw()
    animate(list[i], pos = (ship.x +0, ship.y -1000))                

list =[]                                              #Actors draw
def draw():   
    global score
    global boss
    global enemy_health                                           
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
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
    if score >=250 and boss == True:
        screen.draw.text(str('Enemy Health'), color = 'red', center = (400,25), fontname = 'walkway_black', fontsize =30)
        screen.draw.text(str(enemy_health), color = 'red', center = (400,50), fontname = 'walkway_black', fontsize =30)                                           #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    global Bolt_speed
    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
        Bolt_speed = 0.5
        Bolt.pos = (400,-50)
        enemy_ship.pos = (400,-60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
        #score = 0
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
    #ship.image = 'new_ship.png'  
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     #originally 0.25 then 0.05
    
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
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    #ship.image = 'new_ship.png'
    game = False
                                              #updates
def update_game():
    global game
    global ship_image
    global score
    global menu

    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png'
        #ship.image = 'new_ship.png'
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def bolt_perk():
    Bolt.draw()
    Bolt.y += Bolt_speed

def enemy():
    animate(enemy_ship, pos = (enemy_ship.x, enemy_ship.y + 200))

def enemy_attack():
    #sounds.fire.play()
    animate(enemy_laser, pos = (enemy_ship.x, enemy_ship.y + 1000))
#def enemy_left():
    #animate(enemy_ship, pos = (enemy_ship.x +100, enemy_ship.y))
#def enemy_right():
    #animate(enemy_ship, pos = (enemy_ship.x -200, enemy_ship.y))

score = 0 
speed = 0.5 
Bolt_speed = 1
game = False 
menu = False 
boss = False
enemy_health = 50                         #main game loop                                       #Game
def update():
    global speed
    global Bolt_speed
    global score 
    global game 
    global list
    global boss   
    global enemy_health

    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

        if score > 100:
            bolt_perk()
            
        if score in range(250,253):   #250
            boss = True
            enemy()

        if score >=250 and boss == True:
            enemy_attack()

        if score >=250:   #250
            speed = 0
            big_asteroid.pos = (600, -100)
            big_asteroid_two.pos = (300, -100)                                                                 
            medium_asteroid.pos = (50, -100)
            medium_asteroid_two.pos = (500, -100)
            small_asteroid.pos = (150, -100)
            small_asteroid_two.pos= (700, -100)
            
        if enemy_laser.y > 800 and score > 250 and boss == True:
            enemy_laser.pos = (enemy_ship.x, enemy_ship.y)
            enemy_attack()
            sounds.fire.play()
            
    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.01          #originally 0.001
            
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
            enemy_health -= 0.1
            #print(enemy_health)

        if item.colliderect(enemy_ship) and score >=250 and enemy_health <=0 and boss == True:
            enemy_ship.center = (400, -60)
            enemy_laser.center = (400,-60)
            boss = False
            score += 10
            speed = 3
            enemy_health = 30

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two) or ship.colliderect(enemy_laser):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= [] 
        screen.clear()

    if ship.colliderect(Bolt):
        speed = 0.5
        Bolt.pos = (400,-50)
        Bolt_speed = 0

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  

pgzrun.go()
'''

#ship = Actor('new_ship', center = (400, 500))
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #THis module deletes all laser actors after each round to prevent lag            
Bolt = Actor('bolt_gold.png', center = (400,-50))               #THis module also draws a Bold at score > 100. If ship touches bolt, asteroids slow down.
                                                                #An enemy ship appears, and shoots. lasers destroy the user ship
                                                                #enemy ship takes damage. health is printed. 
                                                                #Asteroids re appear after boss is destroyed, perks drop after.
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

def draw_laser(i):
    list[i].draw()
    animate(list[i], pos = (ship.x +0, ship.y -1000))                

list =[]                                              #Actors draw
def draw():   
    global score
    global boss
    global enemy_health                                           
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
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
    if score >=250 and boss == True:
        screen.draw.text(str('Enemy Health'), color = 'red', center = (400,25), fontname = 'walkway_black', fontsize =30)
        screen.draw.text(str(enemy_health), color = 'red', center = (400,50), fontname = 'walkway_black', fontsize =30)                                           #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    global Bolt_speed
    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
        Bolt_speed = 0.5
        Bolt.pos = (400,-50)
        enemy_ship.pos = (400,-60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
        #score = 0
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))
    
    
    if score > 600 and boss == False:       ######
        
        screen.clear()
        screen.blit('space_background.png', (0,0))
        big_asteroid.draw()
        big_asteroid_two.draw()
        medium_asteroid.draw()
        medium_asteroid_two.draw()
        small_asteroid.draw()
        small_asteroid_two.draw()
        Bolt.draw()
        enemy_laser.draw()
        enemy_ship.draw()
        ship.draw()
        
        for i in range(len(list)):
            draw_laser(i)

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
    #ship.image = 'new_ship.png'  
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     #originally 0.25 then 0.05
    
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
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    #ship.image = 'new_ship.png'
    game = False
                                              #updates
def update_game():
    global game
    global ship_image
    global score
    global menu

    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png'
        #ship.image = 'new_ship.png'
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def bolt_perk():
    Bolt.draw()
    Bolt.y += Bolt_speed

def enemy():
    animate(enemy_ship, pos = (enemy_ship.x, enemy_ship.y + 200))

def enemy_attack():
    #sounds.fire.play()
    animate(enemy_laser, pos = (enemy_ship.x, enemy_ship.y + 1000))
#def enemy_left():
    #animate(enemy_ship, pos = (enemy_ship.x +100, enemy_ship.y))
#def enemy_right():
    #animate(enemy_ship, pos = (enemy_ship.x -200, enemy_ship.y))

score = 0 
speed = 0.5 
Bolt_speed = 1
game = False 
menu = False 
boss = False
enemy_health = 50                         #main game loop                                       #Game
def update():
    global speed
    global Bolt_speed
    global score 
    global game 
    global list
    global boss   
    global enemy_health

    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

        if score > 600:
            bolt_perk()
            
        if score in range(250,253):   #250
            boss = True
            enemy()

        if score >=250 and boss == True:
            enemy_attack()

        if score >=250 and boss == True:   #250
            speed = 0
            big_asteroid.pos = (600, -100)
            big_asteroid_two.pos = (300, -100)                                                                 
            medium_asteroid.pos = (50, -100)
            medium_asteroid_two.pos = (500, -100)
            small_asteroid.pos = (150, -100)
            small_asteroid_two.pos= (700, -100)
            
        if enemy_laser.y > 800 and score > 250 and boss == True:
            enemy_laser.pos = (enemy_ship.x, enemy_ship.y)
            enemy_attack()
            sounds.fire.play()
            
    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)
    
    if keyboard.z:
        laser_system()

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.01          #originally 0.001
            
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
            enemy_health -= 0.1
            #print(enemy_health)

        if item.colliderect(enemy_ship) and score >=250 and enemy_health <=0 and boss == True:
            enemy_ship.center = (400, -60)
            enemy_laser.center = (400,-60)
            boss = False
            score += 10
            speed += 3
            enemy_health = 50
            screen.clear()

        if item.y <= -100:          ##############
            del list[0]

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two) or ship.colliderect(enemy_laser):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= [] 
        screen.clear()

    if ship.colliderect(Bolt):
        speed = 0.5
        Bolt.pos = (400,-50)
        Bolt_speed = 0

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  

pgzrun.go()
'''
'''
#ship = Actor('new_ship', center = (400, 500))
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #THis module deletes all laser actors after each round to prevent lag            
Bolt = Actor('bolt_gold.png', center = (400,-50))               #THis module also draws a Bold at score > 100. If ship touches bolt, asteroids slow down.
                                                                #An enemy ship appears, and shoots. lasers destroy the user ship
                                                                #enemy ship takes damage. health is printed. 
                                                                #Asteroids re appear after boss is destroyed, perks drop after.
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

def draw_laser(i):
    list[i].draw()
    animate(list[i], pos = (ship.x +0, ship.y -1000))                

list =[]                                              #Actors draw
def draw():   
    global score
    global boss
    global enemy_health                                           
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
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
    if score >=250 and boss == True:
        screen.draw.text(str('Enemy Health'), color = 'red', center = (400,25), fontname = 'walkway_black', fontsize =30)
        screen.draw.text(str(enemy_health), color = 'red', center = (400,50), fontname = 'walkway_black', fontsize =30)                                           #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    global Bolt_speed
    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
        Bolt_speed = 0.5
        Bolt.pos = (400,-50)
        enemy_ship.pos = (400,-60)
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
        #score = 0
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
    #ship.image = 'new_ship.png'  
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     #originally 0.25 then 0.05
    
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
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    #ship.image = 'new_ship.png'
    game = False
                                              #updates
def update_game():
    global game
    global ship_image
    global score
    global menu

    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png'
        #ship.image = 'new_ship.png'
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def bolt_perk():
    Bolt.draw()
    Bolt.y += Bolt_speed

def enemy():
    animate(enemy_ship, pos = (enemy_ship.x, enemy_ship.y + 200))

def enemy_attack():
    #sounds.fire.play()
    animate(enemy_laser, pos = (enemy_ship.x, enemy_ship.y + 1000))
#def enemy_left():
    #animate(enemy_ship, pos = (enemy_ship.x +100, enemy_ship.y))
#def enemy_right():
    #animate(enemy_ship, pos = (enemy_ship.x -200, enemy_ship.y))

score = 0 
speed = 0.5 
Bolt_speed = 1
game = False 
menu = False 
boss = False
enemy_health = 50                         #main game loop                                       #Game
def update():
    global speed
    global Bolt_speed
    global score 
    global game 
    global list
    global boss   
    global enemy_health

    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

        if score > 550:
            bolt_perk()
            
        if score in range(250,253):   #250
            boss = True
            enemy()

        if score >=250 and boss == True:
            enemy_attack()

        if score >=250 and boss == True:   #250
            speed = 0
            big_asteroid.pos = (600, -100)
            big_asteroid_two.pos = (300, -100)                                                                 
            medium_asteroid.pos = (50, -100)
            medium_asteroid_two.pos = (500, -100)
            small_asteroid.pos = (150, -100)
            small_asteroid_two.pos= (700, -100)
            
        if enemy_laser.y > 800 and score > 250 and boss == True:
            enemy_laser.pos = (enemy_ship.x, enemy_ship.y)
            enemy_attack()
            sounds.fire.play()
            
    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.01          #originally 0.001
            
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
            enemy_health -= 0.1
            #print(enemy_health)

        if item.colliderect(enemy_ship) and score >=250 and enemy_health <=0 and boss == True:
            enemy_ship.center = (400, -60)
            enemy_laser.center = (400,-60)
            boss = False
            score += 10
            speed += 3
            enemy_health = 50
            screen.clear()

        if item.y <= -100:          ##############
            del list[0]

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two) or ship.colliderect(enemy_laser):
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= [] 
        screen.clear()

    if ship.colliderect(Bolt):
        speed = 0.5
        Bolt.pos = (400,-50)
        Bolt_speed = 0

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  

pgzrun.go()

'''
#ship = Actor('new_ship', center = (400, 500))
ship = Actor('ship3.png', center = (400, 500))                  #This module has a stary background. The ship moves and shoots with noise. 
#ship_image = 'millennium_falcon.png'                           #This version has a menu. It also has a 'game over' menu + game over music
#ship = Actor(ship_image, center = (400, 500))                  #This also draws six asteroids, and explodes (image and sound) when hit. Laser trvels through asteroid
#ship_image_one = 'millennium_falcon.png'                       #the meteors changes back into a meteor after explosion, and responds at a random spot off screen
#ship_image_two = 'ship3.png'                                   #the meteors moves and spins. Laser blows at all places it hits.
                                                                #The meteors speed, amd the score increase each time a meteor is destroyed.
laser = Actor('redlaser.png', center = (ship.x, ship.y))        #If the ship is hit by an asteroid, then it blows up
invisible_laser = Actor('invisable_laser.png')                  #This version also has an instructions menu. 
ship_explosion = Actor('explosion_one.png')                     #THis module deletes all laser actors after each round to prevent lag            
Bolt = Actor('bolt_gold.png', center = (400,-50))               #THis module also draws a Bold at score > 100. If ship touches bolt, asteroids slow down.
shield = Actor('shield_gold.png', center = (400,-50))                                                                #An enemy ship appears, and shoots. lasers destroy the user ship
                                                                #enemy ship takes damage. health is printed. 
                                                                #Asteroids re appear after boss is destroyed, perks drop after.
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

def draw_laser(i):
    list[i].draw()
    animate(list[i], pos = (ship.x +0, ship.y -1000))                

list =[]   
shield_status = False                                            #Actors draw
def draw():   
    global score
    global boss
    global enemy_health  
    global shield_status                                         
    screen.clear()
    screen.blit('space_background.png', (0,0))  
    
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
    shield.draw()
    enemy_laser.draw()
    enemy_ship.draw()
    if score >=250 and boss == True:
        screen.draw.text(str('Enemy Health'), color = 'red', center = (400,25), fontname = 'walkway_black', fontsize =30)
        screen.draw.text(str(enemy_health), color = 'red', center = (400,50), fontname = 'walkway_black', fontsize =30)                                           #score system
    color = 'green'
    if score >=0:
        color = 'green'
    if score <0:
        color = 'red'

    global Bolt_speed
    if ship.image == 'explosion_one.png':
        screen.draw.text(str('GAME OVER'), color = 'red', center = (400,300), fontname = 'walkway_black', fontsize =60)
        Bolt_speed = 0.5
        Bolt.pos = (400,-50)
        enemy_ship.pos = (400,-60)
        shield.pos = (400,-50)
        shield_status = False
                                                                                                     
    screen.draw.text(str(score), color = color, center = (750,500))
    screen.draw.text(str('Score:'), color = color, center = (700,500))

    if game == False:
        ship.center = (400, 500)
        screen.draw.text(str('A Journey Through an Asteroid Belt'), color = 'Yellow', center = (400, 375))
        screen.draw.text(str('Press "B" for instructions, "A" to begin'), color = 'Yellow', center = (400, 400))
        #score = 0
                                                #Asteroid reset normal 
    if menu == True:
        screen.draw.text(str('Press the spacebar to fire. Use the left and right arrows to maneuver.'), color = 'Yellow', center = (400,200))
        screen.draw.text(str('When asteroids are destroyed, points are added to the score, and the asteroids speed up.'), color = 'Yellow', center = (400,225))
        screen.draw.text(str('When asteroids move off screen points are subtracted from your score. '), color = 'Yellow', center = (400,250))
        screen.draw.text(str('If an asteroid hits your ship, game over. Please Press C to remove these instructions.'), color = 'Yellow', center = (400,275))

    if shield_status ==True:
        screen.draw.circle((ship.x, ship.y), 80, color = 'blue')
        #s = circle((ship.x, ship.y), 80, color = 'blue')
        #screen.draw.s
        
        

def big_asteroid_normal():
    num = random.randint(50,450)
    big_asteroid.image = 'big_meteor.png'
    big_asteroid.center = (num, -50)

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
    #ship.image = 'new_ship.png'  
                                                #Explosions
def update_big_asteroid_explode():
    sounds.largebang.play()
    big_asteroid.image = 'explosion_one.png'
    clock.schedule_unique(big_asteroid_normal, 0.01)     #originally 0.25 then 0.05
    
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
    global game                                  #ship
    ship.image = 'explosion_one.png'
    sounds.smb_gameover.play()
    game = False                                   #Game
                                                                                
def game_restart():
    ship.image = 'ship3.png' 
    #ship.image = 'new_ship.png'
    game = False
                                              #updates
def update_game():
    global game
    global ship_image
    global score
    global menu
    global shield_speed
    global shield_status
    if keyboard.a:                                                                                #Game
        game = True
        ship.image = 'ship3.png'
        #ship.image = 'new_ship.png'
        score = 0
    if keyboard.B:
        menu = True
    if keyboard.C:
        menu = False

def laser_system():
    sounds.fire.play()
    list.append(Actor('redlaser.png',(ship.x,ship.y-60)))
    
def update_ship():
    if keyboard.left:
        ship.x -=10
        laser.x -=10
    if keyboard.right:
        ship.x +=10
        laser.y +=10

def bolt_perk():
    Bolt.draw()
    Bolt.y += Bolt_speed

def shield_perk():
    #draw.shield()
    shield.y += shield_speed

    #screen.draw.circle((ship.x, ship.y), 80, color = 'blue')

def enemy():
    animate(enemy_ship, pos = (enemy_ship.x, enemy_ship.y + 200))

def enemy_attack():
    #sounds.fire.play()
    animate(enemy_laser, pos = (enemy_ship.x, enemy_ship.y + 1000))
#def enemy_left():
    #animate(enemy_ship, pos = (enemy_ship.x +100, enemy_ship.y))
#def enemy_right():
    #animate(enemy_ship, pos = (enemy_ship.x -200, enemy_ship.y))

score = 0 
speed = 0.5 
Bolt_speed = 1
shield_speed = 1
game = False 
menu = False 
boss = False
enemy_health = 50                         #main game loop                                       #Game
def update():
    global speed
    global Bolt_speed
    global score 
    global game 
    global list
    global boss   
    global enemy_health
    global shield_speed
    global shield_status

    update_game()
    if game == True:                                           #asteroid updates              #Game
        big_asteroid.angle += 1
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

        if score > 500:
            bolt_perk()

        if score >100:
            shield_perk()
            
        if score in range(250,253):   #250
            boss = True
            enemy()

        if score >=250 and boss == True:
            enemy_attack()

        if score >=250 and boss == True:   #250
            speed = 0
            big_asteroid.pos = (600, -100)
            big_asteroid_two.pos = (300, -100)                                                                 
            medium_asteroid.pos = (50, -100)
            medium_asteroid_two.pos = (500, -100)
            small_asteroid.pos = (150, -100)
            small_asteroid_two.pos= (700, -100)
            
        if enemy_laser.y > 800 and score > 250 and boss == True:
            enemy_laser.pos = (enemy_ship.x, enemy_ship.y)
            enemy_attack()
            sounds.fire.play()
            
    if keyboard.space:
        clock.schedule_unique(laser_system, 0.05)
        
    elif keyboard.z:
        laser_system()

    for item in list:

        if item.colliderect(big_asteroid):
            update_big_asteroid_explode()
            score +=1
            speed += 0.01          #originally 0.001
            
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
            enemy_health -= 0.1
            #print(enemy_health)

        if item.colliderect(enemy_ship) and score >=250 and enemy_health <=0 and boss == True:
            enemy_ship.center = (400, -60)
            enemy_laser.center = (400,-60)
            boss = False
            score += 10
            speed += 3
            enemy_health = 50
            screen.clear()

        if item.y <= -100:          ##############
            del list[0]

    if ship.colliderect(big_asteroid) or ship.colliderect(big_asteroid_two) or ship.colliderect(medium_asteroid) or ship.colliderect(medium_asteroid_two) or ship.colliderect(small_asteroid) or ship.colliderect(small_asteroid_two) or ship.colliderect(enemy_laser): 
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        speed = 0.5
        list= []
        shield_status = False
        screen.clear()

    if shield_status == True and big_asteroid.y == ship.y + 30 or big_asteroid_two.y == ship.y + 30:
        update_ship_explode()
        big_asteroid_normal()
        big_asteroid_two_normal()
        medium_asteroid_normal()
        medium_asteroid_two_normal()
        small_asteroid_normal()
        small_asteroid_two_normal()
        
    if ship.colliderect(Bolt):
        speed = 0.5
        Bolt.pos = (400,-50)
        Bolt_speed = 0

    if ship.colliderect(shield):
        shield_status = True
        shield.pos = (400,-50)
        shield_speed = 0

    if big_asteroid.y > 650:
        big_asteroid_normal()
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

    if ship.x < 50:
        ship.x += 10

    if ship.x > 750:
        ship.x -=10  

pgzrun.go()
'''