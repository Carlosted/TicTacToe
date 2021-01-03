import pygame
import numpy
# import board

if __name__ == "__main__":
    pass
    pygame.init()

    # Global variables
    dimensions = (600, 600)
    colorWHITE = (255, 255, 255)
    run = None

    # Create screen
    screen = pygame.display.set_mode(dimensions)

    # Title and icon
    pygame.display.set_caption('TicTacToe')
    pygame.display.set_icon(pygame.image.load('Images/appIcon.png'))

    # White background
    screen.fill(colorWHITE)
    pygame.draw.line(screen, (51), (0, 200), (600, 200))
    pygame.draw.line(screen, (51), (0, 400), (600, 400))
    pygame.draw.line(screen, (51), (200, 0), (200, 600))
    pygame.draw.line(screen, (51), (400, 0), (400, 600))

    # Game loop
    run = True
    while run:
        # Input
        click = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = numpy.floor(numpy.divide(pygame.mouse.get_pos(), 200))
        # Update

        # Show
        pygame.display.update()
        if isinstance(click, numpy.ndarray):
            print(click)
