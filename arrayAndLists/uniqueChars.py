'''

convert string to array, and iterate over the array.

build a hashmap to while iterating, and check if the char has been used before

with O(1) look up time

run time complexity is O(n), linear

space time complexity is O(n), linear

'''

def hasUniqueChars(str):
  h = {}
  for char in str:
    if char not in h:
      h[char] = 1
    else:
      return False
  
  return True

# print(hasUniqueChars('abac'))
# print(hasUniqueChars('abc'))
# print(hasUniqueChars(''))

def hasUniqueCharsNoAdditionalDataStructures(str):
  startIndex = 0
  for i in range(0, len(str)):
    curChar = str[i]
    for j in range(startIndex + 1, len(str)):
      compChar = str[j]
      if curChar == compChar: return False
    startIndex += 1
  
  return True

# print(hasUniqueCharsNoAdditionalDataStructures('abcd'))
# print(hasUniqueCharsNoAdditionalDataStructures('abcda'))
# print(hasUniqueCharsNoAdditionalDataStructures(''))

'''

run time complexity O(n^2)
space time complexity O(1)

could also use two indexes, and two while loops

'''

def hasUniqueCharsNoAdditionalDataStructuresWhile(str):
  curIndex = 0

  while curIndex < len(str) - 1:
    curChar = str[curIndex]
    searchIndex = curIndex + 1

    while searchIndex < len(str):
      compChar = str[searchIndex]
      if curChar == compChar: return False

      searchIndex += 1
    curIndex += 1
  
  return True

# print(hasUniqueCharsNoAdditionalDataStructuresWhile('abc'))
# print(hasUniqueCharsNoAdditionalDataStructuresWhile('abca'))
# print(hasUniqueCharsNoAdditionalDataStructuresWhile('abcdefghijklmnopqrzy1245'))

'''

1) clever methods would be using a bit vector

2) sorting the array (n log(n) time and checking for neighboring values)

'''