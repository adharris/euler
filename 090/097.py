#! /usr/bin/env python

def last_n_mult(a, b, n):
  return (a * b) % (10**n)

def last_n_power(base, p, n):
  total = 1
  for i in range(p):
    total = last_n_mult(total, base, n)
  return total



print last_n_mult(last_n_power(2, 7830457, 10), 28433, 10) + 1