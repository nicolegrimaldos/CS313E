#  File: Graph.py

#  Description: Using Graphs, adjMatrix, deleting vertices and edges, etc.

#  Student Name: Nicole Grimaldos

#  Student UT EID: ng23476

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 4/30/21

#  Date Last Modified: 5/1/21

import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))

    def peek(self):
        return self.queue[0]


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return True
        return False

    # get the index from the vertex label
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return i
        return -1

    # add a Vertex object with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        fromIndex = self.get_index(fromVertexLabel)
        toIndex = self.get_index(toVertexLabel)
        weight = self.adjMat[fromIndex][toIndex]
        if weight != 0:
            return weight
        return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors(self, vertexLabel):
        neighbors = []
        idx = self.get_index(vertexLabel)
        length = len(self.Vertices[idx])
        for i in range(length):
            if self.Vertices[idx][i] != 0:
                neighbors.append(self.Vertices[idx][i])
        return neighbors

    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices(self):
        for i in range(len(self.Vertices)):
            print(self.Vertices[i])

    # do a depth first search in a graph starting at vertex v (index)
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while not theStack.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if u == -1:
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs(self, v):
        theQueue = Queue()

        theQueue.enqueue(v)
        (self.Vertices[v]).visited = True
        # print(self.Vertices[v])
        print(self.Vertices[v])

        while not theQueue.is_empty():
            u = self.get_adj_unvisited_vertex(theQueue.peek())
            if u == -1:
                u = theQueue.dequeue()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theQueue.enqueue(u)

        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        start = self.get_index(fromVertexLabel)
        finish = self.get_index(toVertexLabel)
        self.adjMat[start][finish] = 0
        self.adjMat[finish][start] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):
        vertexIndex = self.get_index(vertexLabel)
        del (self.Vertices[vertexIndex])
        del (self.adjMat[vertexIndex])
        for i in range(len(self.Vertices)):
            del (self.adjMat[i][vertexIndex])

    # get length
    def get_length(self):
        num = 0
        for i in range(len(self.Vertices)):
            num += 1
        return num


def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_vertex(city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # do the depth first search
    print("Depth First Search")
    cities.dfs(start_index)
    print()
    #
    # print("/n Ajacency Matrix")
    # for i in range (num_vertices):
    #     for j in range(num_vertices):
    #         print(cities.adjMat[i][j], end = " ")
    #     print()
    # print()
    # test depth first search

    # test breadth first search
    print("Breadth First Search")
    cities.bfs(start_index)
    print()

    # test deletion of an edge
    print("Deletion of an edge")
    edges = sys.stdin.readline().strip().split()
    start = edges[0]
    finish = edges[1]
    cities.delete_edge(start, finish)

    print("\nAdjacency Matrix")
    for i in range(num_vertices):
        for j in range(num_vertices):
            if j != num_vertices - 1:
                print(cities.adjMat[i][j], end=" ")
            else:
                print(cities.adjMat[i][j], end="")
        print()
    print()

    # test deletion of a vertex
    print("Deletion of a vertex")
    print()
    print("List of Vertices")
    to_delete = sys.stdin.readline().strip()
    cities.delete_vertex(to_delete)

    cities.get_vertices()

    print("\nAdjacency Matrix")
    numVert = cities.get_length()
    for i in range(numVert):
        for j in range(numVert):
            if j != numVert - 1:
                print(cities.adjMat[i][j], end=" ")
            else:
                print(cities.adjMat[i][j], end="")
        print()
    print()


if __name__ == "__main__":
    main()

# Depth First- Going along a branch until you cant go any further
# then backtrack to a fork and go along another branch until you cant go further
