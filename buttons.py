import pygame
from drawing import *
import displays 

button_random = pygame.Rect(310, 140 , 140, 60)
button_Reset = pygame.Rect(310, 230 , 140, 60)

button_BFS = pygame.Rect(20,350, 120, 60)
button_DFS= pygame.Rect(170, 350, 120, 60)
button_UCS = pygame.Rect(320, 350, 120, 60)

button_Greedy = pygame.Rect(20, 440, 120, 60)
button_ID = pygame.Rect(170, 440, 120, 60)
button_A = pygame.Rect(320, 440, 120, 60)

khungDiem = pygame.Rect(375, 80, 100, 60)

def hienButton():
    btnRandom(DISPLAYSURF)
    btnBFS(DISPLAYSURF)
    btnDFS(DISPLAYSURF)
    btnReset(DISPLAYSURF)   
    btnGreedy(DISPLAYSURF)
    btnID(DISPLAYSURF)
    btnUCS(DISPLAYSURF)
    btnA(DISPLAYSURF)
    pygame.display.update()

def btnDFS(DISPLAYSURF):
    veButton(DISPLAYSURF, button_DFS, '#FFBF00', "DFS", '#FFFFFF', 30)
def btnRandom(DISPLAYSURF):
    veButton(DISPLAYSURF, button_random, '#FFDEAD', "CREATE GAME", '#FFFFFF', 25)
def btnBFS(DISPLAYSURF):
    veButton(DISPLAYSURF, button_BFS, '#F0DC82', "BFS", '#FFFFFF', 30)
def btnUCS(DISPLAYSURF):
    veButton(DISPLAYSURF, button_UCS, '#CC5500', "UCS", '#FFFFFF', 30)
def btnReset(DISPLAYSURF):
    veButton(DISPLAYSURF, button_Reset, '#DC143C', "RESET GAME", '#FFFFFF', 25)
def btnGreedy(DISPLAYSURF):
    veButton(DISPLAYSURF, button_Greedy, '#ACE1AF', "GREEDY", '#FFFFFF', 25)
def btnID(DISPLAYSURF):
    veButton(DISPLAYSURF, button_ID, '#00A86B', "ID-10", '#FFFFFF', 30)
def btnA(DISPLAYSURF):
    veButton(DISPLAYSURF, button_A, '#FF7F50', "A*", '#FFFFFF', 30)