#!/usr/bin/env python3

import os
import sys

def read_file(inputfile):
    with open(inputfile) as file:
        return [eachLine.rstrip() for eachLine in file]


def part_1(data):
    total = 0
    for eachRow in data:
        wnums, anums = eachRow.split(':')[1].split('|')
        wnums = [eachNum for eachNum in wnums.split(' ') if eachNum]
        anums = [eachNum for eachNum in anums.split(' ') if eachNum]
        numofwinners = len(set(wnums).intersection(set(anums)))
        if numofwinners:
            total += 2**(numofwinners-1)

    return total

def part_2(data):
    total = 0
    extrawinners = []
    for eachRow in data:
        # Always one more 
        total += 1
        modifier = 1
        if extrawinners:
            extracopiesofcard = extrawinners.pop(0)
            total += extracopiesofcard
            modifier += extracopiesofcard
        wnums, anums = eachRow.split(':')[1].split('|')
        wnums = [eachNum for eachNum in wnums.split(' ') if eachNum]
        anums = [eachNum for eachNum in anums.split(' ') if eachNum]
        numofwinners = len(set(wnums).intersection(set(anums)))
        for i in range(0,numofwinners):
            if i < len(extrawinners):
                extrawinners[i] += 1 * modifier
            else:
                extrawinners.append(1 * modifier)
    return total

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments.")

    inputfile = sys.argv[1]

    if not os.path.exists(inputfile):
        sys.exit(f"{inputfile} does not exist.")
    
    data = read_file(inputfile)
    p1total = part_1(data)
    p2total = part_2(data)

    print(f"Part 1: {p1total}")
    print(f"Part 2: {p2total}")


if __name__ == '__main__':
    main()
