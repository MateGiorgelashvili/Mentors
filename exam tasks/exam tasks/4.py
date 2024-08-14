# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Test Cases:
# [2, 4, 0, 100, 4, 11, 2602, 36] ->  11
# [160, 3, 1719, 19, 11, 13, -21] -> 160
# [7516484, 526386, 1637037, 813302, -8496994, 812820, 3797630, -3773758, 921354, 6123650, 1693668] -> 1637037
# [8811272, 9218790, 9094178, -818772, 2711934, -3905606, 1332109] -> 1332109
# [-4207752, 362590, 5205484, 11340, 3740336, 1360605] -> 1360605

def find_mol(arr):
  even_count = []
  odd_count = []
  for i in arr:
    if i % 2 == 0:
      even_count.append(str(i))
    if i % 2 == 1:
      odd_count.append(str(i))
  if len(even_count) > len(odd_count):
    return int("".join(odd_count))
  if len(even_count) < len(odd_count):
    return int("".join(even_count))

print(find_mol([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_mol([160, 3, 1719, 19, 11, 13, -21]))
print(find_mol([7516484, 526386, 1637037, 813302, -8496994, 812820, 3797630, -3773758, 921354, 6123650, 1693668]))
print(find_mol([8811272, 9218790, 9094178, -818772, 2711934, -3905606, 1332109]))
print(find_mol([-4207752, 362590, 5205484, 11340, 3740336, 1360605]))