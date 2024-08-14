# You will be given a number and you will need to return it as a string in Expanded Form

# Test Cases:
# 70304 -> '70000 + 300 + 4'
# 42 -> '40 + 2'
# 710163 -> '700000 + 10000 + 100 + 60 + 3'
# 853546 -> '800000 + 50000 + 3000 + 500 + 40 + 6'
# 511604 -> '500000 + 10000 + 1000 + 600 + 4'

def ragaca(number):
  string_num = str(number)
  string_len = len(string_num) - 1
  arr = []
  new_str = ""
  for i in string_num:
    arr.append(i)
    if i == "0":
      new_str += i
    else:
      new_str += i
  new_str += arr[0]
  new_str += "0" * string_len
  return new_str

print(ragaca(70304))