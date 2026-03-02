def fibionacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibionacci(n-1) + fibionacci(n-2)