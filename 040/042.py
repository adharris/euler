import csv
from math import sqrt

def invert_tri(t):
  return (float(1) / 2) * ( sqrt(8 * t + 1) - 1)

def word_value(word):
  return sum([ord(c) - 64 for c in word])


words = csv.reader(open('042.txt'))
words = words.next()

def tri_words(words):
  for word in words:
    v = word_value(word)
    t = invert_tri(v)
    if t % 1 == 0:
      yield word

print len(list(tri_words(words)))
