import numpy as np
from matplotlib import pyplot as plt
import globals 
import Util

DEBUG = False
DEBUG2 = False

class QuadTree(object):

    def __init__(self, data, mins, maxs, depth, nodeId):

        if DEBUG: print "node id: "+str(nodeId)
        self.mins=mins
        self.maxs=maxs
        self.depth=depth
        self.n_node_id=nodeId
        # update node Index
        globals.node_index[nodeId]=depth
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
        if not globals.node_index:
            nodeId=0
        else:
            nodeId=max(globals.node_index)

        if DEBUG: print "* node id: "+str(nodeId)
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
        return hash(self.n_node_id)

    def __eq__(self, other):
        return (self.n_node_id) == (other.n_node_id)

    def draw_rectangle(self, ax, depth):
        if depth is None or depth == 0:
            if DEBUG2: print "square id: "+str(self.n_node_id)
            if DEBUG2: print "min x,y: "+str(self.mins)
            if DEBUG2: print "sizes: "+str(self.sizes)

            box=Util.getCoordinates(self.mins,self.sizes)
            if globals.coord_id:
                base_point_id=max(globals.coord_id.values())
            else:
                base_point_id=0

            p1_id=base_point_id+1
            if box[0] not in globals.coord_id:
                globals.coord_id[box[0]]=p1_id
            else:
                p1_id=globals.coord_id[box[0]]

            p2_id=base_point_id+2
            if box[1] not in globals.coord_id:
                globals.coord_id[box[1]]=p2_id
            else:
                p2_id=globals.coord_id[box[1]]

            p3_id=base_point_id+3
            if box[2] not in globals.coord_id:
                globals.coord_id[box[2]]=p3_id
            else:
                p3_id=globals.coord_id[box[2]]

            p4_id=base_point_id+4
            if box[3] not in globals.coord_id:
                globals.coord_id[box[3]]=p4_id
            else:
                p4_id=globals.coord_id[box[3]]

            if DEBUG2: print "box p1: "+str(p1_id)+" - "+str(box[0])
            if DEBUG2: print "box p2: "+str(p2_id)+" - "+str(box[1])            
            if DEBUG2: print "box p3: "+str(p3_id)+" - "+str(box[2])
            if DEBUG2: print "box p4: "+str(p4_id)+" - "+str(box[3])

            if box[0] in globals.edges:
                rm_list=[]
                for p in globals.edges[box[0]]:
                    if p.distTo(box[0]) > p.distTo(box[1]) or p.distTo(box[0]) > p.distTo(box[2]):
                        rm_list.append(p)
                
                for p in rm_list:
                    globals.edges[box[0]].remove(p)

                globals.edges[box[0]].update([box[1],box[2]]) 

            else:
                globals.edges[box[0]]=set([box[1],box[2]]) 

            if box[1] in globals.edges:
                rm_list=[]
                for p in globals.edges[box[1]]:
                    if p.distTo(box[1]) > p.distTo(box[0]) or p.distTo(box[1]) > p.distTo(box[3]):
                        rm_list.append(p)

                for p in rm_list:
                    globals.edges[box[1]].remove(p)

                globals.edges[box[1]].update([box[0],box[3]]) 

            else:
                globals.edges[box[1]]=set([box[0],box[3]]) 

            if box[2] in globals.edges:
                rm_list=[]
                for p in globals.edges[box[2]]:
                    if p.distTo(box[2]) > p.distTo(box[0]) or p.distTo(box[2]) > p.distTo(box[3]):
                        rm_list.append(p)
                
                for p in rm_list:
                    globals.edges[box[2]].remove(p)

                globals.edges[box[2]].update([box[0],box[3]])

            else:
                globals.edges[box[2]]=set([box[0],box[3]]) 

            if box[3] in globals.edges:
                rm_list=[]
                for p in globals.edges[box[3]]:
                    if p.distTo(box[3]) > p.distTo(box[1]) or p.distTo(box[3]) > p.distTo(box[2]):
                        rm_list.append(p)

                for p in rm_list:
                    globals.edges[box[3]].remove(p)

                globals.edges[box[3]].update([box[1],box[2]]) 

            else:
                globals.edges[box[3]]=set([box[1],box[2]]) 

            if DEBUG2: print "--"
            rect = plt.Rectangle(self.mins, *self.sizes, zorder=2, ec='#000000', fc='none')
            ax.add_patch(rect)

        if depth is None or depth > 0:
            for child in self.children:
                child.draw_rectangle(ax, depth - 1)