#!/usr/bin/env python3

import os
import re
import sys

GAME_NUM = re.compile(r'Game (\d+):')
PART1_POSSIBLE = {'red': 12,
                  'green': 13,
                  'blue': 14}

def read_file(inputfile):
    p1total = 0
    p2total = 0
    with open(inputfile) as file:
        for eachLine in file:
            p1total += part_1(eachLine)
            p2total += part_2(eachLine)
    return p1total, p2total

def part_1(eachline):
    gamenum = re.match(GAME_NUM, eachline)[1]
    for eachColor, eachCount in PART1_POSSIBLE.items():
        pattern = re.compile(f"(\d+) {eachColor}")
        for eachMatch in re.finditer(pattern, eachline):
            if int(eachMatch[1]) > eachCount:
                return 0
    return int(gamenum)

def part_2(eachline):
    colors = {'red': 0,
              'green': 0,
              'blue': 0}
    for eachColor in colors.keys():
        max = 0
        pattern = re.compile(f"(\d+) {eachColor}")
        for eachMatch in re.finditer(pattern, eachline):
            gamecount = int(eachMatch[1])
            if gamecount > max:
                max = gamecount
        colors[eachColor] = max
    power = 1
    for eachValue in colors.values():
        power *= eachValue
    return power

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments.")

    inputfile = sys.argv[1]

    if not os.path.exists(inputfile):
        sys.exit(f"{inputfile} does not exist.")
    
    p1total,p2total = read_file(inputfile)
    print(f"Part 1: {p1total}")
    print(f"Part 2: {p2total}")


if __name__ == '__main__':
    main()
