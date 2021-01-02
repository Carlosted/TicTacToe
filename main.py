import pygame, sys
pygame.init()

dimensions = (600, 600)


screen = pygame.display.set_mode(dimensions)

screen.fill((255, 255, 255))
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
