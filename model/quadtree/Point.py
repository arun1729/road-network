import numpy as np

class Point:

		def __init__(self,x,y):
		    self.x = x
		    self.y = y

		def distTo(self,x_to,y_to):
			a=numpy.array((self.x,self.y))
			a=numpy.array((x_to,y_to))
			dist = numpy.linalg.norm(a-b)
			return dist

		def __hash__(self):
			hashxy = 7
			hashxy = 71 * hashxy + self.x;
			hashxy = 71 * hashxy + self.y;
			return hashxy

		def __eq__(self, other):
			return (self.x,self.y) == (other.x,other.y) 

		def __str__(self):
			return "x: "+str(self.x)+" : "+" y: "+str(self.y)



