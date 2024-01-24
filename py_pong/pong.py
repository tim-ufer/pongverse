import os
from time import sleep
import numpy as np
import curses


def print_mat(mat):
    for x in mat:
        for y in x:
            print(y, end='')
        print()


def refresh(mat):
    os.system('clear')
    print_mat(mat)
    # sleep(1)


def main(*args):
    xs = 16
    ys = 41
    center_v = xs // 2
    center_h = ys // 2
    wall_h = '\u23BA'
    wall_v = '\u2502'
    paddle = '\u2503'
    ball = '\u2B57'
    mat = np.empty([xs, ys], dtype=object)
    mat[:, :] = ' '
    # Define walls
    mat[0, :] = '\u23BD'
    mat[xs-1, :] = wall_h
    mat[1:xs-1, 0] = wall_v
    mat[1:xs-1, ys-1] = wall_v
    # Set up paddles and ball
    mat[center_v-1:center_v+1, 1] = paddle
    mat[center_v-1:center_v+1, ys-2] = paddle
    mat[center_v, center_h] = ball
    player_pos = center_v
    # Set up curses to get live input
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()

    gameover = False
    while not gameover:
        refresh(mat)
        # action = input('Press k/j for up/down:\n')
        action = screen.getkey()
        if action == 'k' and player_pos > 2:
            mat[player_pos, 1] = ' '
            mat[player_pos-2, 1] = paddle
            player_pos -= 1
        elif action == 'j' and player_pos < xs-2:
            mat[player_pos-1, 1] = ' '
            mat[player_pos+1, 1] = paddle
            player_pos += 1

    print()
    
    curses.nocbreak()
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    curses.wrapper(main())
