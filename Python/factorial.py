#factorial
#All right! Now we're cooking. Let's try a factorial problem.
#To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example:
#factorial(4) would equal 4 * 3 * 2 * 1, which is 24.

#1.Define a function factorial that takes an integer x as input.
#Calculate and return the factorial of that number.

def factorial(x):
  total = 1
  while x > 0:
    total *= x
    x -= 1
  return total
print factorial(3)