import csv

from faker import Faker

fake = Faker()

with open('users.csv', mode='w') as file:
    file_writer = csv.writer(
        file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['first_name', 'last_name', 'email', 'bio'])

    for _ in range(100):
        file_writer.writerow(
            [fake.first_name(), fake.last_name(), fake.email(), fake.text()])
