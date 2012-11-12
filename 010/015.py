from math import factorial
def set_bits(n):
  n = n - ((n >> 1) & 0x55555555)
  n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
  return (((n + (n >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24

grid_size = 20
all_down = 2**grid_size -1
all_right = (2**grid_size - 1) * 2**grid_size

index = all_down
valid  = 0
#while index <= all_right:
#  if set_bits(index) == grid_size:
#    print bin(index)
#    valid = valid + 1
#  index = index + 1

print factorial(grid_size * 2) / (factorial(grid_size)**2)
print valid
