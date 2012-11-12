def dumb_cancel(num, denom):
  actual_value = float(num) / denom
  if actual_value >= 1:
    return False
  if num % 10 == 0 and denom % 10 == 0:
    return False
  for i in str(num):
    new_num = str(num).replace(i,'')
    new_denom = str(denom).replace(i,'')
    if new_num != '' and new_denom != '' and int(new_denom) != 0 and float(new_num) / int(new_denom) == actual_value:
      return True
  return False

num_max = 100
denom_max = 100

fractions = []
for i in range(10, num_max):
  for j in range(10, denom_max):
    if dumb_cancel(i, j):
      fractions.append((i, j))

mult = [1, 1]
for fract in fractions:
  mult[0] *= fract[0]
  mult[1] *= fract[1]
print mult
