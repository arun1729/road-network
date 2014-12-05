
#Test for point class

from Point import Point

p1=Point(20.0,30.0)
print p1

p2=Point(20.0,30.0)

print p1==p2

p3=Point(30.0,20.0)

print p1==p3

print p1.distTo(p3)

print p1.distTo(p2)
