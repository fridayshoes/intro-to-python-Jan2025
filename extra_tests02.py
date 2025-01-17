
# String Challenge

# Have the function StringChallenge (str) take the str parameter being passed and return the
# string in reversed order. For example: if the input
# string is "Hello World and Coders" then your program should return the string sredoC dna dlrow olleH.

# Examples

# Input: "coderbyte"
# Output: etybredoc

# Input: "I Love Code"
# Output: edoc evoL I


example1 = "coderbyte"
example2 = "I Love Code"


def StringChallenge(strParam):
  # code goes here
  return strParam[::-1]


# Test1

print("Example 1 test")
print(StringChallenge(example1))

print("Example 2 test")
print(StringChallenge(example2))



# keep this function call here
# print StringChallenge (raw_input())
