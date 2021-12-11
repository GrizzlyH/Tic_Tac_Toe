import pygame

pygame.init()

#  Game variables
WIDTH = 900
HEIGHT = 900


#  Creating the pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


gameLoop = True
while gameLoop:

    #  Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False


    pygame.display.update()

pygame.quit()