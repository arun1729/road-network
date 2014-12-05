
from matplotlib import pyplot as plt
from QuadTree import QuadTree
import Util
import globals
import numpy as np
from random import randrange

globals.init()  

# 2 D plane
size=1000 # if aquares are not fully forming increase plane size
X=Util.getPlane(size)

mins = (0.0, 0.0)
maxs = (size-1.0, size-1.0)

QT = QuadTree(X, mins, maxs, 0,0)

QT.add_square()

# Util.add_square_at(QT,3)

# for high density choose ones counter depth with highest number of squares randomly
while(True):
 	node=randrange(max(globals.nodeIndex))
	if len(globals.nodeIndex)>10: # limit network generation by number of nodes
		break

	Util.add_square_at(QT,node)

Util.printStats(globals.nodeIndex)
Util.bfs_print(QT)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.set_xlim(0, size-1.0)
ax.set_ylim(0, size-1.0)

# for each depth
for d in range(0,len(globals.nodeIndex)):
    QT.draw_rectangle(ax, depth=d)

for point in globals.edges:
	for edge in globals.edges[point]:
		print str(globals.coord_id[point])+" - "+str(globals.coord_id[edge]) +" - "+ str(point.distTo(edge))

plt.savefig('test.png')
#plt.show()

print "Done"

# Util.add_square_at(QT,5)
# Util.add_square_at(QT,6)
# Util.add_square_at(QT,9)
# Util.add_square_at(QT,10)




