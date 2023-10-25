#drawing.py
import pygame
from displays import *
import buttons 

def draw_board(board, soLan):
    n = len(board)
    DISPLAYSURF.fill('#000000')
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                left= 20 + j * ( KichThuocOvuong - 18)
                top = 70 + i * (KichThuocOvuong - 18)
                pygame.draw.rect(DISPLAYSURF, '#800000', (left, top , KichThuocOvuong - 20 , KichThuocOvuong - 20), 4)
            
                font = pygame.font.Font(None, 36)
                text = font.render(str(board[i][j]), True, '#FFFFFF')
                text_rect = text.get_rect(center=(left + KichThuocOvuong // 2 -10, top + KichThuocOvuong // 2 -10))
                DISPLAYSURF.blit(text, text_rect)
    buttons.hienButton()
    score_views(soLan)
    pygame.display.update()

def veButton(surface, rect, color, text, text_color, font_size):
    pygame.draw.rect(surface, color, rect)
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def veChu(Surface, rect, fontSize, chu, color):
    font = pygame.font.Font(None, fontSize)
    text = font.render(chu, True, color)
    text_rect = text.get_rect(center=rect.center)
    Surface.blit(text, text_rect)

def score_views(soLan):
    font = pygame.font.Font(None, 50)
    text = font.render(f"Score: {soLan}", True, '#FFFFFF')
    text_rect = text.get_rect(center= (375, 95))
    DISPLAYSURF.blit(text, text_rect)

    pygame.display.update()

def win():
    font = pygame.font.Font(None, 45)
    text = font.render("Congaratulation, winner!", True, '#228B22')
    score_hcn = text.get_rect(center = (230,30))
    DISPLAYSURF.blit(text, score_hcn)
    pygame.display.update()
    
def no_solver():
    font = pygame.font.Font(None, 45)
    text = font.render("No solution found!", True, '#DC143C')
    score_hcn = text.get_rect(center = (230,30))
    DISPLAYSURF.blit(text, score_hcn)
    pygame.display.update()
    
def print_solver():
    font = pygame.font.Font(None, 45)
    text = font.render("Looking for a solution!", True, '#228B22')
    score_hcn = text.get_rect(center = (230,30))
    DISPLAYSURF.blit(text, score_hcn)
    pygame.display.update()