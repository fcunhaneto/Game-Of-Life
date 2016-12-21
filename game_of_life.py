#!/usr/bin/env python3

from sys import exit

import pygame
from pygame.locals import *


def main():
    pygame.init()

    screen_size = (640, 480)
    screen = pygame.display.set_mode(screen_size, 0, 32)
    pygame.display.set_caption('Game Of Life')

    # Function that opens the game and show the rules
    language = opening_game_screen_0(screen)
    opening_game_screen_1(screen, language)
    opening_game_screen_2(screen, language)

    # Creates the points for the board lines
    lines_x, lines_y = make_board(screen_size)

    # Creates the canvas for the board
    screen.fill((255, 255, 255))

    # Draw the lines on the x-axis
    for points in lines_x:
        pygame.draw.aaline(screen, (211, 215, 207), points[0], points[1], 1)

    # Draw the lines on the y-axis
    for points in lines_y:
        pygame.draw.aaline(screen, (211, 215, 207), points[0], points[1], 1)

    # Draw the board
    pygame.display.update()

    # Creates a matrix that represents cells on the board
    cells_matrix = []
    make_cells_matrix(cells_matrix, lines_x, lines_y)

    # List of live cells on the board
    board_cells = []

    # Flag for init or end the game
    init = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    speed = 1

    while True:
        # The event loop begins
        for event in pygame.event.get():

            # Program exit event
            if event.type == QUIT:
                pygame.quit()
                exit()

            # To start the game capture the mouse clicks and create a live cells in the matrix cells
            if event.type == MOUSEBUTTONDOWN:
                i = int(event.pos[0] / 12)
                j = int(event.pos[1] / 12)
                cells_matrix[i][j] = 1
                board_cells.append((i, j))
                pygame.draw.rect(screen, (255, 0, 0), [i * 12, j * 12, 10, 10])
                pygame.display.update()
            # Begin the game when press the return key
            if event.type == KEYDOWN:
                # Se a tecla return for pressionada inicia o jogo
                if event.key == K_RETURN:
                    init = True
                if event.key == K_KP_PLUS:
                    if speed <= 60:
                        speed += 1
                if event.key == K_KP_MINUS:
                    if speed > 1:
                        speed -= 1

        if init:
            screen.fill((255, 255, 255))

            lines_x, lines_y = make_board(screen_size)

            for points in lines_x:
                pygame.draw.aaline(screen, (211, 215, 207), points[0], points[1], 1)

            for points in lines_y:
                pygame.draw.aaline(screen, (211, 215, 207), points[0], points[1], 1)

            life_cicle(len(lines_x), len(lines_y), cells_matrix, board_cells)

            for i, j in board_cells:
                pygame.draw.rect(screen, (255, 0, 0), [i * 12, j * 12, 10, 10])

            pygame.display.update()

            # --- Limit the frames per second
            clock.tick(speed)

def opening_game_screen_0(screen):
    my_font = pygame.font.Font('fonts/roboto/Roboto-Black.ttf', 16)
    text_surface_1 = my_font.render("Select Language - Selecione a Língua", True, (255, 255, 255))
    text_surface_2 = my_font.render("For english press key 1", True, (255, 255, 255))
    text_surface_3 = my_font.render("Para português tecle 2", True, (255, 255, 255))

    screen.fill((0, 0, 0))

    # Draw text in board
    screen.blit(text_surface_1, (160, 100))
    screen.blit(text_surface_2, (160, 140))
    screen.blit(text_surface_3, (160, 170))

    pygame.display.update()

    flag = True

    while flag:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_1:
                    language = 1
                    flag = False
                if event.key == K_2:
                    language = 2
                    flag = False

    return language


