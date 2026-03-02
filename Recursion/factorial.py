def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n-1)
print(fact(5)) 

## n* fact(n-1) will be evaluated as 5*fact(4) and then fact(4) will be evaluated as 4*fact(3) and so on until we reach the base case where n is 0. At that point, the function will return 1 and the results will be combined to give the final result of 120 for fact(5).