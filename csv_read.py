import csv

with open('users.csv', mode='r') as file:
    file_reader = csv.reader(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for row in file:
        print(row)