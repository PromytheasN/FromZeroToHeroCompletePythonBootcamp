"""
bject Oriented Programming
Homework Assignment
Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
"""

import math

class Line:
    
    def __init__(self,coor1,coor2):
        
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
        
""" you can test this using this code: 

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.slope()
li.distance()
"""



#second problem/solution
#Making a class for a cylinder having 2 methods for 
#finding volume and surface_area

class Cylinder:
    
    p = 3.14
    
    def __init__(self,height=1,radius=1):
        
        self.height = height
        self.radius = radius
      
        
    def volume(self):
        
        return Cylinder.p*self.radius**2*self.height
    
    def surface_area(self):
        
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)

""" You can test this using this code:

c = Cylinder(2,3)
c.surface_area()
c.volume()
"""
    
