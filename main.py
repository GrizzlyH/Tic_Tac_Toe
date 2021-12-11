import pygame

pygame.init()

#  Game variables
WIDTH = 900
HEIGHT = 900
mouseClicked = False
player = 1

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#  Creating the pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

def update_board(board, x, y, player):
    if board[x][y] == 0:
        board[x][y] = player
        if player == 1:
            player = 2
            return player
        else:
            player = 1
            return player
    else:
        return player


def cell_collision(boardRect, pos):
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


def board():
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


board = board()
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
            x, y = cell_collision(boardRect, pos)
            player = update_board(board, x, y, player)
            print(board)

    pygame.display.update()

pygame.quit()