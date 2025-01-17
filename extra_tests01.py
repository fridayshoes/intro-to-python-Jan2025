#
# Array Challenge
# 
# Have the function ArrayChallenge (strArr) take the array of strings stored in
# strArr, which will only contain two strings of equal length and return the 
# number of characters at each position that are different between them.

# For example: if strArr is ["house", "hours"] then your program should return 2. 
# The string will always be of equal length and will only contain lowercase
# characters from the alphabet and numbers.


# Examples

# Input: ["10011", "10100"]
# Output: 3

# Input: ["abcdef", "defabc"]
# Output: 6


example1 = ["10011", "10100"]
example2 = ["abcdef", "defabc"]



def ArrayChallenge(strArr):
  print(strArr[0])
  print(strArr[1])
  differences = 0
  for char1, char2 in zip(strArr[0], strArr[1]): # use zip to pair up the characters from both strings at index
    if char1 != char2: # if characters are not equal we increment the differences counter
      differences += 1

  print(differences)

  strArr = differences # line for cosmetic use (not needed)
    
  # code goes here
  return strArr



print("Example 1")
print(ArrayChallenge(example1))

print("Example 2")
print(ArrayChallenge(example2))



# keep this function call here
# print ArrayCahllenge(raw_input())

