# Write a function with the rules:

# returns true  / True if every element in an array is an integer or a float with no decimals.
# returns true  / True if array is empty.
# returns false / False for every other input.


# Test cases:
# [] -> True
# [1, 2, 3, 4] -> True
# [1.0, 2.0, 3.0] -> True
# [1.0, 2.0, 3.0001] -> False
# ["-1"] -> False

def function_with_rules(arr):
  if not arr:
    return True
  for i in arr:
    if type(i) == int or type(i) == float:
      return True
    else:
      return False
    
print(function_with_rules([]))
print(function_with_rules([1,2,3,4]))
print(function_with_rules([1.0,2.0,3.0]))
print(function_with_rules([1.0,2.0,3.0001]))
print(function_with_rules(["-1"]))