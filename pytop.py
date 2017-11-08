#!/usr/bin/env python

import sys
from time import sleep
import curses
import atexit
import psutil

'''
PyTop - Sean Browning
Based on the TOP clone by Giampaolo Rodola <g.rodola@gmail.com>

My own take on a platform independent python htop clone, sans actual process info.
Mainly for looking at load info as processes are running.
depends on the curses library, which is not traditionally for windows.

One workaround for that is through the following:
1. find the relevant file on https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses
2. install wheel (if not already installed) via pip install wheel
3. navigate to the .whl file and install with pip install
'''

def tear_down():
# Clear the window when we exit
    window.keypad(0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()

# Initial curses setup

window = curses.initscr()
curses.endwin()

def print_line(lineno, text):
# a wrapper around curses.addstr()
    window.addstr(lineno, 0, text, 0)

def get_dashes(perc):
    dashes = "|" * int((float(perc) / 10 * 4))
    empty_dashes = " " * (40 - len(dashes))
    return dashes, empty_dashes

def cpu_speed(lineno):
    speed = psutil.cpu_freq()
    perc = (speed.current / speed.max * 100)
    dashes, empty_dashes = get_dashes(perc)

    line = " Freq  [%s%s] %5s%% %s / %s" % (
        dashes, empty_dashes,
        perc,
        str(int(speed.current)) + "MHz",
        str(int(speed.max)) + "MHz"
    )
    print_line(lineno, line)

def mem_load(lineno):
    mem = psutil.virtual_memory()
    dashes, empty_dashes = get_dashes(mem.percent)
    line = " Mem   [%s%s] %5s%% %6s / %s" % (
        dashes, empty_dashes,
        mem.percent,
        str(int(mem.used / 1024 / 1024)) + "M",
        str(int(mem.total / 1024 / 1024)) + "M"
        )
    print_line(lineno, line)

def swap_load(lineno):
    swap = psutil.swap_memory()
    dashes, empty_dashes = get_dashes(swap.percent)
    line = " Swap  [%s%s] %5s%% %6s / %s" % (
        dashes, empty_dashes,
        swap.percent,
        str(int(swap.used / 1024 / 1024)) + "M",
        str(int(swap.total / 1024 / 1024)) + "M"
        )
    print_line(lineno, line)

def cpu_load():
    percs = psutil.cpu_percent(interval=0, percpu=True)
    for cpu_num, perc in enumerate(percs):
        dashes, empty_dashes = get_dashes(perc)
        print_line(cpu_num, " CPU%-2s [%s%s] %5s%%" % (cpu_num, dashes, empty_dashes, perc))

def main():
    # i = 0
    # while i < 10000:
    #     window.erase()
    #     if i % 2 == 0:
    #         print_line(0, str(i))
    #     else:
    #         print_line(1, str(i))
    #     i += 1
    #     window.refresh()
    #     sleep(2)
    while True:
        cpunum = psutil.cpu_count()
        window.erase()
        cpu_load()
        cpu_speed(cpunum)
        mem_load(cpunum + 1)
        swap_load(cpunum + 2)
        window.refresh()
        sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        tear_down()
