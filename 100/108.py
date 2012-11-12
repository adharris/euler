from collections import defaultdict

class Fraction:
  def __init__(self, denom):
    self.num = 1
    self.denom = denom
  def __str__(self):
    return "%d / %d" % (self.num, self.denom)
  def get_n(self, other):
    return (float(self.denom) * other.denom) / (self.denom + other.denom)
  def get_other(self, n):
    return Fraction(- (float(n) * self.denom) / (n - self.denom))
  def is_valid(self):
    return self.denom > 0 and self.denom == int(self.denom)

class N:
  def __init__(self, n):
    self.n = n
  def find_fractions(self):
    for d in range(self.n + 1, 2 * self.n + 1):
      f = Fraction(d)
      if f.get_other(self.n).is_valid():
        yield f, f.get_other(self.n)
  def count(self):
    return sum(1 for _ in self.find_fractions())


def generate_fractions(limit):
  d = defaultdict(int)
  i = 0
  while True:
    i += 1
    f1 = Fraction(i)
    for j in range(1, i+1):
      n = f1.get_n(Fraction(j))
      if n == int(n):
        # print "(1 / %d) + (1 / %d) = (1 / %d)" % (i, j, n)
        d[n] += 1
        if d[n] >= limit:
          return n

def main():
  print generate_fractions(100)

  # count = 0
  # for f1, f2 in n.find_fractions():
  #   count += 1
  #   print "%s + %s = 1 / %d" % (f1, f2, n.n)


if __name__ == '__main__':
  main()