import re
from collections import defaultdict
from operator import itemgetter

def get_message(code):
  return ''.join(map(lambda x: chr(x), code))

def has_word(word, message):
  return not re.search(word, message, re.I) is None

def decode(message, key):
  m = []
  for i in range(len(message)):
    m.append( message[i] ^ key[i % len(key)])
  return m

  

f = open("cipher1.txt")
message = map(lambda x: int(x), f.readline().split(","))
dic = defaultdict(int)
for m in message:
  dic[m] += 1
print dic

print sorted(dic.iteritems(), key=itemgetter(1))

for i in range(ord('a'), ord('z') + 1):
  for j in range(ord('a'), ord('z') + 1):
    for k in range(ord('a'), ord('z') + 1):
      key = (i, j, k)
      m = get_message(decode(message, key))
      if  has_word('the', m) and has_word('and', m) and has_word('life', m):
        print map(lambda x: chr(x), key)
        print m
        print sum(map(lambda x: ord(x), m))


