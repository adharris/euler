#! /usr/bin/env python

from collections import defaultdict
from math import sqrt, ceil

def getWords():
  f = open("words.txt", "rd.txt")
  for line in f.readlines():
    yield line.strip()
  f.close()

def getAnagrams(words):
  m = defaultdict(list)
  for word in words:
    sort = ''.join(sorted(word))
    for word2 in m[sort]:
      yield (word, word2)
    m[sort].append(word)

def getPowers(length):
  start = int(ceil(sqrt(10 ** (length - 1))))
  end = int(sqrt(10**length))
  for i in range(start, end):
    yield i**2


def replace(word1, word2, mask):
  mask = str(mask)
  word_map = dict()
  mask_map = dict()
  new_word1 = [0]*len(word1)
  new_word2 = [0]*len(word1)

  for i in range(len(mask)):
    this_letter = word1[i]
    this_mask = mask[i]
    if this_letter in word_map and word_map[this_letter] != this_mask:
      return ('0', '0')
    if this_mask in mask_map and mask_map[this_mask] != this_letter:
      return ('0', '0')
    mask_map[this_mask] = this_letter
    word_map[this_letter] = this_mask
    new_word1[i] = this_mask

  for i in range(len(word2)):
    new_word2[i] = word_map[word2[i]]

  return (''.join(new_word1), ''.join(new_word2))

def findPowersForAnagram(anagram):
  length = len(anagram[0])

  for power in getPowers(length):
    replaced = replace(anagram[0], anagram[1], power)
    if replaced[1][0] != '0' and isSquare(int(replaced[1])):
      yield (anagram, replaced)

def isSquare(i):
  return int(sqrt(i))**2 == i

def main():
  anagrams = getAnagrams(getWords())

  m = 0
  for anagram in anagrams:
    for power in findPowersForAnagram(anagram):
      t = int(max(power[1]))
      if t > m:
        print power
        m = t

if __name__ == '__main__':
  main();

