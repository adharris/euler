#! /usr/bin/env python

from math import log

class Exponent:
  def __init__(self, line, base, exp):
    self.line = line
    self.base = base
    self.exp = exp
  def __str__(self):
    return "%d^%d (line %d)" % (self.base, self.exp, self.line)
  def isGreaterThan(self, other):
    return self.exp * log(self.base) > other.exp * log(other.base)

def getExponents(filename):
  f = open(filename)
  for i,line in enumerate(f.readlines()):
    parts = line.strip().split(',');
    yield Exponent(i, int(parts[0]), int(parts[1]))


def main():
  exponents = getExponents('base_exp.txt')
  largest = exponents.next()
  for i,exponent in enumerate(exponents):
    if exponent.isGreaterThan(largest):
      largest = exponent
  print largest


if __name__ == '__main__':
  main();