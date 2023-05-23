# graphs are data unordered structures containing vertices (V) and edges (E) taht connect vertices
# G(V,E) where v is vertices and e is the edges
# types: directed and undirected
# undirected can be traversed both ways A-B [(A,B),(B,A)] are valid
# directed can travel only in specified direction A->B only [(A,B)] is valid
# weighted graph: vertices have weight (cost) defined to them
# unweighted graph: vertices have no weight (cost) defined to them

# tree- undirected graph where any 2 vertices are connected by exactly on edge
# forest- undirected graph where connected components are tree (disjoint union of trees)
# directed acyclic graph (DAG)- finite directed graph wuth no directed cycles
# complete graph- every single pair of vertices are connected

# adjacency list- assign a list to every vertex in graph that stores edges accordingly
# adjacency matrix- for given G(V,E) contruct matrix 'M' of size V*V 
# where M[i][j] represent edge weight from node i to node j

# breadth first search (BFS)
# aims to visit every single node eactly once
# start with given vertex, visit the neighbor of the vertex, visit the neighbor of neighbor until all nodes visited
# O(V+E) run time
# stores lots of references so memory consumtion is high
# advntage is that it constructs a shortest path
# first, visit any vertex and initialize it in the queue
# visit all neighbors of the vertex and add them to the queue
# dequeue the neighbor from queue and traverse its neighbors and marks it as visited
# repeat process till all vertex are dequeued (visited) and empty queue is returned

class Node:

    def __init__(self,name):
        self.name=name
        self.adjacency_list=[]
        self.visited=False

def BFS(start_node):
    queue=[start_node]

    #iterate the queue till it returns empty queue
    while queue:
        actual_node=queue.pop(0)
        actual_node.visited=True
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            if not n.visited:
                queue.append(n)

if __name__=="__main__":

    n1=Node("A")
    n2=Node("B")
    n3=Node("C")
    n4=Node("D")
    n5=Node("E")

    # provide the neighbors to the nodes
    n1.adjacency_list.append(n2)
    n1.adjacency_list.append(n3)
    n2.adjacency_list.append(n4)
    n3.adjacency_list.append(n5)

    BFS(n1)