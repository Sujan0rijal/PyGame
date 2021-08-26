#crating our first game window
import pygame

#initialize pygame
pygame.init()

#create the screen
screem = pygame.display.set_mode((800,600))


#Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False