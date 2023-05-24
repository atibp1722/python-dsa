# bellman-ford
# slower than dijkstra algorithm
# can hande negatve edge wrights unlike djikstra
# realx all edge in G(V,E) at same time for v-1 iterations
# due negative edge weghts; negative cycle may occur
# main vertex initialized to 0
# all other vertces weight infnity
# terminate the algorithm if now change in distance occurs in 2 consecutive iterations

class Edge:

    def __init__(self, weight,start_vertex,target_vertex):
        self.weight=weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertex

class Node:

    def __init__(self,name):
        self.name=name
        self.adjacency_list=[]
        self.predecessor=None
        self.min_distance=float('inf')

class BellmanFord:

    def __init__(self,vertex_list,edge_list,start_vertex):
        self.vertex_list=vertex_list
        self.edge_list=edge_list
        self.start_vertex=start_vertex
        self.hasCycle=False

    def findShortestPath(self):
        # initialize the start vertex with 0 
        self.start_vertex.min_distance=0
        # make V-1 iterations
        for _ in range(len(self.vertex_list)-1):
            # consider all edges in every iteration
            for edge in self.edge_list:
                u=edge.start_vertex
                v=edge.target_vertex
                dist=u.min_distance+edge.weight

                # update the min distance 
                if dist<v.min_distance:
                    v.predecessor=u
                    v.min_distance=dist
        
        # check for negatve cycles
        for edge in self.edge_list:
            if self.checkCycle(edge):
                print("Negative cycle detected")
                return
            
    def checkCycle(self,edge):
        # if distance decrease after evry iteration there is negative cycle
        if edge.start_vertex.min_distance+edge.weight<edge.target_vertex.min_distance:
            self.hasCycle=True
            return True
        else:
            return False
        
    def getShortestPath(self,vertex):
        # check for negatice cycle
        if not self.hasCycle:
            print("Shortest path has cost",vertex.min_distance)
            # update node value
            node=vertex
            # iterate until node get all predecessor having min distance
            while node is not None:
                print(node.name)
                node=node.predecessor
        else:
            print("Negative cycle occured in the graph")

if __name__=="__main__":

    n1=Node("A")
    n2=Node("B")
    n3=Node("C")
    n4=Node("D")
    n5=Node("E")
    n6=Node("F")

    e1=Edge(5,n1,n2)
    e2=Edge(9,n1,n5)
    e3=Edge(12,n2,n5)
    e4=Edge(4,n1,n2)
    e5=Edge(7,n2,n4)
    e6=Edge(3,n3,n4)
    e7=Edge(1,n3,n6)
    e8=Edge(6,n5,n6)
    e9=Edge(4,n5,n3)
    e10=Edge(3,n4,n5)

    n1.adjacency_list.append(e1)
    n1.adjacency_list.append(e2)
    n2.adjacency_list.append(e3)
    n2.adjacency_list.append(e4)
    n3.adjacency_list.append(e5)
    n3.adjacency_list.append(e6)
    n4.adjacency_list.append(e7)
    n4.adjacency_list.append(e8)
    n5.adjacency_list.append(e9)
    n6.adjacency_list.append(e10)

    vertices=[n1,n2,n3,n4,n5,n6]
    edges=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]

    bellman_ford=BellmanFord(vertices, edges, n1)
    bellman_ford.findShortestPath()
    bellman_ford.getShortestPath(n6)