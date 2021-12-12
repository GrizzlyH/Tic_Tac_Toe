import pygame

pygame.init()

#  Game variables
WIDTH = 900
HEIGHT = 900
mouseClicked = False
player = 1
WINNER = 0
GAMEOVER = False
font = pygame.font.SysFont('sans', 40)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#  Creating the pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


def end_screen(board, player, gameLoop):
    global GAMEOVER
    if GAMEOVER:
        winText = f"The winner is Player {WINNER}"
        winTextImg = font.render(winText, True, BLACK)
        pygame.draw.rect(screen, RED, (WIDTH//2 - 160, HEIGHT//2 - 150, 320, 50))
        screen.blit(winTextImg, (WIDTH//2 - 160, HEIGHT//2 - 150))

        againText = f"Play again?"
        againTextImg = font.render(againText, True, BLACK)
        again = pygame.draw.rect(screen, GREEN, (WIDTH//2 - 80, HEIGHT // 2 - 80, 170, 50))
        screen.blit(againTextImg, (WIDTH//2 - 80, HEIGHT // 2 - 80))

        quitText = f"Quit"
        quitTextImg = font.render(quitText, True, BLACK)
        quitButton = pygame.draw.rect(screen, GREEN, (WIDTH//2 - 50, HEIGHT // 2 - 20, 80, 50))
        screen.blit(quitTextImg, (WIDTH//2 - 50, HEIGHT // 2 - 20))

        if again.collidepoint(pos):
            GAMEOVER = False
            player = 1
            board = make_board()
            print(board)
            return gameLoop, board, player
        elif quitButton.collidepoint(pos):
            gameLoop = False
            return gameLoop, board, player
        else:
            return gameLoop, board, player


def check_for_winner(board):
    """Determine if a winning move has been made"""
    global GAMEOVER
    global WINNER
    for rows in board:
        if not 0 in rows:
            if sum(rows) == 3 or sum(rows) == 6:
                WINNER = player
                print(f'The winner is {player}')
                GAMEOVER = True
    for i in range(0, 3):
        if board[0][i] * board[1][i] * board[2][i] == 1 or board[0][i] * board[1][i] * board[2][i] == 8:
            WINNER = player
            print(f'The winner is {player}')
            GAMEOVER = True
    if board[0][0] * board[1][1] * board[2][2] == 1 or board[0][0] * board[1][1] * board[2][2] == 8:
        WINNER = player
        print(f'The winner is {player}')
        GAMEOVER = True
    if board[0][2] * board[1][1] * board[2][0] == 1 or board[0][2] * board[1][1] * board[2][0] == 8:
        WINNER = player
        print(f'The winner is {player}')
        GAMEOVER = True
    if not 0 in board[0] and not 0 in board[1] and not 0 in board[2]:
        WINNER = player
        print(f"The game is a Tie")
        GAMEOVER = True


def draw_marker(board):
    """Update the game visually as per the updated board"""
    for i, rows in enumerate(board):
        for j, item in enumerate(rows):
            if item == 1:
                pygame.draw.line(screen, RED, (WIDTH//3*j + 25, HEIGHT//3*i +25), (WIDTH//3 * (j+1) -25, HEIGHT//3*(i+1) -25), 10)
                pygame.draw.line(screen, RED, (WIDTH//3*(j+1) - 25, HEIGHT//3*i +25), (WIDTH//3 * j +25, HEIGHT//3*(i+1) -25), 10)
            elif item == 2:
                pygame.draw.circle(screen, GREEN, (WIDTH//3*j +150, HEIGHT//3*i +150), 125, 10)


def update_board(board, x, y, player):
    """Check to see if the cell selected is valid, then select cell, check for winner, and change player"""
    if board[x][y] == 0:
        board[x][y] = player
        check_for_winner(board)
        if player == 1:
            player = 2
            return player
        else:
            player = 1
            return player
    else:
        return player


def cell_collision(boardRect, pos):
    """Return indices of cell selected"""
    for x, rows in enumerate(boardRect):
        for y, columns in enumerate(rows):
            if columns.collidepoint(pos):
                return x, y


def board_rects(board):
    """Creates an array of pygame Rectangles in order to enable Mouse Collision Detection"""
    boardRect = []
    for a, rows in enumerate(board):
        columnList = []
        for b, columns in enumerate(rows):
            columnList.append(pygame.Rect(WIDTH//3*b, HEIGHT//3*a, WIDTH//3, HEIGHT//3))
        boardRect.append(columnList)
    return boardRect


def make_board():
    """This function creates the game board in an array"""
    board = []
    for i in range(1, 4):
        columnList = []
        for x in range(1, 4):
            columnList.append(0)
        board.append(columnList)
    return board


def draw_board():
    """This function draws the game background to the screen"""
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (WIDTH//3 * i, 25), (WIDTH//3 * i, HEIGHT - 25), 10)
        pygame.draw.line(screen, BLACK, (25, HEIGHT//3 * i), (WIDTH-25, HEIGHT//3 * i), 10)


board = make_board()
boardRect = board_rects(board)

gameLoop = True
while gameLoop:

    # Draw the board to the screen
    draw_board()

    #  Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.MOUSEBUTTONDOWN and mouseClicked == False:
            mouseClicked = True
        if event.type == pygame.MOUSEBUTTONUP and mouseClicked == True:
            mouseclicked = False
            pos = pygame.mouse.get_pos()
            if not GAMEOVER:
                x, y = cell_collision(boardRect, pos)
                player = update_board(board, x, y, player)
                print(board)

    draw_marker(board)
    if GAMEOVER == True:
        gameLoop, board, player = end_screen(board, player, gameLoop)
    pygame.display.update()

pygame.quit()