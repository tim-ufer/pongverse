import numpy as np
import curses


def refresh(stdscr, mat):
    for i, x in enumerate(mat):
        for j, y in enumerate(x):
            stdscr.addstr(i, j, y, curses.A_NORMAL)
    stdscr.refresh()


def main(stdscr):
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
    gameover = False
    while not gameover:
        refresh(stdscr, mat)
        # action = input('Press k/j for up/down:\n')
        action = stdscr.getkey()
        if action == 'k' and player_pos > 2:
            mat[player_pos, 1] = ' '
            mat[player_pos-2, 1] = paddle
            player_pos -= 1
        elif action == 'j' and player_pos < xs-2:
            mat[player_pos-1, 1] = ' '
            mat[player_pos+1, 1] = paddle
            player_pos += 1
        # break

    # print()
    # print(mat)


if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.curs_set(False)
    curses.wrapper(main)

