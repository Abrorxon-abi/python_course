import csv

from faker import Faker

fake = Faker()

with open('users.csv', mode='w') as file:
    file_writer = csv.writer(
        file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow([ 'first_name', 'last_name', 'email'])

    for _ in range(10):
        file_writer.writerow(
            [fake.first_name(), fake.last_name(), fake.email(), fake.text()])


with open('users.csv') as file:
    file_reader = csv.reader(
        file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for row in file:
        print(row)
