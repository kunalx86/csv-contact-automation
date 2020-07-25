import csv

with open("./details.csv", "r") as f, open("phone_numbers.txt", "w") as w_f:
  csv_reader = csv.reader(f, delimiter=",")
  for row in csv_reader:
    contact_no = row[7]
    if len(contact_no) > 10:
      contact_no = contact_no[2:]
    w_f.write(contact_no + " ")
    print(contact_no)
