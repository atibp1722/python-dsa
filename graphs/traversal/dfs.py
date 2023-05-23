# depth first search
# explores a node as far aspossible before backtracking
# O(V+E) run time
# betther than bfs in memory complexity as it holds less references
# uses stack as its underlying data structure

# visit any node and add it to the stack
# add all its neighbors on to the stack; pop to mark vertex as visited
# visit any neighbor as far as possible; if no neigbor found backtrack
# repeat until all vertex visited and stack empty

class Node:

    def __init__(self,name):
        self.name=name
        self.adjacency_list=[]
        self.visited =False

def DFS(start_node):
    stack=[start_node]

    while stack:
        actual_node=stack.pop()
        actual_node.visited=True
        print(actual_node.name)

        for n in actual_node.adjacency_list:
            if not n.visited:
                stack.append(n)

if __name__=="__main__":

    n1=Node('A')
    n2=Node('B')
    n3=Node('C')
    n4=Node('D')
    n5=Node('E')

    n1.adjacency_list.append(n2)
    n1.adjacency_list.append(n3)
    n2.adjacency_list.append(n4)
    n3.adjacency_list.append(n5)

    DFS(n1)