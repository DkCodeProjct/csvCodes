from tabulate import tabulate
import sys
import csv

#file name for make tabulate-grid
fileName = sys.argv[1]

#open file and read
with open(fileName,'r') as file:
    fileReader = csv.DictReader(file)
    fileData = list(fileReader)
    
    #make tabulate grid
    tabulatTable = tabulate(fileData, headers="keys", tablefmt="grids")
    print(tabulatTable)
