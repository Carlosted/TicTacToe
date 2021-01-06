import pygame
import numpy as np

if __name__ == "__main__":
    pygame.init()

    # Loading images
    appIcon = pygame.image.load("Images/appIcon.png")
    rs = (150, 150)
    xImage = pygame.transform.scale(pygame.image.load("Images/X.png"), rs)
    oImage = pygame.transform.scale(pygame.image.load("Images/O.png"), rs)

    # Global variables
    dimensions = (600, 600)
    colorWHITE = (255, 255, 255)
    run = True
    player = 1
    board = np.zeros((3, 3), int)

    # Create screen
    screen = pygame.display.set_mode(dimensions)

    # Title and icon
    pygame.display.set_caption("TicTacToe")
    pygame.display.set_icon(appIcon)

    # Initial screen
    def resetGame():
        # White background and lines
        screen.fill(colorWHITE)
        pygame.draw.line(screen, (51), (0, 200), (600, 200))
        pygame.draw.line(screen, (51), (0, 400), (600, 400))
        pygame.draw.line(screen, (51), (200, 0), (200, 600))
        pygame.draw.line(screen, (51), (400, 0), (400, 600))

    def winCheck():
        # Checking for diagonals
        if (
            board[0][0] != 0
            and board[0][0] == board[1][1]
            and board[1][1] == board[2][2]
        ):
            return ((0, 0), (2, 2))
        if (
            board[0][2] != 0
            and board[0][2] == board[1][1]
            and board[1][1] == board[2][0]
        ):
            return ((0, 2), (2, 0))
        # Checking for rows and columns
        for i in range(3):
            if (
                board[i][0] != 0
                and board[i][0] == board[i][1]
                and board[i][1] == board[i][2]
            ):
                return ((i, 0), (i, 2))
            if (
                board[0][i] != 0
                and board[0][i] == board[1][i]
                and board[1][i] == board[2][i]
            ):
                return ((0, i), (2, i))
        for i in range(3):
            for j in range(3):
                # Checking for not tie
                if board[i][j] == 0:
                    return 0
        return None

    def endGame(cords):
        # Reversing them because I fucked up
        cord0 = cords[0][::-1]
        cord1 = cords[1][::-1]
        if cords == 0:
            print("Tie")
        else:
            pygame.draw.line(
                screen,
                (200, 0, 40),
                [s * 200 + 100 for s in cord0],
                [f * 200 + 100 for f in cord1],
                12,
            )

    # Initial update
    resetGame()
    # Game loop
    while run:
        # Input
        click = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = np.floor(np.divide(pygame.mouse.get_pos(), 200))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resetGame()
                    player = 1
                    board = np.zeros((3, 3), int)

        # Update
        # Check for win or tie
        end = winCheck()
        if end:
            endGame(end)
        if isinstance(click, np.ndarray):
            # updating board and player
            if board[int(click[1])][int(click[0])] == 0:
                board[int(click[1])][int(click[0])] = player
                if player == 1:
                    player = 2
                else:
                    player = 1

        # Show
        for i in range(3):
            for j in range(3):
                if board[j][i] == 1:
                    screen.blit(xImage, (i * 200 + 25, j * 200 + 25))
                elif board[j][i] == 2:
                    screen.blit(oImage, (i * 200 + 25, j * 200 + 25))

        pygame.display.update()
