#Author_name: StephenCurry
#Author_Email: stepfencurryxiao@gmail.com
#FaceBook: https://www.facebook.com/xiao.stepfencurry.3
#Github: https://github.com/stepfencurryxiao/Cross-Fire/blob/master/AIGame/AIGame.py
#Edition: v2.3
#Last update: 2019.8.23

from functools import reduce
#import the pygame!
import pygame

# import random for random numbers!
import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import *
#The game will use sys.exit()
import sys
#import the time module
import time
#use math module to compute distance
import math

#use pandas to read data
import pandas as pd
#The machine learning module
from sklearn import tree
import numpy as np


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('plane.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

    #The move function
    #move_ip(speed)
    def update(self, pressed_keys):
        if pressed_keys == 'w':
            self.rect.move_ip(0, -30)
        if pressed_keys == 's':
            self.rect.move_ip(0, 30)
        if pressed_keys == 'a':
            self.rect.move_ip(-30, 0)
        if pressed_keys == 'd':
            self.rect.move_ip(30, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

class Player_two(pygame.sprite.Sprite):
    def __init__(self):
        super(Player_two, self).__init__()
        self.image = pygame.image.load('player.png').convert_alpha()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

    #The move function
    #move_ip(speed)
    def update(self, pressed_keys):
        if pressed_keys == 'w':
            self.rect.move_ip(0, -30)
        if pressed_keys == 's':
            self.rect.move_ip(0, 30)
        if pressed_keys == 'a':
            self.rect.move_ip(-30, 0)
        if pressed_keys == 'd':
            self.rect.move_ip(30, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('missile.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        #produce the random numbers
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))) 
        self.speed = random.randint(2,5)

    #The move function
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            #kill the Enemy
            self.kill()

    #get the rect
    def get_rect(self):
        return self.rect


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(center=(
            random.randint(820, 900), random.randint(0, 600)))

    def update(self):
        self.rect.move_ip(-50, 0)
        if self.rect.right < 0:
            self.kill()

class Gold(pygame.sprite.Sprite):
    def __init__(self):
        super(Gold,self).__init__()
        self.image=pygame.image.load("gold.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))

    def update(self):
        self.rect.move_ip(-50,0)
        if self.rect.right<0:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super(Bomb,self).__init__()
        self.image=pygame.image.load('bomb-2.gif').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-30,0)
        if self.rect.right<0:
            self.kill()
            
class Bomb_two(pygame.sprite.Sprite):
    def __init__(self):
        super(Bomb_two,self).__init__()
        self.image=pygame.image.load('bomb-1.gif').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-30,0)
        if self.rect.right<0:
            self.kill()
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet,self).__init__()
        self.image=pygame.image.load('bullet.png').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-50,0)
        if self.rect.right<0:
            self.kill()


class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        super(Dragon,self).__init__()
        self.image=pygame.image.load('dragon.png').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(0,random.randint(0,600)))
    def update(self):
        self.rect.move_ip(20,0)
        if self.rect.left>800:
            self.kill()

class Flame(pygame.sprite.Sprite):
    def __init__(self):
        super(Flame,self).__init__()
        self.image=pygame.image.load('flame.png').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-50,0)
        if self.rect.right<0:
            self.kill()

    #get the rect
    def get_rect(self):
        return self.rect

def exit_game():
    sys.exit()

def model(file_name,distance):
    sys.__stdout__ = sys.stdout
    # use decisiontreeclassifier to predict
    clf = tree.DecisionTreeClassifier()
    #read the data
    data = pd.read_csv(file_name)
    X = data[['distance']]
    Y = data[['key']]

    #train the module
    clf = clf.fit(X,Y)
    # predict 
    press_key = clf.predict(np.array(distance).reshape(1,-1))

    if press_key == ['down']:
        return 's'
    if press_key == ['up']:
        return 'w'
    if press_key == ['right']:
        return 'd'
    if press_key == ['left']:
        return 'a'


global distance
def compute_distance(Player,other):
	#compute the distance
    return math.sqrt(math.pow(Player.rect.center[0] - other.get_rect().center[0],2)+
                     math.pow(Player.rect.center[1] - other.get_rect().center[1],2))
    
_Life = 10
_Life_player_two = 10
Time=0
endscore=""
#everything's time
global enemy_millsecond 
global cloud_millsecond 
global gold_millsecond 
global bobm_millsecond 
global bomb_two_millsecond 
global bubblet_millsecond 
global flame_millsecond



