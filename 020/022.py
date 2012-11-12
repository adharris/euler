import csv

reader =  csv.reader(open('names.txt'))
names =  sorted(reader.next())

def value(name):
  return sum(map(lambda x: ord(x) - 64, name))

total = 0
for i in range(len(names)):
  total += (i + 1) * value(names[i])

print total
