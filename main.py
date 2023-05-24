import pygame as g

from board import Board

g.init()

WINDOW_SIZE = (600, 600)
screen = g.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])


def draw(display):
    display.fill('white')
    board.draw(display)
    g.display.update()


if __name__ == '__main__':
    running = True
    while running:
        mx, my = g.mouse.get_pos()
        for event in g.event.get():
            if event.type == g.QUIT:
                running = False

            elif event.type == g.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.click(mx, my)

        if board.is_in_checkmate('black'):
            print('White wins!')
            running = False
        elif board.is_in_checkmate('white'):
            print('Black wins!')
            running = False

        draw(screen)
