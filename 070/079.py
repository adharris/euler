
def validate_key(string, key):
  for s in str(string):
    if s == key[0]:
      key = key[1:]
      if len(key) == 0:
        return True
  return False

def validate_keys(string, keys):
  for key in keys:
    if not validate_key(string, key):
      return False
  return True

def find_shortest(keys):
  i = 0
  while True:
    i += 1
    if validate_keys(str(i), keys):
      return i
    if i % 100000 == 0: print i


keys = [str(int(s)) for s in file('keylog.txt')]
print find_shortest(keys)

