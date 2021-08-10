#  File: TopoSort.py

#  Description: Finding if a graph has a cycle and then doing TopoSort

#  Student Name: Nicole Grimaldos

#  Student UT EID: ng23476

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 5/3/21

#  Date Last Modified: 5/12/21

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

    def in_stack(self, v):
        return v in self.stack

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
        self.inpath = False

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

        start = self.get_index(start)
        finish = self.get_index(finish)
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
    def get_adj_unvisited_vertex(self, v, theStack):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
            if (self.adjMat[v][i] > 0) and ((self.Vertices[i]).was_visited()):
                if theStack.in_stack(i):
                    return 0
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices(self):
        for i in range(len(self.Vertices)):
            print(self.Vertices[i])

    # do a depth first search in a graph starting at vertex v (index)
    def dfs(self):
        nVert = len(self.Vertices)
        for v in range(nVert):
            # create the Stack
            theStack = Stack()
            bucket = []
            # mark the vertex v as visited and push it on the Stack
            (self.Vertices[v]).visited = True
            theStack.push(v)

            # visit all the other vertices according to depth
            while not theStack.is_empty():
                # get an adjacent unvisited vertex
                u = self.get_adj_unvisited_vertex(theStack.peek(), theStack)
                if u == 0:
                    if theStack.in_stack(u):
                        return True
                elif u == -1:
                    u = theStack.pop()
                else:
                    (self.Vertices[u]).visited = True
                    theStack.push(u)
                    bucket.append(u)

            # the stack is empty, let us rest the flags
            nVert = len(self.Vertices)
            for i in range(nVert):
                (self.Vertices[i]).visited = False
        return False

    def in_degree(self, vertex):
        degree = 0
        for row in range(len(self.Vertices)):
            degree += self.adjMat[row][self.get_index(vertex.get_label())]
        return degree

        # get the index from the vertex label
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return i
        return -1

    def topo_helper(self):
        in_degree = [0] * len(self.Vertices)

        for i in self.adjMat:
            for x in i:
                #print(i)
                for j in self.adjMat[x]:
                    in_degree[j] += 1

        queue = []
        for i in range(len(self.Vertices)):
            if in_degree[i] == 0:
                queue.append(i)

        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:

            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            top_order.append(self.Vertices[u].get_label())

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.adjMat[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)


        return top_order
    # theQueue = Queue()
        # nVert = len(self.Vertices)
        # while nVert > 0:
        #     list = []
        #     for i in range(nVert):
        #         if (self.in_degree(self.Vertices[i])) != 0:
        #             list.append(self.Vertices[i].get_label())
        #     for i in range(len(list) - 1):
        #         theQueue.enqueue(list[i])
        #         self.delete_vertex(list[i])
        # new_list = []
        # while not theQueue.is_empty():
        #     new_list.append(theQueue.dequeue())
        # return new_list

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

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):
        return self.dfs()

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        return self.toposort_helperr()

    def toposort_helperr(self):
        zero_list = []
        vertList = []
        in_zero = True
        col = 0
        length = (len(self.Vertices))
        while len(vertList) != length:

            for row in range(len(self.adjMat)):
                for i in range(len(self.adjMat)):
                    if self.adjMat[i][col] != 0:
                        in_zero = False
                if in_zero:
                    # print("Ooo",str(self.Vertices[col]))
                    zero_list.append(str(self.Vertices[col]))
                    vertList.append(str(self.Vertices[col]))
                zero_list.sort()
                col += 1
                in_zero = True

            for i in zero_list:
                self.delete_vertex(i)
            zero_list = []
            col = 0
        return vertList





def main():
    # create a Graph object
    theGraph = Graph()

    # read the number of vertices
    line = (sys.stdin.readline()).strip()
    num_vertices = int(line)
    # print(num_vertices)

    # add the vertices to the graph
    for i in range(num_vertices):
        city = (sys.stdin.readline()).strip()
        # print(city)
        theGraph.add_vertex(city)

    # read the number of edges
    line = (sys.stdin.readline()).strip()
    num_edges = int(line)

    # read the edges and add them to the adjacency matrix
    for i in range(num_edges):
        line = (sys.stdin.readline()).strip()
        # print(line)
        edge = line.split()
        start = (edge[0])
        finish = (edge[1])
        weight = 1
        theGraph.add_directed_edge(start, finish, weight)

    #print the adjacency matrix
    # print("\nAdjacency Matrix")
    # for i in range(num_vertices):
    #     for j in range(num_vertices):
    #         print(theGraph.adjMat[i][j], end=" ")
    #     print()
    # print()
    graph = theGraph.has_cycle()
    # test if a directed graph has a cycle
    if graph is True:
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if graph is False:
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)


if __name__ == "__main__":
  main()

