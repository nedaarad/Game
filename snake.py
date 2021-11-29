#!/usr/bin/env python3
"""
Author : nedaarad <nedaarad@localhost>
Date   : 2021-11-29
Purpose: Rock the Casbah
"""

import random
import curses


# The curses library supplies a terminal-independent screen-painting and keyboard-handling facility for text-based terminals
# The random module is a built-in module to generate the pseudo-random variables.


s = curses.initscr()

# The initscr() function determines the terminal type and initialises all implementation data structures.
# Using curses to initialize the screen from there we can set the cursor to 0 that way doesn't show up on the screen after  

curses.curs_set(0)
sh, sw = s.getmaxyx()

# screen height and width

# The getyx macro places the current cursor position of the given window in the two integer variables y and x.

w = curses.newwin(sh, sw, 0, 0)

# The newwin() function creates a new window of a given size, returning the new window object.

w.keypad(1)
w.timeout(100)

# The keypad provides support to scan sets of keys or buttons, so it accepts keypad inputs and refresh the screen every 100 milliseconds.
# The timeout is the number of seconds you want for timeout, somehow the except fails to catch.


snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

# to create the food for just put the star in place for the food as the center of the screen go ahead and add that food
# to the screen and the food of curses is going to be by beacause next up we have to tell our snake he is going initially 

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    #for every movement of the snake we have two keys

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

        # losing if the Y position is either at the top or at the heigth of the screen or
        # if the X position is either at the left or at the width of the screen
        # or losing if snake is in itself any of these things happen

    new_head = [snake[0][0], snake[0][1]]
    # to determine the new head of the snake

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

# food location:
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)