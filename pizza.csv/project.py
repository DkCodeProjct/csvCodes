from tabulate import tabulate
import csv
import sys

def main():
    filePath = checkCli()
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        table_data = data[1:]
        print(tabulate(table_data, headers=headers,tablefmt='grid'))
        
    
def checkCli():
    
    if len(sys.argv) != 2:
        sys.exit('too many command-line argument') 
    if len(sys.argv[1]) == 0:
        sys.exit('too few command-line argument')
    if not  sys.argv[1].endswith('.csv'):
        sys.exit('NOT a CSV file')
    else:
        return sys.argv[1]
if __name__ == "__main__":
    main()