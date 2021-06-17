import pygame, os
from random import randrange

# Initialization --------------------------------------------- #
pygame.init()
from pygame.locals import *

clock = pygame.time.Clock()


# Load Images ------------------------------------------------ #
bg = pygame.image.load(os.path.join('images', 'bg.jpg'))
icon = pygame.image.load(os.path.join('images', 'icon.png'))
startscreen = pygame.image.load(os.path.join('images', 'startscreen.jpg'))

# Variables -------------------------------------------------- #
bgX = 0
bgX2 = bg.get_width()

# Setup window ----------------------------------------------- # 
pygame.display.set_caption('Evolution Minigame') # set window name
WINDOW_SIZE = (800, 437) # set up window size

win = pygame.display.set_mode(WINDOW_SIZE) # initiate window

class Player(object):
    # Images ----------------------------------------------------- #
    run = [pygame.image.load(os.path.join('cell', str(x) + '.png')) for x in range(8, 16)] # 8-15 run
    jump = [pygame.image.load(os.path.join('cell', str(x) + '.png')) for x in range(1, 8)] # 1-7 jump
    slide = [pygame.image.load(os.path.join('images', 'S1.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
    fall = pygame.image.load(os.path.join('images', '0.png'))
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.falling = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.falling:
            win.blit(self.fall, (self.x, self.y + 30))
        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.3
            win.blit(self.jump[self.jumpCount//18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
                self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            elif self.slideCount > 20 and self.slideCount < 80:
                self.hitbox = (self.x, self.y+3, self.width-8, self.height-35)

            if self.slideCount >= 110:
                self.slideCount = 0
                self.runCount = 0
                self.slideUp = False
                self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)
            win.blit(self.slide[self.slideCount//10], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1
            self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-13)

        pygame.draw.rect(win, (255,0,0),self.hitbox, 2)

class Saw(object):
    rotate = [pygame.image.load(os.path.join('images', 'SAW0.png')), pygame.image.load(os.path.join('images', 'SAW1.png')), pygame.image.load(os.path.join('images', 'SAW2.png')), pygame.image.load(os.path.join('images', 'SAW3.png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        if self.rotateCount >= 8:
            self.rotateCount = 0
        win.blit(pygame.transform.scale(self.rotate[self.rotateCount//2], (64,64)), (self.x,self.y))
        self.rotateCount += 1

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False


class Spike(Saw):
    img = pygame.image.load(os.path.join('images', 'spike.png'))

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y, 28,315)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False

# Functions -------------------------------------------------- #
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    start = True
    titleFont = pygame.font.SysFont('comicsans', 80)
    while start:
        win.blit(startscreen, (0, 0))
        draw_text('Evolution', titleFont, (0, 0, 0), win, 270, 160)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                start = False
            if event.type == KEYDOWN:
                start = False

            pygame.display.update()
            clock.tick(speed)

def updateFile():
    f = open('scores.txt','r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score

    return last



def endScreen():
    #global pause, score, speed, obstacles
    pause = 0
    score = 0
    speed = 30
    obstacles = []

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                runner.falling = False
                runner.sliding = False
                runner.jumpin = False

        win.blit(bg, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        lastScore = largeFont.render('Best Score: ' + str(updateFile()),1,(0,0,0))
        currentScore = largeFont.render('Score: '+ str(score),1,(0,0,0))
        win.blit(lastScore, (WINDOW_SIZE[0]/2 - lastScore.get_width()/2,150))
        win.blit(currentScore, (WINDOW_SIZE[0]/2 - currentScore.get_width()/2, 240))
        pygame.display.update()
    score = 0

def redrawWindow():
    largeFont = pygame.font.SysFont('comicsans', 30)
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2,0))
    text = largeFont.render('Score: ' + str(score), 1, (255,255,255))
    runner.draw(win)
    for obstacle in obstacles:
        obstacle.draw(win)

    win.blit(text, (700, 10))
    pygame.display.update()


pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, 3000)
speed = 50

score = 0

run = True
runner = Player(200, 313, 64, 64)

obstacles = []
pause = 0
fallSpeed = 0


main_menu()

while run:
    if pause > 0:
        pause += 1
        if pause > fallSpeed * 2:
            endScreen()

    score = speed//10 - 3

    # check for collision
    for obstacle in obstacles:
        if obstacle.collide(runner.hitbox):
            runner.falling = True

            if pause == 0:
                pause = 1
                fallSpeed = speed
        # remove obstacles out of the screen
        if obstacle.x < -64:
            obstacles.pop(obstacles.index(obstacle))
        # move obstacles
        else:
            obstacle.x -= 1.4

    # move background
    bgX -= 1.4
    bgX2 -= 1.4

    # endless background
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width() 

    # Eventloop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

        # generate obstacles
        if event.type == USEREVENT+1:
            speed += 1

        if event.type == USEREVENT+2:
            r = randrange(0,2)
            if r == 0:
                obstacles.append(Saw(810, 310, 64, 64))
            elif r == 1:
                obstacles.append(Spike(810, 0, 48, 310))

    # key input
    if runner.falling == False:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            if not(runner.jumping):
                runner.jumping = True

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if not(runner.sliding):
                runner.sliding = True

    clock.tick(speed)
    redrawWindow()
