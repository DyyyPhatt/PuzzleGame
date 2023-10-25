import pygame
from buttons import *
import drawing
import imples 
import sys
import consoles

pygame.init()

fpsClock = pygame.time.Clock()
FPS = 60
def main():
    global soLan
    soLan = 0
    gameBanDau = consoles.khoiTao(3)
    game = [row[:] for row in gameBanDau]
    drawing.draw_board(game,soLan)
    while True:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                soLan = 0
                if button_random.collidepoint(event.pos):
                    gameBanDau = consoles.khoiTao(3)
                    game = [row[:] for row in gameBanDau]
                    drawing.draw_board(game,soLan)
                elif button_BFS.collidepoint(event.pos):
                    imples.BFS(game)
                elif button_DFS.collidepoint(event.pos):
                    imples.DFS(game)
                elif button_ID.collidepoint(event.pos):
                    imples.ID(game,10,100)
                elif button_A.collidepoint(event.pos):
                    imples.A_star(game)
                elif button_UCS.collidepoint(event.pos):
                    imples.UCS(game)
                elif button_Reset.collidepoint(event.pos):
                    game = [row[:] for row in gameBanDau]
                    drawing.draw_board(game,soLan)
                elif button_Greedy.collidepoint(event.pos):
                    imples.Greedy(game)

            elif event.type == pygame.KEYDOWN:
                soLan +=1  
                if event.key == pygame.K_LEFT:
                    consoles.move(game, 'left')
                elif event.key == pygame.K_RIGHT:
                    consoles.move(game, 'right')
                elif event.key == pygame.K_UP:                        
                    consoles.move(game, 'up')
                elif event.key == pygame.K_DOWN:
                    consoles.move(game, 'down')
                drawing.draw_board(game, soLan)

            if consoles.check(game):
                win()
                soLan = 0

        pygame.display.update()    
        fpsClock.tick(FPS) 
         
main()