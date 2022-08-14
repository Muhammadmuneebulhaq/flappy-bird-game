'''Author: Muhammad Muneeb ul Haq
Date started: 23 April 2022
Date completed: 8 May 2022
'''

import random
import sys
import pygame
from pygame.locals import *

# Global variables
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAMEIMAGES = {}
GAMESOUNDS = {}
PLAYER = 'gallery\\bird.png'
BACKGROUND = 'gallery\\background.png'
PIPE = 'gallery\\pipe.png'


def iscollide(px, py, up, lp):
    if py > GROUNDY - 25 :
        GAMESOUNDS['over'].play()
        return True
    
    for pipe in up:
        pipeHeight = GAMEIMAGES['pipe'][0].get_height()
        if(py < pipeHeight + pipe['y'] - GAMEIMAGES['player'].get_height()) and abs(px - pipe['x']) <= 32:
            GAMESOUNDS['over'].play()
            return True

    for pipe in lp:
        if (py + GAMEIMAGES['player'].get_height() > pipe['y']) and abs(px - pipe['x']) <= 32:
            GAMESOUNDS['over'].play()
            return True

    return False


#to generate pipes
def getrandompipe():
    # to create 2 pipes one straight and other rotated to blit on the screen
        pipeheight = GAMEIMAGES['pipe'][0].get_height()
        offset = SCREENHEIGHT /3
        lowerpipey = offset + random.randrange(0,int(SCREENHEIGHT - GAMEIMAGES['base'].get_height()  - 1.2 *offset))
        upperpipey = (pipeheight - lowerpipey) + offset
        pipex = SCREENWIDTH   
        pipe = [{'x': pipex, 'y': -upperpipey}#upper pipe
        , {'x': pipex, 'y': lowerpipey}#lower pipe
        ]
        return pipe
def welcomescreen():
    #shows welcome images on the screen
    playerx = int((SCREENWIDTH-GAMEIMAGES['player'].get_height())/2)
    playery = int((SCREENHEIGHT - GAMEIMAGES['player'].get_height())/2)
    basex = 0
    basey = int(SCREENHEIGHT - GAMEIMAGES['base'].get_height())
    while True:
        for event in pygame.event.get():
            #if user points cross button or presses escape button
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            #this will start the main function if user presses space or up arrow
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            #this shows the message and other images on the screen
            else:
                SCREEN.blit(GAMEIMAGES['background'],(0,0))#pastes image on the screen  with the given x and y components
                SCREEN.blit(GAMEIMAGES['base'],(basex,GROUNDY))
                SCREEN.blit(GAMEIMAGES['player'],(playerx, playery-100))
                SCREEN.blit(GAMEIMAGES['message'],(0, 0))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def maingame():
    #main game function
    global playery
    score = 0
    playerx = int(SCREENWIDTH/10)
    playery = int(SCREENWIDTH/2)
    # to get 2 pipes with a little difference between their x axis points
    newpipe1 = getrandompipe()
    newpipe2 = getrandompipe()

    #my list of upper pipes
    upperpipes = [
        {'x': newpipe1[0]['x'], 'y':newpipe1[0]['y']},
        {'x': newpipe2[0]['x']+200, 'y':newpipe2[0]['y']}
    ]
    #my list of lower pipes
    lowerpipes = [
        {'x': newpipe1[1]['x'], 'y':newpipe1[1]['y']},
        {'x': newpipe2[1]['x']+200, 'y':newpipe2[1]['y']}
    ]

    pipevelocity = -6
    playervelocity = 9
    playermaxvelocity = 10
    playerminvelocity = -8
    playeracceleration = 1
    playerflapacceleration = -8
    playerflapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if playery > 0:
                    playervelocity = playerflapacceleration
                    playerflapped = True
                    playery = playery - 50
                    GAMESOUNDS['wing'].play()
            
        crashtest = iscollide(playerx, playery, upperpipes, lowerpipes)
        if crashtest:
            welcomescreen()
            return

        playermidpos = playerx + GAMEIMAGES['player'].get_width()/2
        
        for pipe in upperpipes:
            pipemidpos = pipe['x'] + GAMEIMAGES['pipe'][0].get_width()/2
            if pipemidpos <= playermidpos < pipemidpos + 5:
                score += 1
                print(f"Your score is {score}")
                GAMESOUNDS['point'].play()
        if playerminvelocity < playervelocity < playermaxvelocity and not playerflapped:
            playervelocity  += playeracceleration
        if playerflapped:            
            playerflapped = False
        playery = playery + 5
        
        # to move pipe to left
        for upperpipe, lowerpipe in zip(upperpipes, lowerpipes):
            upperpipe['x'] += pipevelocity 
            lowerpipe['x'] += pipevelocity

        # TO Add new pipe before other one is removed
        if 0 < upperpipe['x'] < 5:
            # to get 2 pipes with a little difference between their x axis points
            newpipe_a = getrandompipe()
            newpipe_b = getrandompipe()
            newpipe_b[0]['x'] += 200
            newpipe_b[1]['x'] += 200
            upperpipes.append(newpipe_a[0])
            lowerpipes.append(newpipe_a[1])
            upperpipes.append(newpipe_b[0])
            lowerpipes.append(newpipe_b[1])

        #if pipe moves out of screen remove it
        if upperpipes[0]['x']  < -GAMEIMAGES['pipe'][0].get_width():
            upperpipes.pop(0)
            lowerpipes.pop(0)

        # to blit all the images
        SCREEN.blit(GAMEIMAGES['background'],(0,0))#pastes image on the screen  with the given x and y components
        for upperpipe, lowerpipe in zip(upperpipes, lowerpipes):
            SCREEN.blit(GAMEIMAGES['pipe'][0],(upperpipe['x'],upperpipe['y']))
            SCREEN.blit(GAMEIMAGES['pipe'][1],(lowerpipe['x'],lowerpipe['y']))
        SCREEN.blit(GAMEIMAGES['base'],(0,GROUNDY))
        SCREEN.blit(GAMEIMAGES['player'],(playerx, playery))
        
        mydigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in mydigits:
            width += GAMEIMAGES['numbers'][digit].get_width()
        xoffset = (SCREENWIDTH - width)/2
        for digit in mydigits:
            SCREEN.blit(GAMEIMAGES['numbers'][digit], (xoffset, 20))
            xoffset += GAMEIMAGES['numbers'][digit].get_width()
            pygame.display.update()
        FPSCLOCK.tick(FPS)
            
