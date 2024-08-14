# Determine if a walk (given as an array of directions) takes exactly 10 minutes 
# and returns you to the starting point.

# Args:
# walk (list of str): List of one-letter direction strings ('n', 's', 'e', 'w').
# Each direction takes 1 minute (so list with length of 10 elements takes 10 minutes)

# Returns:
# bool: True if the walk is exactly 10 minutes and returns to start, False otherwise.

# Test Cases:
# ['w','e','w','e','w','e','w','e','w','e','w','e'] -> False
# ['n','s','n','s','n','s','n','s','n','s'] -> True
# ['n','n','n','s','n','s','n','s','n','s'] -> False
# ['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] -> False
# ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] -> True



def siaruli(walk):
  if len(walk) != 10:
    return False
  
  start_position = 0
  
  for i in walk:
    if i == "n":
      start_position -= 1
    elif i == "s":
      start_position += 1
    elif i == "e":
      start_position -= 1
    elif i == "w":
      start_position += 1

  return start_position == 0
    
print(siaruli(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(siaruli(['n','s','n','s','n','s','n','s','n','s']))
print(siaruli(['n','n','n','s','n','s','n','s','n','s']))
print(siaruli(['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']))
print(siaruli(['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']))