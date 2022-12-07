# content from kids can code: http://kidscancode.org/blog/
'''
Sources:
https://python.hotexamples.com/examples/-/Player/respawn/python-player-respawn-method-examples.html
https://python-forum.io/thread-24462.html
Andrew (Table 0)
Tyson (Table 0)

Goals, Rules, Feedback, Freedom

Goals: Get all 4 tokens to quit the game / move to the next level
Rules: If you fall off and hit any of the red borders you die
Feedback: When you collide with a mob you get a point
Freedom: It does not matter how you get to the top platform and collect the final sprite it is up to the user
'''

# import libraries and modules

# from platform import platform
from multiprocessing import reduction
from pickle import TRUE
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
# asset folders for importing images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'Mariogame_Images')

# from symbol import power
vec = pg.math.Vector2

# game settings 
WIDTH = 800
HEIGHT = 800
FPS = 30

# player settings
PLAYER_GRAV = 0.8
PLAYER_FRIC = 0.1
SCORE = 0

#define all of the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (73, 46, 24)

# define the draw function and add all of the attributes
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)
# Create the player class 
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
#Creates the player as minecraft steve by taking the "Steve1.png from the file directory of images
        self.image = pg.image.load(os.path.join(img_folder, 'steve1.png')).convert()
        self.image.set_colorkey(BROWN)
        self.rect = self.image.get_rect()
        self.rect.center = (0,775)
        self.pos = vec(30,430)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
#defines the controls for the player
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
#defines the jumo function and states if the player collides with a platform TP them to top
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, all_plats, False)
        self.rect.x += -1
        if hits:
            self.vel.y = -20
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
# the friction values 
        self.acc.x += self.vel.x * -0.15
        self.acc.y += self.vel.y * -0.05
        self.vel += self.acc
        self.pos += self.vel + 0.3 * self.acc
        self.rect.midbottom = self.pos
# if the player y value is greater than heigh TP them to that point
        if self.rect.y > HEIGHT:
            self.pos = (50,770)
# creates the platforms class and assings unique attritbutes
class Platform(Sprite):
    def __init__(self, x, y, w, h, typeof1):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# Creates the border classes with the main difference between the platform and the borders being the color
class Border(Sprite):
    def __init__(self, x, y, w, h, typeof1):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.typeof1 = typeof1
# creates the mob classes and makes the mob a mario coin
# also removes the background color of the mario coin "white"
class Mob(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(img_folder, 'mariocoin.png')).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()

# create groups
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
all_mobs = pg.sprite.Group()
all_borders = pg.sprite.Group()

# instantiate Platform class
player = Player()
plat = Platform(10, 775, 100, 15,'plat')
plat2 = Platform(100, 670, 120, 15,'plat')
plat3 = Platform(220, 540, 120, 15, 'plat')
plat4 = Platform(450, 670, 50, 15,'plat')
plat5 = Platform(650, 540, 50, 15,'plat')
plat6 = Platform(475, 420, 50, 15,'plat')
plat7 = Platform(690, 300, 50, 15,'plat')
plat8 = Platform(690, 200, 50, 15,'plat')
plat9 = Platform(0, 100, 675, 5,'plat')
coinplat = Platform(700, 750, 50, 15,'plat')
mob1 = Mob(700, 700, 25, 15,'mob')
mob2 = Mob(50, 400, 50, 15, 'mob')
mob3 = Mob(475, 200, 50, 15, 'mob')
winmob = Mob(50, 50, 675, 5, 'mob')
#Instantiate Border Class
plat_bottom = Border(0, 795, 800, 80,'ground')
plat_left = Border(-45, 0, 50, 800,'ground')
plat_right = Border(795, 0, 50, 800,'ground')
# add the individual instances to all respective groups
all_sprites.add(player)
all_plats.add(plat, plat2, plat3, plat4, plat5, plat6, plat7, plat8, plat9, coinplat,)
all_borders.add(plat_bottom, plat_left, plat_right)
all_mobs.add(mob1, mob2, mob3,winmob)

#All Sprites group for the platforms
all_sprites.add(plat)
all_sprites.add(plat2)
all_sprites.add(plat3)
all_sprites.add(plat4)
all_sprites.add(plat5)
all_sprites.add(plat6)
all_sprites.add(plat7)
all_sprites.add(plat8)
all_sprites.add(plat9)
all_sprites.add(coinplat)

# All Sprites group for the borders
all_sprites.add(plat_left)
all_sprites.add(plat_right)

# All Sprites group for the Mobs
all_sprites.add(mob1)
all_sprites.add(mob2)
all_sprites.add(mob3)
all_sprites.add(winmob)

# Game loop
running = True
while running:
# keep the loop running using clock
    clock.tick(FPS)
# if the player collides with a platform TP them to the top and print in the terminal
    hits = pg.sprite.spritecollide(player, all_plats, False)
    if hits:
        # print("ive struck a plat")
        player.pos.y = hits[0].rect.top
        player.vel.y = 0
# if the player comes into contact with the mario coin than kill the mario coin and add 1 to the player score
    mobhits = pg.sprite.spritecollide(player, all_mobs, True)
    if mobhits:
        print("ive struck a mob")
        SCORE += 1     
# if the player quits the game window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
# if the player gets to a score of 3 than quit the window signyfing a win
        if SCORE > 3:
                event.type == pg.quit
                running = False
#if the player hits space bar than jump
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()

############ Update ##############
    # update all sprites
    all_sprites.update()
############ Draw ################
# draw the background screen
    screen.fill(BLACK)
    # draw text
    # draw_text("Level 1", 22, WHITE, WIDTH - 700, HEIGHT / 24)
    draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/20)
    # draw_text("Score: " + str(YOU_WIN), 22, WHITE, WIDTH/2, HEIGHT/20)
    # draw_text('FPS: ")
    # draw_text("score")
    # draw all sprites
    all_sprites.draw(screen)
    # buffer - after drawing everything, flip display
    pg.display.flip()
pg.quit()
