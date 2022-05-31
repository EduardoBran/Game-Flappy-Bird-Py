"""
EXBINDO/DIMENSIONANDO JANELA
COLOCANDO BACKGROUND
CRIANDO CLASSE DO PASSARO
POSICIONADO PASSARO NO MEIO DA IMAGEM
"""
import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 770


class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(r'images\bluebird-midflap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        ...

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load(r'images\background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.blit(BACKGROUND, (0, 0))

    bird_group.update()
    bird_group.draw(screen)


    pygame.display.update()
