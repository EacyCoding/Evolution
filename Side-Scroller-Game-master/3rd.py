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