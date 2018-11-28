[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# QuadTree Model for generating random road networks

## Generate a sample road network

- clone repo and then run the following
```
cd road-network/rng
python network_gen.py <plane size> <number of nodes>
```

## output
```
Generating road network...
*** Tree Stats ***
...
generating squares...
writing data to files...
# of edges: 1099
generate road network image at: /path/to/your/dir/road-network/rand-quad-road-network.png
node list at: /path/to/your/dir/road-network/node-list
edge list at: /path/to/your/dir/road-network/edge-list
Done
```

# About the model

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

This image from Wikipedia shows how an image is represented using a QuadTree:
![quadImage](https://upload.wikimedia.org/wikipedia/commons/a/a0/Quad_tree_bitmap.svg)

[QuadTree Wikipedia](https://en.wikipedia.org/wiki/Quadtree)

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

[![a](https://ga-beacon.appspot.com/UA-130066281-1/road-network?pixel)](https://github.com/arun1729/road-network)
