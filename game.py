#Author: StephenCurry
#Author_Email: stepfencurryxiao@gmail
#Edition: v2.0
#Last update: 2019.8.16

#import the pygame!
import pygame

# import random for random numbers!
import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import *

import sys

import time


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('plane.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

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
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600)))
        self.speed = random.randint(2,5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(center=(
            random.randint(820, 900), random.randint(0, 600)))

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

class Gold(pygame.sprite.Sprite):
    def __init__(self):
        super(Gold,self).__init__()
        self.image=pygame.image.load("gold.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))

    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right<0:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super(Bomb,self).__init__()
        self.image=pygame.image.load('bomb-2.gif').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-3,0)
        if self.rect.right<0:
            self.kill()
            
class Bomb_two(pygame.sprite.Sprite):
    def __init__(self):
        super(Bomb_two,self).__init__()
        self.image=pygame.image.load('bomb-1.gif').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-3,0)
        if self.rect.right<0:
            self.kill()
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet,self).__init__()
        self.image=pygame.image.load('bullet.png').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right<0:
            self.kill()


class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        super(Dragon,self).__init__()
        self.image=pygame.image.load('dragon.png').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(0,random.randint(0,600)))
    def update(self):
        self.rect.move_ip(2,0)
        if self.rect.left>800:
            self.kill()

class Flame(pygame.sprite.Sprite):
    def __init__(self):
        super(Flame,self).__init__()
        self.image=pygame.image.load('flame.png').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right<0:
            self.kill()


def exit_game():
    sys.exit()


_Life = 10
Time=0
endscore=""
global enemy_millsecond 
global cloud_millsecond 
global gold_millsecond 
global bobm_millsecond 
global bomb_two_millsecond 
global bubblet_millsecond 
global flame_millsecond 

def IsDie():
    global _Life
    global Time
    global endscore

    try:
        if pygame.sprite.spritecollideany(player, enemies):
            all_sprites.remove(enemies)
            _Life -= 1
                
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

        Time=Time+1
        if Time>0 and Time<2000:
            endscore="E"
        if Time>2000 and Time<4000:
            endscore="D"
            enemy_millsecond = 1000
            cloud_millsecond = 2000
            gold_millsecond = 2000
            bobm_millsecond = 5700
            bomb_two_millsecond = 5700
            bubblet_millsecond = 1000
            flame_millsecond =1000

        if Time>4000 and Time<4500:
            endscore="C"
        if Time>4500 and Time<6000:
            endscore="B"
        if Time>6000 and Time<10000:
            endscore="A"
        if Time>10000:
            endscore="SSS"
            enemy_millsecond = 10
            cloud_millsecond = 2000
            gold_millsecond = 5000
            bobm_millsecond = 9700
            bomb_two_millsecond = 9700
            bubblet_millsecond = 6000
            flame_millsecond =10
        
        if _Life == 0:
            font = pygame.font.Font(None,48)
            text = font.render("GAME OVER!!!You score is:{}".format(endscore), True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.centery = screen.get_rect().centery + 24
            screen.blit(text, text_rect)
            pygame.time.delay(50)
            player.kill()
            del _Life

    except NameError:
        exit_game()

        
        

# initialize pygame
pygame.init()

#music:
pygame.mixer.init()
pygame.mixer.music.load("bgm2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
pygame.time.delay(1000)


# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cross Fire")

pygame.font.init()

enemy_millsecond = 500
cloud_millsecond = 1000
gold_millsecond = 500
bobm_millsecond = 1500
bomb_two_millsecond = 1500
bubblet_millsecond = 250
flame_millsecond = 500

# Create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, enemy_millsecond)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, cloud_millsecond)
ADDGOLD=pygame.USEREVENT+3
pygame.time.set_timer(ADDGOLD,gold_millsecond)
ADDBOBM=pygame.USEREVENT+4
pygame.time.set_timer(ADDBOBM,bobm_millsecond)
ADDBOBMTWO=pygame.USEREVENT+5
pygame.time.set_timer(ADDBOBMTWO,bomb_two_millsecond)
ADDBULLET=pygame.USEREVENT+6
pygame.time.set_timer(ADDBULLET,bomb_two_millsecond)
ADDFLAME=pygame.USEREVENT+7
pygame.time.set_timer(ADDFLAME,flame_millsecond)

# create our 'player', right now he's just a rectangle
player = Player()


background = pygame.Surface(screen.get_size())
background.fill((135, 206, 250))


enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
golds=pygame.sprite.Group()
bombs=pygame.sprite.Group()
bomb_twos=pygame.sprite.Group()
bullets=pygame.sprite.Group()
dragons=pygame.sprite.Group()
flames=pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running=True
start=True
try:
    while running:
        if start==True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key==K_b:
                        the_dragon=Dragon()
                        all_sprites.add(the_dragon)
                        dragons.add(the_dragon)
                    if event.key==pygame.K_ESCAPE:
                        sys.exit()
                        pygame.quit()
                    if event.type == pygame.QUIT:
                        running = False
                        sys.exit()
                elif event.type == ADDENEMY:
                    new_enemy = Enemy()
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
                elif event.type == ADDCLOUD:
                    new_cloud = Cloud()
                    all_sprites.add(new_cloud)
                    clouds.add(new_cloud)
                elif event.type==ADDGOLD:
                    new_gold=Gold()
                    all_sprites.add(new_gold)
                    golds.add(new_gold)
                elif event.type==ADDBOBM:
                    new_bomb=Bomb()
                    all_sprites.add(new_bomb)
                    bombs.add(new_bomb)
                elif event.type==ADDBOBMTWO:
                    new_bomb_two=Bomb_two()
                    all_sprites.add(new_bomb_two)
                    bomb_twos.add(new_bomb_two)
                elif event.type==ADDBULLET:
                    new_bullet=Bullet()
                    all_sprites.add(new_bullet)
                    bullets.add(new_bullet)
                elif event.type==ADDFLAME:
                    new_flames=Flame()
                    all_sprites.add(new_flames)
                    flames.add(new_flames)
            screen.blit(background, (0, 0))
            pygame.draw.rect(screen, (255, 0, 0, 180), Rect(300,570,_Life//10,25))
            pygame.draw.rect(screen, (100,200,100,180), Rect(300,570,200,25), 2)
            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys)
            enemies.update()
            clouds.update()
            golds.update()
            bombs.update()
            bomb_twos.update()
            bullets.update()
            dragons.update()
            flames.update()


            IsDie()
                
            for entity in all_sprites:
                screen.blit(entity.image, entity.rect)
                
            pygame.sprite.groupcollide(dragons,enemies,False,True)
            pygame.sprite.groupcollide(dragons,flames,False,True)
            pygame.sprite.groupcollide(dragons,bullets,True,False)
            pygame.display.flip()

except NameError:
    sys.exit()
