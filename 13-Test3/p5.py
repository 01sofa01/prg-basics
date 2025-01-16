class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    
    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y >0:
            return 2
        elif self.x <0 and self.y <0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
    
    def m2(self,a,b):
      f = 0
      if a == 0 or b == 0:
          f = 0
      elif a > 0 and b > 0:
          f = 1
      elif a <0 and b>0:
          f = 2
      elif a<0 and b<0:
          f=3
      elif a>0 and b<0:
          f=4
      if self.m1() == f:
        return True
      return False 
    def m3(self,a,b):
        if ((a - self.x)**2 + (b-self.y)**2) **0.5 > 5:
            return True
        return False 
point =C(5,3)
print(point.m1())
print(point.m2(7,8))
print(point.m3(5,5))
        
