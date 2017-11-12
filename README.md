# QuadTree Model for generating random road networks

![ScreenShot](/sample-network.png)

## QuadTree Model
Eisenstat introduces random road network generation using QuadTree data structure in [Eis10 ]. This project
implements that model in python and can be used to generate random road network of varying sizes.

## QuadTree implementation
The main component of the model is the Quadtree data structure. Quadtree is a tree data structure similar
to a binary tree with the difference that each node could have up to four children instead of two. In this
implementation each node either has four children or no children. The first node in the tree forms the initial
plane. Each node in the tree represents a square and its four children represent the division of the square
into four quadrants. Squares are added to the tree by recursively dividing squares into four quadrants.

## Road network and coordinate generation
Each node in the tree represents a square in a plane. For a given number n of nodes, the squares are randomly divided
into four quadrants, i.e. add four children to leaf nodes in the QuadTree. Each edge of the square forms
a road connecting two points. The Point class represents a point in the 2 dimensional
space. The Point class implements Python’s standard comparison, hash methods and also a method to
calculate euclidean distance to another point in the same plane. Once the desired number of squares are
generated, the tree is recursively traversed to generate Points based on the box formed
by the squares in the tree. From these Points a list of edges are generated and the euclidean
distance between them are calculated. Additionally, there are utility methods to perform Breadth First Search, add
nodes to specific nodes in the tree and print statistics. To visualize the generated road network there is
a utility to plot the network using Matplotlib

License: MIT License

[Eis10] David Eisenstat. “Random road networks: the quadtree model”. In: CoRR abs/1008.4916 (2010).
url: http://arxiv.org/abs/1008.4916.
