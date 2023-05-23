import heapq

# djikstra algorithm
# O(VlogV+E) runtime
# greedy approach- find the global optimum using the local optimum
# every iteration tries to ffind the minimum distance between the vertices
# cannot handle negative weights

class Edge:

    def __init__(self,weight,start_vertex,target_vertex):
        self.weight=weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertex

class Node:

    def __init__(self,name):
        self.name=name
        self.visited=False
        # track the vertex that was visited previously
        self.predecessor=None
        self.adjacency_list=[]
        self.min_distance=float('inf')

    # override the less than function to compare objects
    # cpmarison of objects done based on their distance
    def __lt__(self,other):
        return self.min_distance<other.min_distance
    

class Djikstra:

    def __init__(self):
        self.heap=[]

    def calculate(self, start_vertex):
        start_vertex.min_distance=0
        heapq.heappush(self.heap, start_vertex)

        # iterate the heap
        while self.heap:
            # pop vertex with lowest min distance
            actual_vertex=heapq.heappop(self.heap)
            # view the neighbors of the vertex
            for edge in actual_vertex.adjacency_list:
                u=edge.start_vertex
                v=edge.target_vertex
                new_distance=u.min_distance+edge.weight
                # a shorter path to vertex exists
                if new_distance<v.min_distance:
                    # update the new lowest min distance
                    v.predecessor=u
                    v.min_distance=new_distance
                    heapq.heappush(self.heap,v)

            actual_vertex.visited=True

    @staticmethod
    def shortestPath(vertex):
        print("Shortest path to vertex %s"%str(vertex.min_distance))
        actual_vertex=vertex

        while actual_vertex is not None:
            print("%s"%actual_vertex.name)
            actual_vertex=actual_vertex.predecessor

if __name__=="__main__":

    n1=Node('A')
    n2=Node('B')
    n3=Node('C')
    n4=Node('D')
    n5=Node('E')

    e1=Edge(4,n1, n2)
    e2=Edge(6,n1, n5)
    e3=Edge(3,n1, n3)
    e4=Edge(15,n2, n4)
    e5=Edge(9,n2, n3)
    e6=Edge(15,n5, n3)
    e7=Edge(13,n5, n4)
    e8=Edge(20,n3, n4)
    e9=Edge(8,n3, n5)
    e10=Edge(7,n4, n5)

    n1.adjacency_list.append(e1)
    n1.adjacency_list.append(e2)
    n2.adjacency_list.append(e3)
    n2.adjacency_list.append(e4)
    n4.adjacency_list.append(e8)
    n3.adjacency_list.append(e6)
    n3.adjacency_list.append(e9)
    n5.adjacency_list.append(e10)

    djik=Djikstra()
    djik.calculate(n1)
    djik.shortestPath(n4)