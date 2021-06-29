# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:15:09 2021

@author: Maria-Theresa
"""

import pygame
import random
import sys

import os


'''
'''



# Initialization --------------------------------------------- #
pygame.init()
from pygame.locals import *

clock = pygame.time.Clock()


# Load Images ------------------------------------------------ #
bg = pygame.image.load(os.path.join('images', 'bg.jpg'))
icon = pygame.image.load(os.path.join('images', 'icon.png'))
lvl_one_icon = pygame.image.load(os.path.join('images', 'lvl_one_icon.png'))
startscreen = pygame.image.load(os.path.join('images', 'startscreen.jpg'))

# Set Icon
pygame.display.set_icon(icon)

# Variables -------------------------------------------------- #
bgX = 0
bgX2 = bg.get_width()
click = False

# Fonts ------------------------------------------------------ #
largeFont = pygame.font.SysFont('comicsans', 80)
smallFont = pygame.font.SysFont('comicsans', 30)


# Setup window ----------------------------------------------- # 
pygame.display.set_caption('Evolution Minigame') # set window name
WINDOW_SIZE = (500, 500) # set up window size 800,437

win = pygame.display.set_mode(WINDOW_SIZE) # initiate window

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu(click):
    start = True

    while start:
        win.blit(startscreen, (0, 0))
        #draw_text('Evolution', largeFont, (0, 0, 0), win, 270, 200)
        mx, my = pygame.mouse.get_pos()
        button = pygame.Rect(300, 300, 200, 100)
        lvl_one = lvl_one_icon
        if button.collidepoint((mx, my)):
            button = pygame.Rect(275, 290, 250, 120)
            lvl_one = pygame.transform.smoothscale(lvl_one_icon, (250, 120))
            win.blit(lvl_one, (275, 290))
            if button.collidepoint((mx, my)):
                if click:
                    fade_out(redrawMenu, 500, 500) #800,437
                    start = False
                    
        else:
            win.blit(lvl_one, (300, 300))
            
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                start = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            #pygame.display.update()


def redrawMenu():
    lvl_one = lvl_one_icon
    win.blit(startscreen, (0,0))
    win.blit(lvl_one, (300, 300))


def fade_out(redraw, width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redraw()
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(3)
'''
def endScreen():
    global pause, byspeed,bxspeed,leben, bx,by, sx, sy,speed
    pause = 0
    speed = 30
    sx = []
    sy=[]
    by=[]
    bx=[]

    win.blit(startscreen, (0,0))
    pygame.display.update()
    leben==3



pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, 3000)

main_menu(click)

'''
'''
'''

x=500
y=500
sbreite=100
shoehe=15

sx=200
sy=450

bx= int(x/2)
by= int(y/2)

brad=15
speed=0
bxspeed=1
byspeed=-2
leben=3
pygame.init()
screen= pygame.display.set_mode([x,y])
screen.fill((0,0,0))
pygame.draw.circle(screen, (255,255,0), (bx,by), brad, 0)
pygame.draw.rect(screen, (255,40,0), (sx,sy,sbreite,shoehe),0)
pygame.display.flip()

def sblock():
    global speed
    if sx <= 0 or sx>=x-sbreite:
        speed=0
def ballbewegung():
    global bx,by
    bx+= bxspeed
    by += byspeed
def reset():
    global byspeed,bxspeed,leben, bx,by, sx, sy,speed
    sx=200
    sy=450
    bx=int(x/2)
    by=int(y/2)
    speed=0
    bxspeed=random.randint(-2,2)
    if bxspeed==0:
        bxspeed==1
    bxspeed=random.randint(-2,2)
    if byspeed==0:
        byspeed=2
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (225,255,0), (bx,by), brad,0)
        pygame.draw.rect(screen,(255,40,0), (sx,sy,sbreite,shoehe), 0)
        pygame.display.flip()
        pygame.time.wait(1000)
def ballblock():
    global byspeed,bxspeed,leben
    if by-brad <=0:
        byspeed*=-1
    if bx-brad<=0:
        bxspeed*=-1
    if bx+brad>=x:
        bxspeed*=-1
    if by >= 435 and by <=440:
        if bx>=sx-15 and bx<=sx+sbreite+15:
            byspeed*=-1
        else:
            leben-=1
            reset()
def sbewegung():
    global sx
    sx +=speed
while leben>0:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                speed=-2
            if event.key==pygame.KEYUP:
                    speed=0
            if event.key==pygame.K_RIGHT:
                speed=2
    main_menu(click)   
    
    screen.fill((255,255,0))
    sbewegung()
    sblock()
    pygame.draw.rect(screen,(128,0,0), (sx,sy,sbreite,shoehe), 0)
    ballbewegung()
    ballblock()
    pygame.draw.circle(screen, (0,128,128), (bx,by), brad,0)
    pygame.display.flip()
    pygame.time.wait(5)
#endScreen()
print("Verloren")