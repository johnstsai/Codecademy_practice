#anti_vowel
#Nice work. Next up: vowels!
#Instructions
#1.Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
#For example: anti_vowel("Hey You!") should return "Hy Y!". Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.

def anti_vowel(text):
  string = ""
  for char in text:
    if char not in "aeiouAEIOU":
      string += char
  return string
print anti_vowel("who are you?")