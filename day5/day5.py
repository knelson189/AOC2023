#!/usr/bin/env python3

import os
import re
import sys

REGEX_DIGITS = re.compile(r'\d+')

SEEDS = {}

def parse_file(inputfile):
    mapping = {}
    destorder = []
    with open(inputfile) as file:
        for eachLine in file:
            eachLine = eachLine.rstrip()
            if 'seeds:' in eachLine:
                for eachSeed in re.findall(REGEX_DIGITS, eachLine):
                    SEEDS[int(eachSeed)] = {}
            # Not in map mode
            elif len(eachLine) == 0:
                destinationkey = None
                sourcekey = None
            elif 'map:' in eachLine:
                sourcekey = re.search(r'(.*?)-to', eachLine)[1]
                destinationkey = re.search(r'to-(.*?) ', eachLine)[1]
                destorder.append(destinationkey)
                mapping[destinationkey] = {
                    'source': sourcekey,
                    'ranges': []
                }
            else:
                allnums = re.findall(REGEX_DIGITS, eachLine)
                mapping[destinationkey]['ranges'].append([int(eachNum) for eachNum in allnums])
    return mapping, destorder

def parse_file_p2(inputfile):
    mapping = {}
    destorder = []
    seeds = []
    with open(inputfile) as file:
        for eachLine in file:
            eachLine = eachLine.rstrip()
            if 'seeds:' in eachLine:
                allnums = [int(eachNum) for eachNum in re.findall(REGEX_DIGITS, eachLine)]
                for i in range(0,len(allnums),2):
                    for j in range(allnums[i],allnums[i+1]+1):
                        seeds.append(j)
            # Not in map mode
            elif len(eachLine) == 0:
                destinationkey = None
                sourcekey = None
            elif 'map:' in eachLine:
                sourcekey = re.search(r'(.*?)-to', eachLine)[1]
                destinationkey = re.search(r'to-(.*?) ', eachLine)[1]
                destorder.append(destinationkey)
                mapping[destinationkey] = {
                    'source': sourcekey,
                    'ranges': []
                }
            else:
                allnums = re.findall(REGEX_DIGITS, eachLine)
                mapping[destinationkey]['ranges'].append([int(eachNum) for eachNum in allnums])
    return seeds, mapping, destorder     

def part_1(mapping,destorder):
    for eachSeed in SEEDS.keys():
        for eachDest in destorder:
            sourcekey = mapping[eachDest]['source']
            if sourcekey != 'seed':
                mappingid = SEEDS[eachSeed][sourcekey]
            else:
                mappingid = eachSeed
            
            # if it can't find any ranges default to what the default is
            SEEDS[eachSeed][eachDest] = mappingid
            for eachRangeSet in mapping[eachDest]['ranges']:
                destidstart, sourceidstart, rangenum = eachRangeSet
                if mappingid in range(sourceidstart, sourceidstart+rangenum):
                    SEEDS[eachSeed][eachDest] = (destidstart + (mappingid - sourceidstart))
                    break
    locationid = None
    for eachSeed in SEEDS.keys():
        if locationid == None:
            locationid = SEEDS[eachSeed]['location']
        elif SEEDS[eachSeed]['location'] < locationid:
            locationid = SEEDS[eachSeed]['location']
    return locationid

def part_2(seeds, mapping,destorder):
    localid = 1
    while localid > 0:
        for eachDest in destorder[::-1]:
            if eachDest == 'location':
                mappingid = localid
            elif eachDest == 'seed':
                if mappingid in seeds:
                    return localid
                else:
                    localid += 1
            else:
                for eachRangeSet in mapping[eachDest]['ranges']:
                    destidstart, sourceidstart, rangenum = eachRangeSet
                    if mappingid in range(destidstart, destidstart+rangenum):
                        mappingid = (sourceidstart + mappingid-destidstart)
                        break





def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments.")

    inputfile = sys.argv[1]

    if not os.path.exists(inputfile):
        sys.exit(f"{inputfile} does not exist.")
    
    mapping, destorder = parse_file(inputfile)
    locationid = part_1(mapping, destorder)
    print(f"Part 1: {locationid}")
    seeds, mapping, destorder = parse_file_p2(inputfile)
    destorder.insert(0, 'seed')
    locationid_p2 = part_2(seeds, mapping, destorder)
    print(f"Part 2: {locationid_p2}")


if __name__ == '__main__':
    main()
