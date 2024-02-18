import csv
import sys
def main():
    cli = checkCli()
    cleanData = []
    
    try:
        filepath = sys.argv[1]
        
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file,quotechar='"')
            for row in reader:
                last, first = row['name'].strip().split(',')
                name = first, last, row['house']
                name1 = ' '.join(name[:2])
                lis =[name1,row['house']]
                cleanData.append(lis)

        with open(sys.argv[2] ,'w',newline='') as file:
            writer = csv.writer(file)
            headers = ['name', 'house']
            writer.writerow(headers)
            writer.writerows(cleanData)
    except FileNotFoundError:
        sys.exit('no such a file')

def checkCli():
    
    if len(sys.argv) != 3:
        sys.exit('too many command-line argument')

    if len(sys.argv[1]) == 0:
        sys.exit('too few command-line argument')
    
    if len(sys.argv[2]) == 0:
        sys.exit('too few command-line argument')
    
    if not  sys.argv[1].endswith('.csv'):
        sys.exit('Could not read invalid_file.csv')
    
    if not sys.argv[2].endswith('.csv'):
         sys.exit('Could not read invalid_file.csv')
    
    else:
        return sys.argv[1], sys.argv[2]
main()