#!/usr/bin/env python3
import curses

ctx = curses.initscr()
curses.cbreak()
curses.noecho()
curses.curs_set(0)
ctx.keypad(True)

curses.nocbreak()
ctx.keypad(0)
curses.echo()
curses.curs_set(1)
curses.endwin()

del ctx
