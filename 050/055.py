def is_pal(n):
  s = str(n)
  for i in range(len(s)/2):
    if s[i] != s[len(s)-i-1]:
      return False
  return True

def rev(n):
  return int(''.join(reversed(str(n))))

def lychrel(n):
  i = 1
  while i < 51:
    n = n + rev(n)
    if is_pal(n):
      return i
    i += 1
  return None

limit = 10000
count = 0
for i in range(limit):
  if lychrel(i) is None:
    count += 1

print count
