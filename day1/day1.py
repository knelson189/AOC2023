#!/usr/bin/env python3

import os
import re
import sys

REGEX_DIGITS = re.compile(r'\d')
WORD_NUMBERS = {
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9'
}

def read_file(inputfile):
    total = 0
    with open(inputfile) as file:
        for eachLine in file:
            firstnum, lastnum = find_numbers(eachLine)
            linenum = int(firstnum + lastnum)
            total += linenum
    return total
            
def find_numbers(inputline):
    index_replacements = {}
    for eachWord, eachNum in WORD_NUMBERS.items():
        for eachMatch in re.finditer(eachWord, inputline):
            index_replacements[eachMatch.start()] = eachNum
    index_increase = 0
    for eachIndex, eachNum in sorted(index_replacements.items()):
        inputline = inputline[:eachIndex+index_increase] + eachNum + inputline[eachIndex+index_increase:]
        index_increase += 1

    allnums = re.findall(REGEX_DIGITS, inputline)

    return allnums[0], allnums[-1]

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments.")

    inputfile = sys.argv[1]

    if not os.path.exists(inputfile):
        sys.exit(f"{inputfile} does not exist.")
    
    total = read_file(inputfile)
    print(total)


if __name__ == '__main__':
    main()