if __name__ == '__main__':
    #From here our game starts
    pygame.init()
    FPSCLOCK = pygame.time.Clock()#to control the FPS of the game
    pygame.display.set_caption('Flappy Bird by Muhammad Muneeb')#caption to be displayed on main screen
        
        #game images
    GAMEIMAGES['numbers'] = (pygame.image.load('gallery\\0.png').convert_alpha()
                            ,pygame.image.load('gallery\\1.png').convert_alpha()                            ,pygame.image.load('gallery\\2.png').convert_alpha()
                            ,pygame.image.load('gallery\\3.png').convert_alpha()
                            ,pygame.image.load('gallery\\4.png').convert_alpha()
                            ,pygame.image.load('gallery\\5.png').convert_alpha()
                            ,pygame.image.load('gallery\\6.png').convert_alpha()
                            ,pygame.image.load('gallery\\7.png').convert_alpha()
                            ,pygame.image.load('gallery\\8.png').convert_alpha()
                            ,pygame.image.load('gallery\\9.png').convert_alpha())
    GAMEIMAGES['message'] = pygame.image.load('gallery\\message.png').convert_alpha()
    GAMEIMAGES['base'] = pygame.image.load('gallery\\base.png').convert_alpha()
    GAMEIMAGES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image.load(PIPE).convert_alpha())
    GAMEIMAGES['background'] = pygame.image.load(BACKGROUND).convert()
    GAMEIMAGES['player'] = pygame.image.load(PLAYER).convert_alpha()

        #game sounds
    GAMESOUNDS['over'] = pygame.mixer.Sound('gallery\\audios\\over.wav')
    GAMESOUNDS['point'] = pygame.mixer.Sound('gallery\\audios\\point.wav')
    GAMESOUNDS['wing'] = pygame.mixer.Sound('gallery\\audios\\wing.wav')   

    while True:
        welcomescreen()
        maingame()
        