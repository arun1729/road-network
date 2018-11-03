# global variables

def init():
	# QuadTree Node
	global node_index
	node_index=dict()

	global edges
	edges=dict()
	edges[0]=set()

	# stores [Point] -> ID
	global coord_id
	coord_id=dict()
