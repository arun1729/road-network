import numpy as np

class Point:

		def __init__(self,x,y):
			self.x = x
			self.y = y
			self.pointID=""

		def distTo(self,point):
			a=np.array((self.x,self.y))
			b=np.array((point.x,point.y))
			dist = np.linalg.norm(a-b)
			return dist

		def setID(self,ID):
			self.pointID=ID

		def getID():
			return self.pointID

		def __hash__(self):
			hashxy = 7
			hashxy = 71 * hashxy + self.x
			hashxy = 71 * hashxy + self.y
			return int(hashxy)

		def __eq__(self, other):
			return (self.x,self.y) == (other.x,other.y) 

		def __str__(self):
			return "x: "+str(self.x)+" : "+" y: "+str(self.y)



