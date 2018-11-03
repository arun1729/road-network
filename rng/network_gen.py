
from matplotlib import pyplot as plt
from QuadTree import QuadTree
import Util
import globals
import numpy as np
from random import randrange
import os

globals.init()

# 2 D plane
size=10 # if squares are not fully forming increase plane size
X=Util.getPlane(size)

mins = (0.0, 0.0)
maxs = (size-1.0, size-1.0)

QT = QuadTree(X, mins, maxs, 0,0)

QT.add_square()

print "Generating road network..."
# for high density choose ones counter depth with highest number of squares randomly
while(True):
 	node=randrange(max(globals.node_index))
	if len(globals.node_index)>800: # limit network generation by number of nodes
		break

	Util.add_square_at(QT,node)

Util.printStats(globals.node_index)
#Util.bfs_print(QT)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.set_xlim(0, size-1.0)
ax.set_ylim(0, size-1.0)

# for each depth generate squares
print "generating squares..."
for d in range(0,len(globals.node_index)):
    QT.draw_rectangle(ax, depth=d)

print "writing data to files..."
fn = open('node-list','w')
fe = open('edge-list','w')

edgeCount=0 #directed edge count
for point in globals.edges:
	if point in globals.coord_id:
		fn.write(str(globals.coord_id[point])+","+str(point.x)+","+str(point.y)+"\n")

	for edge in globals.edges[point]:
		fe.write(str(globals.coord_id[point])+","+str(globals.coord_id[edge])+"\n")
		edgeCount=edgeCount+1

fn.close()
fe.close()

print "# of edges: "+str(edgeCount)

plt.savefig('../rand-quad-road-network.png')

dir_path = os.path.dirname(os.path.realpath(__file__))

print "generate road network image at: "+ dir_path + "/rand-quad-road-network.png"

print "Done"





