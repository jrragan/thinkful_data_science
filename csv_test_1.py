__author__ = 'rragan'

import csv

with open('lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print line
