# lines of code

import csv
import sys

def main():  
    filepath = checkCli()
    try:
        count = 0
        with open(filepath, 'r') as file:
            for line in file:
                if not line.lstrip() or line.lstrip().startswith('#'):
                    continue
                else:
                    count += 1
        print(f'{count}')            
    except FileNotFoundError:
        sys.exit('File dose not exist')
def checkCli():
    
    if len(sys.argv) != 2:
        sys.exit('too many command-line argument') 
    if len(sys.argv[1]) == 0:
        sys.exit('too few command-line argument')
    if not  sys.argv[1].endswith('.py'):
        sys.exit('not a python file')
    else:
        return sys.argv[1]

main()