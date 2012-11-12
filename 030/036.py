def is_palindrome(s):
  for i in range(len(s) / 2):
    if s[i] != s[len(s) - i - 1]:
      return False
  return True

limit = 1000000
matches = []
for i in range(0, limit):
  if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
    matches.append(i)

print sum(matches)
