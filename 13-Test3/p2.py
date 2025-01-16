def f(x,y,d):
  for i in range(x,y+1):
     if int(d) == i:
      return True
  return False


print(f(10,15,"14"))
