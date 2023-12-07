from tabulate import tabulate
import csv

name = input("enter Name: ")
age = input("enter Age: ")
mentalStructure = input("enter MentalStructure: ")

with open("student.csv",'a',newline=' ') as file:
    writer = csv.DictWriter(file, fieldnames=['name','age','mentalStructure'])
    writer.writerow({'name':name, 'age':age, 'mentalStructure':mentalStructure}).lstrip()