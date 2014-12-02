# utils Quadtree
import numpy as np
from collections import Counter
from Queue import Queue
from matplotlib import pyplot as plt
import itertools, random

def getPlane(size):
    X=[]
    plane=range(0,size)
    for i in itertools.permutations(plane,2):
        X.append(i)

    for i in plane:
        X.append((i,i))

    X=np.array(X)

    return X

# util
def bfs_print(root):
    print "*** bfs print ***"
    q = Queue()
    s_node=root
    q.put(s_node)
    seen_list = []

    while(not q.empty()):
        node=q.get() # removes
        print node.n_nodeId
        if(node not in seen_list):
            seen_list.append(node)
        for child in node.children:
            if(child not in seen_list):
                q.put(child)
    print "---------------"

# util
def add_square_at(root,nodeid):
    q = Queue()
    s_node=root
    q.put(s_node)
    seen_list = []

    while(not q.empty()):
        node=q.get() # removes
        if nodeid==node.n_nodeId:
            node.add_square()
        else:
            if(node not in seen_list):
                seen_list.append(node)
            for child in node.children:
                if(child not in seen_list):
                    q.put(child)

# util
def printStats(nodeIndex):
    print "*** Tree Stats ***"
    print nodeIndex
    dn=Counter(nodeIndex.values())
    print "depth node count:"
    for depth in dn:
        print " - "+str(depth)+" : "+str(dn[depth])
