import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pygame

from jogo_da_velha import criar_board, faz_movimento, get_input_valido, \
    print_board, verifica_ganhador, verifica_movimento

from mininmax import movimento_ia

pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

pygame.font.init()

def draw_board(win, board):
    height = 600
    width = 600
    tamanho = 600/3

    for i in range(1, 3):
        pygame.draw.line(win, (0,0,0),
                         (0,i * tamanho),
                         (width, i, + tamanho), 3)

        pygame.draw.line(win, (0, 0, 0),
                         (i * tamanho, 0),
                         (i * tamanho, height), 3)

    for i in range(1, 3):
        for j in range(1, 3):
            font = pygame.font.SysFont('comicsans', 100)

            x = j * tamanho
            y = i * tamanho

            text = font.render(board[i][j], 1, (0,0,0))
            win.blit(text, ((x + 75), (y + 75)))

def redraw_window(win, board):
    win.fill((153, 51, 153))
    draw_board(win, board)

def main():
    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Jogo da Véia")

    board = criar_board()

    redraw_window(win, board)
    pygame.display.update()

    jogador = 0
    ganhador = verifica_ganhador(board)