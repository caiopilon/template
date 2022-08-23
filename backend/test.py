class Circle:
   pi = 3.14
  
   def __init__(self, radius):
       self.radius = radius
  
   def circumference(self):
       return 2 * Circle.pi * self.radius
 
c1 = Circle(1)
c2 = Circle(1)
c1.pi = 4
print(f'{c1.circumference()} {c2.circumference()}')