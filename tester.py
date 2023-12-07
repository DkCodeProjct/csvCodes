from tabulate import tabulate
import csv

#collect data //
name = input("enter_Name: ")
age = input("enter_Age: ")
civilStatus = input("enter_civilStatus: ")
psychicStructrue = input("enter:_pyschicStructure: ")
sexuality = input("enter_Sexuality: ")

#make a dict //
psychicData = {

    "name" : name, 
    "age" : age, 
    "civilStatus" : civilStatus,
    "psychicStructrue" : psychicStructrue,
    "sexuality" : sexuality

}

#specifie csv file and open as append //
with open("student.csv",'a') as file:
    writer = csv.DictWriter(file, fieldnames=['name','age','civilStatus','psychicStructrue','sexuality'])
    writer.writerow(psychicData)

#make tabulate grid table //
tabulateGridDataFormat = tabulate([psychicData], headers='keys',tablefmt='grid')

print(tabulateGridDataFormat)