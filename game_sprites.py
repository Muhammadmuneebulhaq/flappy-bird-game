import pygame
from settings import *
 
GAMEIMAGES = {}
GAMESOUNDS = {}
PLAYER = 'gallery\\bird.png'
BACKGROUND = 'gallery\\background.png'
PIPE = 'gallery\\pipe.png'
pygame.init()
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
gameimages_player = pygame.image.load(PLAYER).convert_alpha()

        #game sounds
GAMESOUNDS['over'] = pygame.mixer.Sound('gallery\\audios\\over.wav')
GAMESOUNDS['point'] = pygame.mixer.Sound('gallery\\audios\\point.wav')
GAMESOUNDS['wing'] = pygame.mixer.Sound('gallery\\audios\\wing.wav')