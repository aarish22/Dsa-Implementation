## The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, and so on. The Fibonacci sequence can be defined recursively as follows:

def fibionacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibionacci(n-1) + fibionacci(n-2)