def IsDie():
    global _Life
    global _Life_player_two
    global Time
    global endscore
    
    try:
        if pygame.sprite.spritecollideany(player, enemies):
            all_sprites.remove(enemies)
            _Life += 1
                
        elif pygame.sprite.spritecollideany(player, golds):
            all_sprites.remove(golds)
            _Life += 1
        elif pygame.sprite.spritecollideany(player,bombs):
            all_sprites.remove(bombs)
            _Life += 1
        elif pygame.sprite.spritecollideany(player,bomb_twos):
            all_sprites.remove(bomb_twos)
            _Life += 1
        elif pygame.sprite.spritecollideany(player,flames):
            all_sprites.remove(flames)
            _Life -= 1

        if pygame.sprite.spritecollideany(player_two, enemies):
            all_sprites.remove(enemies)
            _Life_player_two -= 1
                
        elif pygame.sprite.spritecollideany(player_two, golds):
            all_sprites.remove(golds)
            _Life_player_two += 1
        elif pygame.sprite.spritecollideany(player_two,bombs):
            all_sprites.remove(bombs)
            _Life_player_two += 1
            Sound_bomb.play(1)
            
        elif pygame.sprite.spritecollideany(player_two,bomb_twos):
            all_sprites.remove(bomb_twos)
            _Life_player_two += 1
            Sound_bomb.play(1)
            
        elif pygame.sprite.spritecollideany(player_two,flames):
            all_sprites.remove(flames)
            _Life_player_two += 1

        #compute the score(endscore)
        Time=Time+1
        if Time>0 and Time<2000:
            endscore="E"
        elif Time>2000 and Time<4000:
            endscore="D"

        elif Time>4000 and Time<4500:
            endscore="C"
        elif Time>4500 and Time<6000:
            endscore="B"
        elif Time>6000 and Time<10000:
            endscore="A"
        elif Time>10000:
            endscore="SSS"
    
        #when Life is 0,The player die and exit the game
        if _Life == 0:
            Sound_boom.stop()
            #pygame.mixer.music.stop()
            Sound_die.play(1)
            font = pygame.font.Font(None,48)
            text = font.render("The AI player 2 win!!!score:{}".format(endscore), True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.centery = screen.get_rect().centery + 24
            screen.blit(text, text_rect)
            pygame.time.delay(50)
            player.kill()
            #delete the _Life
            del _Life

        if _Life_player_two == 0:
            Sound_boom.stop()
            #pygame.mixer.music.stop()
            Sound_die.play(1)
            font = pygame.font.Font(None,48)
            text = font.render("The AI player 1 win!!!score:{}".format(endscore), True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.centery = screen.get_rect().centery + 24
            screen.blit(text, text_rect)
            pygame.time.delay(50)
            player_two.kill()
            #delete the _Life
            del _Life_player_two

        
    #When we delete the _Life,it will raise a NameError.So catch the NameError 
    except NameError:
        exit_game()

#random to choose the plane
Plane_choice = random.randint(1,2)

global start
global runing

start = False
running = False

# initialize pygame
pygame.init()

#music:
pygame.mixer.init()
#initialize the music
pygame.mixer.music.load("AI_bgm.mp3")
#This is the bgm
#pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
#play the music
pygame.time.delay(1000)
#timesout

# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cross Fire")
clock = pygame.time.Clock()


# The start windows
start_windows = pygame.Surface(screen.get_size())    
start_windows_2 = pygame.Surface(screen.get_size())  
start_windows = start_windows.convert()
start_windows_2 = start_windows_2.convert()
start_windows.fill((255,255,255))  
start_windows_2.fill((0,255,0))

# Load the picture
begin_button_F = pygame.image.load("play_F.png").convert_alpha()
begin_button_U = pygame.image.load("play_U.png").convert_alpha()
Exit_button_F = pygame.image.load("Exit_F.png").convert_alpha()
Exit_button_U = pygame.image.load("Exit_U.png").convert_alpha()
background = pygame.image.load("background.jpg").convert()

L1 = True
while L1:
    clock.tick()
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    if x1 >= 227 and x1 <= 555 and y1 >= 241 and y1 <=327:
        start_windows.blit(begin_button_U, (250, 230))
        if buttons[0]:
            L1 = False
            #stop playing music
            pygame.mixer.music.stop()
            # The game start.
            start = True
            running = True

    elif x1 >= 227 and x1 <= 555 and y1 >= 361 and y1 <=447:
        start_windows.blit(Exit_button_U, (290, 360))
        if buttons[0]:
        	#The game exit
            pygame.quit()
            exit()

    else:
        #draw something
        start_windows.blit(background,background.get_rect())
        start_windows.blit(begin_button_F, (250, 230))
        start_windows.blit(Exit_button_F, (290, 360))
        

    # draw the backgroud
    screen.blit(start_windows,(0,0))
    pygame.display.update()

    for event in pygame.event.get():
    	#Get all the event
        if event.type == pygame.QUIT:
            #exit the pygame
            pygame.quit()
            #exit the game
            exit()

# new Flame and Enemy object     
global new_flames
new_flames = Flame()
global new_enemy
new_enemy = Enemy()

#initialize the font
pygame.font.init()

# set time
enemy_millsecond = 1000
cloud_millsecond = 1000
gold_millsecond = 500
bobm_millsecond = 1500
bomb_two_millsecond = 1500
bubblet_millsecond = 250
flame_millsecond = 1000

# Create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, enemy_millsecond)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, cloud_millsecond)
ADDGOLD = pygame.USEREVENT+3
pygame.time.set_timer(ADDGOLD,gold_millsecond)
ADDBOBM = pygame.USEREVENT+4
pygame.time.set_timer(ADDBOBM,bobm_millsecond)
ADDBOBMTWO = pygame.USEREVENT+5
pygame.time.set_timer(ADDBOBMTWO,bomb_two_millsecond)
ADDBULLET = pygame.USEREVENT+6
pygame.time.set_timer(ADDBULLET,bomb_two_millsecond)
ADDFLAME = pygame.USEREVENT+7
pygame.time.set_timer(ADDFLAME,flame_millsecond)

# create our 'player' and 'player_two', right now he's just a rectangle
player = Player()
player_two = Player_two()

background = pygame.Surface(screen.get_size())
#background.fill(backgroung_color)
background.fill((135, 206, 250))

# The sprite
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
golds = pygame.sprite.Group()
bombs = pygame.sprite.Group()
bomb_twos = pygame.sprite.Group()
bullets = pygame.sprite.Group()
dragons = pygame.sprite.Group()
flames = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player_two)

#play the boom.wav
Sound_boom = pygame.mixer.Sound("boom.wav")
Sound_boom.set_volume(0.2)
Sound_boom.play(-1)

#play the bomb.wav
Sound_bomb = pygame.mixer.Sound("bomb.wav")
Sound_bomb.set_volume(0.5)

#play the die.wav
Sound_die = pygame.mixer.Sound("die.wav")
Sound_die.set_volume(0.5)

try:
	# Try to play the bgm02.mp3
    pygame.mixer.music.load("AI_bgm02.mp3")
    #use -1 to loop play
    pygame.mixer.music.play(-1)
    while running:
        if start==True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_b:
                        the_dragon = Dragon()
                        all_sprites.add(the_dragon)
                        dragons.add(the_dragon)
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                        pygame.quit()
                    if event.type == pygame.QUIT:
                        running = False
                        sys.exit()
                        pygame.quit()
                elif event.type == ADDENEMY:
                    new_enemy = Enemy()
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)

                elif event.type == ADDCLOUD:
                    new_cloud = Cloud()
                    all_sprites.add(new_cloud)
                    clouds.add(new_cloud)
                elif event.type == ADDGOLD:
                    new_gold = Gold()
                    all_sprites.add(new_gold)
                    golds.add(new_gold)
                elif event.type == ADDBOBM:
                    new_bomb = Bomb()
                    all_sprites.add(new_bomb)
                    bombs.add(new_bomb)
                elif event.type == ADDBOBMTWO:
                    new_bomb_two = Bomb_two()
                    all_sprites.add(new_bomb_two)
                    bomb_twos.add(new_bomb_two)
                elif event.type == ADDBULLET:
                    new_bullet = Bullet()
                    all_sprites.add(new_bullet)
                    bullets.add(new_bullet)
                elif event.type == ADDFLAME:
                    new_flames = Flame()
                    all_sprites.add(new_flames)
                    flames.add(new_flames)
            
            #draw the background
            screen.blit(background, (0, 0))
            pygame.draw.rect(screen, (255, 0, 0, 180), Rect(300,500,_Life,25))
            pygame.draw.rect(screen, (100,200,100,180), Rect(300,500,200,25), 2)
            pygame.draw.rect(screen, (255, 0, 0, 180), Rect(300,570,_Life_player_two,25))
            pygame.draw.rect(screen, (100,200,100,180), Rect(300,570,200,25), 2)
            if _Life >= 30:
                _Life = 30
                pygame.draw.rect(screen, (255, 0, 0, 180), Rect(300,500,200,25))
                pygame.draw.rect(screen, (100,200,100,180), Rect(300,500,200,25), 2)
            if _Life_player_two >= 30:
                _Life_player_two = 30
                pygame.draw.rect(screen, (255, 0, 0, 180), Rect(300,570,200,25))
                pygame.draw.rect(screen, (100,200,100,180), Rect(300,570,200,25), 2)
    
            distance = compute_distance(player,new_flames)
            distance_player_two = compute_distance(player,new_enemy)
            #print(distance_player_two)
            
            # Enter the number
            # pressed_keys = pygame.key.get_pressed()
            key = model("data01.csv",distance)
            #predict the 'key'
            key_player_two = model("data02.csv",distance_player_two)
            player.update(key)
            player_two.update(key_player_two)
            #everthing updates
            enemies.update()
            clouds.update()
            golds.update()
            bombs.update()
            bomb_twos.update()
            bullets.update()
            dragons.update()
            flames.update()


            #Is the player die?
            IsDie()

            #print everything in the screen
            for entity in all_sprites:
                screen.blit(entity.image, entity.rect)


            # The dragons sprite
            pygame.sprite.groupcollide(dragons,enemies,False,True)
            pygame.sprite.groupcollide(dragons,flames,False,True)
            pygame.sprite.groupcollide(dragons,bullets,True,False)
            pygame.display.flip()

#Catch the NameError in isDie()
except NameError:
    #game over
    exit_game()
    #sys.exit()
