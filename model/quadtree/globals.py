# global variables

def init():
	# QuadTree Node
	global nodeIndex
	nodeIndex=dict()

	global edges
	edges=dict()
	edges[0]=set()

	# stores [Point] -> ID
	global coord_id
	coord_id=dict()