def opening_game_screen_1(screen, language=2):
    my_font = pygame.font.Font('fonts/roboto/Roboto-Black.ttf', 16)
    if language ==1:
        text_surface_4 = my_font.render("The Game of Life is a cellular automaton devised by the British mathematician",
                                        True, (255, 255, 255))
        text_surface_5 = my_font.render("John Horton Conway.", True, (255, 255, 255))
        text_surface_6 = my_font.render("The game was created to reproduce by simple rules, the transition and changes",
                                        True, (255, 255, 255))
        text_surface_7 = my_font.render("in living beings groups, with applications in several areas of science.",
                                        True, (255, 255, 255))
        text_surface_8 = my_font.render('The "game" is a zero-player game, meaning that its evolution is determined by',
                                        True, (255, 255, 255))
        text_surface_9 = my_font.render("its initial state, requiring no further input.",
                                        True, (255, 255, 255))
        text_surface_10 = my_font.render("Press ENTER to see the rules.", True, (255, 255, 255))

        screen.fill((0, 0, 0))

        screen.blit(text_surface_4, (40, 100))
        screen.blit(text_surface_5, (40, 120))
        screen.blit(text_surface_6, (40, 160))
        screen.blit(text_surface_7, (40, 180))
        screen.blit(text_surface_8, (40, 220))
        screen.blit(text_surface_9, (40, 240))
        screen.blit(text_surface_10, (200, 280))

    elif language == 2:
        text_surface_4 = my_font.render("O jogo da vida é um autómato celular desenvolvido pelo matemático britânico",
                                        True, (255, 255, 255))
        text_surface_5 = my_font.render("John Horton Conway.", True, (255, 255, 255))
        text_surface_6 = my_font.render("O jogo foi criado de modo a reproduzir, através de regras simples, as "
                                        "alterações", True, (255, 255, 255))
        text_surface_7 = my_font.render("e mudanças em grupos de seres vivos, tendo aplicações em diversas áreas",
                                        True, (255, 255, 255))
        text_surface_8 = my_font.render("da ciência.", True, (255, 255, 255))
        text_surface_9 = my_font.render('O "jogo" é um jogo de zero-jogador, o que significa que a sua evolução é',
                                        True, (255, 255, 255))
        text_surface_10 = my_font.render("determinada pelo seu estado inicial, não necessitando de mais entradas.",
                                         True, (255, 255, 255))
        text_surface_11 = my_font.render("Tecle ENTER para ver as regras.", True, (255, 255, 255))

        screen.fill((0, 0, 0))

        screen.blit(text_surface_4, (40, 100))
        screen.blit(text_surface_5, (40, 120))
        screen.blit(text_surface_6, (40, 160))
        screen.blit(text_surface_7, (40, 180))
        screen.blit(text_surface_8, (40, 200))
        screen.blit(text_surface_9, (40, 260))
        screen.blit(text_surface_10, (40, 280))
        screen.blit(text_surface_11, (200, 320))

    pygame.display.update()

    flag = True

    while flag:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    flag = False

    return

def opening_game_screen_2(screen, language=2):
    if language == 1:
        my_font = pygame.font.Font('fonts/roboto/Roboto-Black.ttf', 16)
        text_surface_11 = my_font.render("The rules of the game are:", True, (255, 255, 255))
        text_surface_12 = my_font.render("1- Any live cell with fewer than two live neighbours dies, as if caused",
                                        True, (255, 255, 255))
        text_surface_13 = my_font.render("     by underpopulation.", True, (255, 255, 255))
        text_surface_14 = my_font.render("2- Any live cell with two or three live neighbours lives on to the next",
                                         True, (255, 255, 255))
        text_surface_15 = my_font.render("     generation.", True, (255, 255, 255))
        text_surface_16 = my_font.render("3- Any live cell with more than three live neighbours dies, as if by",
                                         True, (255, 255, 255))
        text_surface_17 = my_font.render("      overpopulation.", True, (255, 255, 255))
        text_surface_18 = my_font.render("4- Any dead cell with exactly three live neighbours becomes a live cell,",
                                         True, (255, 255, 255))
        text_surface_19 = my_font.render("     as if by reproduction.", True, (255, 255, 255))
        text_surface_20 = my_font.render("It is important to understand that all births and deaths occur",
                                         True, (255, 255, 255))
        text_surface_21 = my_font.render('simultaneously. Together they constitute a generation or, as we call them, ',
                                         True, (255, 255, 255))
        text_surface_22 = my_font.render('an "instant" in the life story of the complete initial configuration.',
                                         True, (255, 255, 255))
        text_surface_23 = my_font.render('As soon as you press ENTER the board is show and you can choose the',
                                         True, (255, 255, 255))
        text_surface_24 = my_font.render('your initial settings by selecting with the mouse the squares in the board.',
                                         True, (255, 255, 255))
        text_surface_25 = my_font.render('Once your initial configuration is set, press ENTER and the game starts.',
                                         True, (255, 255, 255))

        screen.fill((0, 0, 0))

        screen.blit(text_surface_11, (60, 20))
        screen.blit(text_surface_12, (60, 50))
        screen.blit(text_surface_13, (60, 70))
        screen.blit(text_surface_14, (60, 100))
        screen.blit(text_surface_15, (60, 120))
        screen.blit(text_surface_16, (60, 150))
        screen.blit(text_surface_17, (60, 170))
        screen.blit(text_surface_18, (60, 200))
        screen.blit(text_surface_19, (60, 220))
        screen.blit(text_surface_20, (60, 250))
        screen.blit(text_surface_21, (60, 270))
        screen.blit(text_surface_22, (60, 290))
        screen.blit(text_surface_23, (60, 320))
        screen.blit(text_surface_24, (60, 340))
        screen.blit(text_surface_25, (60, 370))

    elif language == 2:
        my_font = pygame.font.Font('fonts/roboto/Roboto-Black.ttf', 16)
        text_surface_12 = my_font.render("As regras do jogo são:", True, (255, 255, 255))
        text_surface_13 = my_font.render("1- Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.",
                                         True, (255, 255, 255))
        text_surface_14 = my_font.render("2- Qualquer célula viva com mais de três vizinhos vivos morre de",
                                         True, (255, 255, 255))
        text_surface_15 = my_font.render("     superpopulação.", True, (255, 255, 255))
        text_surface_16 = my_font.render("3- Qualquer célula morta com exatamente três vizinhos vivos se torna uma",
                                         True, (255, 255, 255))
        text_surface_17 = my_font.render("     célula viva.", True, (255, 255, 255))
        text_surface_18 = my_font.render("4- Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo",
                                         True, (255, 255, 255))
        text_surface_19 = my_font.render("     estado para a próxima geração.", True, (255, 255, 255))
        text_surface_20 = my_font.render("É importante entender que todos os nascimentos e mortes ocorrem",
                                         True, (255, 255, 255))
        text_surface_21 = my_font.render('simultaneamente. Juntos eles constituem uma geração ou, como podemos',
                                         True, (255, 255, 255))
        text_surface_22 = my_font.render('chamá-los, um "instante" na história da vida completa da configuração inicial.',
                                         True, (255, 255, 255))
        text_surface_23 = my_font.render('Assim que você teclar ENTER e mostrado o tabuleiro e você pode escolher as',
                                         True, (255, 255, 255))
        text_surface_24 = my_font.render('suas configurações iniciais selecionando com o mouse os quadrados no',
                                         True, (255, 255, 255))
        text_surface_25 = my_font.render('tabuleiro.',
                                         True, (255, 255, 255))
        text_surface_26 = my_font.render('Definida a sua configuração inicial tecle ENTER e o jogo inicia.',
                                         True, (255, 255, 255))

        screen.fill((0, 0, 0))

        screen.blit(text_surface_12, (40, 20))
        screen.blit(text_surface_13, (40, 50))
        screen.blit(text_surface_14, (40, 80))
        screen.blit(text_surface_15, (40, 100))
        screen.blit(text_surface_16, (40, 130))
        screen.blit(text_surface_17, (40, 150))
        screen.blit(text_surface_18, (40, 180))
        screen.blit(text_surface_19, (40, 200))
        screen.blit(text_surface_20, (40, 230))
        screen.blit(text_surface_21, (40, 250))
        screen.blit(text_surface_22, (40, 270))
        screen.blit(text_surface_23, (40, 310))
        screen.blit(text_surface_24, (40, 330))
        screen.blit(text_surface_25, (40, 350))
        screen.blit(text_surface_26, (40, 390))

    pygame.display.update()

    flag = True

    while flag:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    flag = False

    return

