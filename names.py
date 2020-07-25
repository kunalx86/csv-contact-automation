import csv

with open("./details.csv", "r") as f, open("./names.txt", "w") as w_f:
  csv_reader = csv.reader(f, delimiter=",")
  for row in csv_reader:
    name = 'GOOGLING' + row[3].replace(' ', '')
    print(name)
    w_f.write(name + " ")
