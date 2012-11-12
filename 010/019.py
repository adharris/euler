def is_sunday(day):
  return (day) % 7 == 0

def month_days(month, year):
  if month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
      return 29
    else:
      return 28
  elif month in (4,6,9,11):
    return 30
  else:
    return 31

day = 1
month = 1
year = 1900
sundays  = 0

to_year = 2000

while year <= to_year:
  if is_sunday(day):
    print (month, year)
    sundays += 1
  day += month_days(month, year)
  month = month % 12 + 1
  if month == 1:
    year = year +1

print sundays
