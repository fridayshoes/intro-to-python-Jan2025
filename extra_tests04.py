

# String Challenge

# Have the function StringChallenge (str) take
# the str string parameter being passed and return the number of consonants the string contains.

# Examples

# Input: "Hello World"
# Output: 7

# Input: "Alphabets"
# Output: 6


example1 = "Hello World"
example2 = "Alphabets"





def StringChallenge(strParam):
  vowels = 0
  consonants = 0  
  for char in strParam:
    if char.lower() in "aeiou":
      vowels += 1
    elif char.isalpha(): # checks anything that isn't a vowel is an alphbetical character 
      consonants += 1
  print(vowels) # Testing
  print(consonants) # Testing
  strParam = consonants # A line to ensure we finish on strParam (just for aesthetics)
  # code goes here
  return strParam





print("Example 1")
print(StringChallenge(example1))


print("Example 2")
print(StringChallenge(example2))








# keep this function call here
# print StringChallenge (raw_input())
