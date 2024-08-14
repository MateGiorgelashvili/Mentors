# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Test Cases:
# 'Pig latin is cool' -> 'igPay atinlay siay oolcay'
# 'This is my string' -> 'hisTay siay ymay tringsay'
# "Ultima necat" -> 'ltimaUay ecatnay'
# "Lux in tenebris lucet" -> 'uxLay niay enebristay ucetlay'
# "Cucullus non facit monachum" -> 'ucullusCay onnay acitfay onachummay'
def latin(word):
  new_word = word.split()
  newarr = []
  for i in new_word:
    newarr.append(i[1:] + i[0] + "ay")
  result = ' '.join(newarr)
  return result

print(latin("Pig latin is cool"))
print(latin("This is my string"))
print(latin("Ultima necat"))
print(latin("Lux in tenebris lucet"))
print(latin("Cucullus non facit monachum"))
