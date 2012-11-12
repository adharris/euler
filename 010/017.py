def to_words(n):
  s = ""
  hund = n / 100
  if hund > 0:
    s += "%shundred" % digit(hund) 

  if n % 100 != 0:
    if n > 100:
      s += "and"
    ten = n % 100
    s+= tens(ten)

  return s

def tens(n):
  special = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
      16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
  if n in special:
    return special[n]
  if n < 10:
    return digit(n)
  
  t = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}[n / 10]
  if n % 10 == 0:
    return t
  else:
    return "%s%s" % (t, digit(n % 10))

def digit(n):
  return {0: 'zero',
      1: 'one',
      2: 'two',
      3: 'three',
      4: 'four',
      5: 'five',
      6: 'six',
      7: 'seven',
      8: 'eight',
      9: 'nine'}[n]

count = 0
for i in range(1, 1000):
  print to_words(i)
  count += len(to_words(i))
 

print count + len('onethousand')
