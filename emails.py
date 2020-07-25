import csv

with open("./details.csv", "r") as f, open("emails.txt", "w") as w_f:
  csv_reader = csv.reader(f, delimiter=",")
  for row in csv_reader:
    w_f.write(row[2] + " ")
    print(row[2])
