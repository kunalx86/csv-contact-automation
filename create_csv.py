HEADER = 'Name, Given Name, Group Membership, Phone 1 - Type, Phone 1 - Value'

names = []
emails = []
numbers = []

def read(type):
  l = []
  with open(f"./{type}.txt", "r") as f:
    l = f.read()
  l = l.split(" ")
  return l

names = read("names")
numbers = read("phone_numbers")

for i in range(10):
  with open(f"contact{i}.csv", "w") as contact_csv:
    contact_csv.write(HEADER + "\n")
    for j in range(10):
      index = (i * 10) + j
      line = f"{names[index][8:]}, {names[index]}, * myContacts, Mobile, {numbers[index]}"
      contact_csv.write(line + '\n')