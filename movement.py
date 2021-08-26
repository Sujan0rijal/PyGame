#crating our first game window
import pygame

#initialize pygame
pygame.init()

#create the screen
screem = pygame.display.set_mode((800,600))

#title and icons
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("D:/Python/project.png")
pygame.display.set_icon(icon)

#Adding Player
playerImg = pygame.image.load("D:/Python/project2.png")
playerX = 370
playerY = 400

def player(x, y):
    #blit--> draw
    screem.blit(playerImg, (x , y))

#game Lopp
running = True

while running:
    # RGB COLOUR to RGB for background color
    screem.fill((4, 40, 80))

    playerX += 0.01
    playerY -= 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player(playerX, playerY)

        pygame.display.update()