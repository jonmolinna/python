# File Handling
import csv
import json
import os

txt_file = open('./my_file.txt', 'r+')
# print(txt_file.read())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta JavaScript")

txt_file.close()

# File Json

json_file = open('./my_file.json', 'w+')

json_test = {
    "name": "Kendra",
    "surname": 'Contreras',
    "age": 27,
    "language": ["Python", "React", "Php"],
    "website": "dallase.com"
}

json.dump(json_test, json_file, indent=3)
json_file.close()

with open('./my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open('./my_file.json'))
print(json_dict)

# .csv file
csv_file = open('./my_file.csv', 'w+')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'surname', 'age'])
csv_writer.writerow(['Kendra', 'Contreras', 27])

csv_file.close()

with open('./my_file.csv') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx
# .xml file
