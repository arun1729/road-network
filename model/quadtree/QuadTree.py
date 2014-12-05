import numpy as np
from matplotlib import pyplot as plt
import globals 
import Util

DEBUG = False

class QuadTree:

    # init
    def __init__(self, data, mins, maxs, depth, nodeId):

        if DEBUG: print "node id: "+str(nodeId)
        self.mins=mins
        self.maxs=maxs
        self.depth=depth
        self.n_nodeId=nodeId
        # update node Index
        globals.nodeIndex[nodeId]=depth
        self.data = np.asarray(data)

        assert self.data.shape[1] == 2

        if mins is None:
            mins = data.min(0)
        if maxs is None:
            maxs = data.max(0)

        self.mins = np.asarray(mins)
        self.maxs = np.asarray(maxs)
        self.sizes = self.maxs - self.mins

        self.children = []

    def add_square(self):

        mids = 0.5 * (self.maxs + self.mins)
        if DEBUG: print self.data
        if DEBUG: print mids
        xmin, ymin = self.mins
        xmax, ymax = self.maxs
        xmid, ymid = mids

        sq_q1 = self.data[(self.data[:, 0] < mids[0]) & (self.data[:, 1] < mids[1])]
        sq_q2 = self.data[(self.data[:, 0] < mids[0]) & (self.data[:, 1] >= mids[1])]
        sq_q3 = self.data[(self.data[:, 0] >= mids[0]) & (self.data[:, 1] < mids[1])]
        sq_q4 = self.data[(self.data[:, 0] >= mids[0]) & (self.data[:, 1] >= mids[1])]

        if DEBUG: print "d1:" + str(sq_q1)
        if DEBUG: print "d2:" + str(sq_q2)
        if DEBUG: print "d3:" + str(sq_q3)
        if DEBUG: print "d4:" + str(sq_q4)

        if DEBUG: print "depth: "+str(self.depth)

        nodeId=0
        if not globals.nodeIndex:
            nodeid=0
        else:
            nodeId=max(globals.nodeIndex)

        if DEBUG: print "* nodeid: "+str(nodeId)
        if sq_q1.shape[0] > 0:
            nodeId=nodeId+1
            self.children.append(QuadTree(sq_q1, [xmin, ymin], [xmid, ymid],self.depth + 1, nodeId))
                
        if sq_q2.shape[0] > 0:
            nodeId=nodeId+1
            self.children.append(QuadTree(sq_q2,[xmin, ymid], [xmid, ymax],self.depth + 1, nodeId))
                              
        if sq_q3.shape[0] > 0:
            nodeId=nodeId+1
            self.children.append(QuadTree(sq_q3,[xmid, ymin], [xmax, ymid],self.depth + 1, nodeId))
                                
        if sq_q4.shape[0] > 0:
            nodeId=nodeId+1
            self.children.append(QuadTree(sq_q4,[xmid, ymid], [xmax, ymax],self.depth + 1, nodeId))

    
    def __hash__(self):
        return hash(self.n_nodeId)

    def __eq__(self, other):
        return (self.n_nodeId) == (other.n_nodeId)                           

    def draw_rectangle(self, ax, depth):
        if depth is None or depth == 0:
            print "square id: "+str(self.n_nodeId)
            print "min x,y: "+str(self.mins)
            print "sizes: "+str(self.sizes)
            box=Util.getCoordinates(self.mins,self.sizes)
            base_r_node=max(globals.edges)

            p1=base_r_node+1
            if tuple(box[0]) not in globals.coord_id:
                globals.coord_id[tuple(box[0])]=p1
            else:
                p1=globals.coord_id[tuple(box[0])]

            p2=base_r_node+2
            if tuple(box[1]) not in globals.coord_id:
                globals.coord_id[tuple(box[1])]=p2
            else:
                p2=globals.coord_id[tuple(box[1])]

            p3=base_r_node+3
            if tuple(box[2]) not in globals.coord_id:
                globals.coord_id[tuple(box[2])]=p3
            else:
                p3=globals.coord_id[tuple(box[2])]

            p4=base_r_node+4
            if tuple(box[3]) not in globals.coord_id:
                globals.coord_id[tuple(box[3])]=p4
            else:
                p4=globals.coord_id[tuple(box[3])]

            print "box p1: "+str(p1)+" - "+str(box[0])
            print "box p2: "+str(p2)+" - "+str(box[1])            
            print "box p3: "+str(p3)+" - "+str(box[2])
            print "box p4: "+str(p4)+" - "+str(box[3])

            globals.edges[p1]=[p2,p3] # 0 -> 1,2
            globals.edges[p2]=[p1,p4] # 1 -> 0,4
            globals.edges[p3]=[p1,p4] # 2 -> 1,4
            globals.edges[p4]=[p2,p3] # 4 -> 2,3

            print "--"
            rect = plt.Rectangle(self.mins, *self.sizes, zorder=2, ec='#000000', fc='none')
            ax.add_patch(rect)

        if depth is None or depth > 0:
            for child in self.children:
                child.draw_rectangle(ax, depth - 1)









