#!/usr/bin/env python3

import os
import re
import sys

def read_file(inputfile):
    enginedata = []
    with open(inputfile) as file:
        for eachLine in file:
            enginedata.append([*eachLine.rstrip()])
    return enginedata

def part_1(enginedata):
    numstartindex = None
    currentnumber = None
    numendindex = None
    total = 0
    for eachRowIndex, eachRowData in enumerate(enginedata):
        rowlength = len(eachRowData)
        for eachColIndex, eachChar in enumerate(eachRowData):
            if eachChar.isdigit():
                if currentnumber:
                    currentnumber = currentnumber + eachChar
                    numendindex = eachColIndex
                else:
                    currentnumber = eachChar
                    numstartindex = eachColIndex
                    numendindex = eachColIndex
            else:
                if currentnumber:
                    if valid_number_check(enginedata, eachRowIndex, numstartindex, numendindex, rowlength):
                        total += int(currentnumber)
                    numstartindex = None
                    currentnumber = None
                    numendindex = None

        # check if number at the end of the row
        if currentnumber:
            if valid_number_check(enginedata, eachRowIndex, numstartindex, numendindex, rowlength):
                total += int(currentnumber)
            numstartindex = None
            currentnumber = None
            numendindex = None

    return total
                    
def valid_number_check(enginedata, rowindex, colindexstart, colindexend, rowlength):
    # Make sure I don't go outside the bounds of the size of enginedata
    for eachRowIndex in range( max(0, rowindex-1), min(rowindex+2, len(enginedata))):
        for eachColIndex in range( max(0, colindexstart-1), min(colindexend+2, rowlength)):
            if not enginedata[eachRowIndex][eachColIndex].isdigit() and enginedata[eachRowIndex][eachColIndex] != '.':
                return True
    return False

def part_2(enginedata):
    total = 0
    for eachRowIndex, eachRowData in enumerate(enginedata):
        rowlength = len(eachRowData)
        for eachColIndex, eachChar in enumerate(eachRowData):
            if eachChar == '*':
                num1, num2 = valid_gear_check(enginedata, eachRowIndex, eachColIndex, rowlength)
                if num1 and num2:
                    total += (num1 * num2)
    return total

def valid_gear_check(enginedata, rowindex, colindex, rowlength):
    validnumbers = set()
    for eachRowIndex in range( max(0, rowindex-1), min(rowindex+2, len(enginedata))):
        for eachColIndex in range( max(0, colindex-1), min(colindex+2, rowlength)):
            if enginedata[eachRowIndex][eachColIndex].isdigit():
                validnumbers.add(get_numbers_from_row(enginedata, eachRowIndex, eachColIndex))
    if len(validnumbers) == 2:
        return validnumbers
    else:
        return 0, 0
                
def get_numbers_from_row(enginedata, rowindex, colindex):
    currentnumber = None
    returnnumber = False
    for eachColIndex, eachChar in enumerate(enginedata[rowindex]):
        if eachColIndex == colindex:
            returnnumber = True
        if eachChar.isdigit():
            if currentnumber:
                currentnumber = currentnumber + eachChar
            else:
                currentnumber = eachChar
        else:
            if returnnumber:
                return int(currentnumber)
            else:
                currentnumber = None

def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments.")

    inputfile = sys.argv[1]

    if not os.path.exists(inputfile):
        sys.exit(f"{inputfile} does not exist.")
    
    enginedata = read_file(inputfile)
    p1total = part_1(enginedata)
    p2total = part_2(enginedata)

    print(f"Part 1: {p1total}")
    print(f"Part 2: {p2total}")


if __name__ == '__main__':
    main()
