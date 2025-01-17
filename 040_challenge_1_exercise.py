# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.
example_words = [
   'hello',
   'nonbiological',
   'Kay',
   'this-is-a-long-word',
   'antidisestablishmentarianism'
 ]


print("")
print("Function: report_long_words")

def report_long_words(words):
  non_hyphen_words = remove_words_with_hyphen(words)
  words_longer_than_nine = remove_short_words(non_hyphen_words)
  words_shortened_to_fifthteen_or_less = word_shortener(words_longer_than_nine)
  return (f"These words are quite long: {', '.join(words_shortened_to_fifthteen_or_less)}")

def remove_words_with_hyphen(words):
  non_hyphen_words = []
  for word in words:
    if "-" not in word:
      non_hyphen_words.append(word)
  return non_hyphen_words
  
  pass

def remove_short_words(non_hyphen_words):
  words_longer_than_nine =[]
  for word in non_hyphen_words:
    if len(word) >= 10:
      words_longer_than_nine.append(word)
  return words_longer_than_nine
  
  pass

def word_shortener(words_longer_than_nine):
  words_shortened_to_fifthteen_or_less = []
  for word in words_longer_than_nine:
    if len(word) >= 15:
      words_shortened_to_fifthteen_or_less.append((word[:15]) + "...")
    else:
      words_shortened_to_fifthteen_or_less.append(word)
  return words_shortened_to_fifthteen_or_less  
  
  pass
    
# My tests start

print("Function - remove words with hyphen")
print(remove_words_with_hyphen(example_words))

print("Function remove_short_words")
print(remove_short_words(example_words))

print("Function - word_shortener")
print(word_shortener(example_words))

# My tests end

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