def make_board(size):
    """Creates the lines in the x and y axis."""
    width, height = size
    lines_x = [[(0, y), (width, y)] for y in range(11, height, 12)]
    lines_y = [[(x, 0), (x, height)] for x in range(11, width, 12)]

    return (lines_x, lines_y)


def make_cells_matrix(cells_matrix, lines, columns):
    """Creates an array with all squares of the board with a value of 0.
       Where zero means empty and 1 means occupied.
    """
    for i in range(0, len(lines)):
        col = []
        for j in range(0, len(columns)):
            col.append(0)

        cells_matrix.append(col)

def life_cicle(lines, columns, cells_matrix, board_cells):
    """Defines death or creation of cells according to the rules of the game"""

    line = []
    for i in range(lines):
        column = []
        for j in range(columns):
            cells = 0
            if i > 0 and j > 0:
                if cells_matrix[i - 1][j - 1] == 1:
                    cells += 1
            if i > 0:
                if cells_matrix[i - 1][j] == 1:
                    cells += 1
            if i > 0 and j < (columns - 1):
                if cells_matrix[i - 1][j + 1] == 1:
                    cells += 1
            if j < (columns - 1):
                if cells_matrix[i][j + 1] == 1:
                    cells += 1
            if i < (lines - 1) and j < (columns - 1):
                if cells_matrix[i + 1][j + 1] == 1:
                    cells += 1
            if i < (lines - 1):
                if cells_matrix[i + 1][j] == 1:
                    cells += 1
            if i < (lines - 1) and j > 0:
                if cells_matrix[i + 1][j - 1] == 1:
                    cells += 1
            if j > 0:
                if cells_matrix[i][j - 1] == 1:
                    cells += 1

            column.append(cells)

        line.append(column)

    for i in range(lines):
        for j in range(columns):
            if cells_matrix[i][j] == 1:
                if line[i][j] < 2 or line[i][j] > 3:
                    cells_matrix[i][j] = 0
                    board_cells.remove((i, j))
            if cells_matrix[i][j] == 0:
                if line[i][j] == 3:
                    cells_matrix[i][j] = 1
                    board_cells.append((i, j))

main()