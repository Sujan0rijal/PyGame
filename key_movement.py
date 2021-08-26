import pygame

# initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('D:/Python/project.png')
pygame.display.set_icon(icon)

# Adding player
playerImg = pygame.image.load('D:/Python/project2.png')
playerX = 370
playerY = 480
playerX_change = 0
# x and y coordinate passed
def player(x,y):
    #blit --> draw
    screen.blit(playerImg, (x,y))

# Game loop
running = True


while running:

    # RGB COLOR TO RGB for background color
    screen.fill((4, 40, 80))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # if keystroke is pressed whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                #Increase to 0.3 if u want to increase the spped
                playerX_change = -0.2

            if event.key == pygame.K_RIGHT:
                playerX_change = +0.2

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    player(playerX, playerY)

    pygame.display.update()
