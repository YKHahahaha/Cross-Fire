# import the pygame module
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
        self.rect.move_ip(-3, 0)
        if self.rect.right < 0:
            self.kill()

class Gold(pygame.sprite.Sprite):
    def __init__(self):
        super(Gold,self).__init__()
        self.image=pygame.image.load("gold.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))

    def update(self):
        self.rect.move_ip(-3,0)
        if self.rect.right<0:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super(Bomb,self).__init__()
        self.image=pygame.image.load('bomb-2.gif').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right<0:
            self.kill()
            
class Bomb_two(pygame.sprite.Sprite):
    def __init__(self):
        super(Bomb_two,self).__init__()
        self.image=pygame.image.load('bomb-1.gif').convert_alpha()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
    def update(self):
        self.rect.move_ip(-5,0)
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
        self.rect.move_ip(-3,0)
        if self.rect.right<0:
            self.kill()





# initialize pygame
pygame.init()

#music:
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("bgm2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
pygame.time.delay(1000)


# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cross Fire")



# Create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
ADDGOLD=pygame.USEREVENT+3
pygame.time.set_timer(ADDGOLD,500)
ADDBOBM=pygame.USEREVENT+4
pygame.time.set_timer(ADDBOBM,1500)
ADDBOBMTWO=pygame.USEREVENT+5
pygame.time.set_timer(ADDBOBMTWO,1500)
ADDBULLET=pygame.USEREVENT+6
pygame.time.set_timer(ADDBULLET,250)
ADDFLAME=pygame.USEREVENT+7
pygame.time.set_timer(ADDFLAME,500)

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
while running:
    if start==True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==K_b:
                    the_dragon=Dragon()
                    all_sprites.add(the_dragon)
                    dragons.add(the_dragon)
                if event.type == QUIT:
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
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            font = pygame.font.Font(None,48)
            text = font.render("GAME OVER!!!", True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.centery = screen.get_rect().centery + 24
            screen.blit(text, text_rect)
            pygame.time.delay(300)
        if pygame.sprite.spritecollideany(player, golds):
            all_sprites.remove(golds)
        if pygame.sprite.spritecollideany(player,bombs):
            all_sprites.remove(bombs)
        if pygame.sprite.spritecollideany(player,bomb_twos):
            all_sprites.remove(bomb_twos)
        if pygame.sprite.spritecollideany(player,flames):
            sound=pygame.mixer.Sound("booms.mp3")
            sound.play()
            font = pygame.font.Font(None,48)
            text = font.render("GAME OVER!!!", True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.centery = screen.get_rect().centery + 24
            screen.blit(text, text_rect)
            player.kill()
            pygame.time.delay(300)
        pygame.sprite.groupcollide(dragons,enemies,False,True)
        pygame.sprite.groupcollide(dragons,flames,False,True)
        pygame.sprite.groupcollide(dragons,bullets,True,False)
        pygame.display.flip()

   
