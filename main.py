import pygame

pygame.init()

# Global variables
dimensions = (600, 600)
colorWHITE = (255, 255, 255)

# Create screen
screen = pygame.display.set_mode(dimensions)

# Title and icon
pygame.display.set_caption('TicTacToe', )
pygame.display.set_icon(pygame.image.load('appIcon.png'))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Setting background color to white
    screen.fill(colorWHITE)
    pygame.display.update()
