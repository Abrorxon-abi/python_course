import csv


def scv_reader(file):
    with open(file.strip()) as scv_file:
        data = csv.reader(scv_file, quotechar='|')
        for row in data:
            print(row)


scv_reader('users.csv')

# ---------------------------------------------------

def scv_reader(file):
    with open(file.strip()) as scv_file:
        data = csv.reader(scv_file, delimiter='\t')
        for row in data:
            print(''.join(row))


scv_reader('users.csv')

# ---------------------------------------------------

def scv_reader(file):
    with open(file.strip()) as scv_file:
        data = csv.reader(scv_file)
        print(list(data))

scv_reader('users.csv')



