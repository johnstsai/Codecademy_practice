#reverse
#Great work so far! Let's practice writing some functions that work with strings.
#1.Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".
#You may not use reversed or [::-1] to help you with this.

def reverse(text):
  rword = ""
  for char in text:
  	rword = char + rword
  return rword
print reverse("how are you?")