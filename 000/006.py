one = 0
for i in range(1, 101):
  one += i * i
print one

two = 0
for i in range(1, 101):
  two = two + i
print two * two - one
