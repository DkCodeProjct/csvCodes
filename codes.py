import csv

def main():
    
    getPassword = input('password: ')
    
    if isValid(getPassword):
        
        getName = input('name: ')
        location = input('location: ')
        
        age = int(input('age: '))
        
        if age > 18:
            
            relationhship = input('relationship:[y/n] ').lower()
            
            if 'y' in relationhship:
                
                howLong = int(input('howLongTheRelationship: '))
            
            else:
                
                why = input("reasonForNotHaving: ")
                job = input('emplyeeOrNot: [y/n]').lower()
                if 'y' in job:
                    what = input("what'sTheJobRole: ")
                    salary = int(input('slary: '))
                
                else:
                    
                    why = input('reasonForNotHavingAjob: ')

                    with open('data.csv', mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([getPassword])

        else:
            print('NotAllowd...!')
            exit(0)
    else:
        print('invlaidPassword...!')

def isValid(string):
    if string[0].isalpha() == False or string[1].isalpha() == False:
        return False
    if len(string) < 2 or len(string) > 6:
        return False
    

    for s in string:
        if s in [' ', ',', '?', '.']:
            return False
    return True
if __name__ == "__main__":
    main()
