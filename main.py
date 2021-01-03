import pygame
import numpy as np

if __name__ == "__main__":
    pygame.init()

    # Loading images
    appIcon = pygame.image.load("Images/appIcon.png")
    # xImage = pygame.image.load("Images/X.png")
    # oImage = pygame.image.load("Images/O.png")

    # Global variables
    dimensions = (600, 600)
    colorWHITE = (255, 255, 255)
    run = True
    player = 1
    # Making game screen array (0 : ' ' 1 : 'X' 2 : 'O')
    board = np.zeros((3, 3), int)

    # Create screen
    screen = pygame.display.set_mode(dimensions)

    # Title and icon
    pygame.display.set_caption("TicTacToe")
    pygame.display.set_icon(appIcon)

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
            return board[0][0]
        if (
            board[0][2] != 0
            and board[0][2] == board[1][1]
            and board[1][1] == board[2][0]
        ):
            return board[0][2]
        for i in range(board.shape[0]):
            # Checking for rows
            if (
                board[i][0] != 0
                and board[i][0] == board[i][1]
                and board[i][1] == board[i][2]
            ):
                return board[i][0]
            # Checking for columns
            if (
                board[0][i] != 0
                and board[0][i] == board[1][i]
                and board[1][i] == board[2][i]
            ):
                return board[0][i]
            for j in range(board.shape[1]):
                # Checking for not tie
                if board[i][j] == 0:
                    return 0
        return 3

    def endGame(end):
        global run
        run = False

    # Game loop
    while run:
        # Input
        click = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = np.floor(np.divide(pygame.mouse.get_pos(), 200))
        # Update
        # Check for win or tie
        end = winCheck()
        if end > 0:
            endGame(end)
        if isinstance(click, np.ndarray):
            print(click)
            print(board)
            # updating board and player
            if board[int(click[1])][int(click[0])] == 0:
                board[int(click[1])][int(click[0])] = player
                if player == 1:
                    player = 2
                else:
                    player = 1
        # Show

        pygame.display.update()
