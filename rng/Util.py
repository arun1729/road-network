import numpy as np
from Queue import Queue
import itertools, random
from Point import Point

def getPlane(size):
    X=[]
    plane=range(0,size)
    for i in itertools.permutations(plane,2):
        X.append(i)

    for i in plane:
        X.append((i,i))

    X=np.array(X)

    return X

def bfs_print(root):
    print "*** bfs print ***"
    q = Queue()
    s_node=root
    q.put(s_node)
    seen_list = []

    while(not q.empty()):
        node=q.get() # removes
        print node.n_node_id
        if(node not in seen_list):
            seen_list.append(node)
        for child in node.children:
            if(child not in seen_list):
                q.put(child)
    print "---------------"

def add_square_at(root,nodeid):
    q = Queue()
    s_node=root
    q.put(s_node)
    seen_list = []

    while(not q.empty()):
        node=q.get() # removes
        if nodeid==node.n_node_id:
            node.add_square()
        else:
            if(node not in seen_list):
                seen_list.append(node)
            for child in node.children:
                if(child not in seen_list):
                    q.put(child)

def printStats(nodeIndex):
    print "*** Tree Stats ***"
    print nodeIndex

def getCoordinates(baseXY,boxSize):
	p1=Point(baseXY[0],baseXY[1])
	p2=Point(baseXY[0]+boxSize[0],baseXY[1])
	p3=Point(baseXY[0],baseXY[1]+boxSize[1])
	p4=Point(p2.x,p2.y+boxSize[1])
	
	return (p1,p2,p3,p4)
	

def getBetaInt(alpha,beta,m,maxv):
    beta=int(np.random.beta(alpha,beta,1)[0]*m)
    while(beta>maxv):
        print beta
        beta=int(np.random.beta(alpha,beta,1)[0]*m)

    return beta








