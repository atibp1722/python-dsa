# tree: undirected graph data structure with V (vertices) and E (edges)
# two vertices are connected by exactly one path (edge)
# tress define a parent-child realtionship
# 3 types of nodes
# root node: always the parent node
# internal nodes: nodes having 1 or 2 children
# leaf nodes: nodes having 0 children

# binary search tree every node can have atmost 2 children
# left node always smaller than root node
# right node always greater than root node
# all nodes can be accessed from root node
# search for nodes at arbitary postion takes O(logN) time
# it takes short time since the data is already sorted, half of the data can be ignored
# height of tree is the number of edges from longest downward path between root and leaf node
# a tree will hev 2^h-1 nodes; ie a root with 2 children can have maximum 7 total nodes
# for searching to take O(logN) time the tree has to be balanced
# an unbalanced tree takes O(N) to search for arbitary elements

# binary search tree operations
# insert: if an empty tree, make the node the root (parent) node
# for each consecutive insertion check if element to be inserted is larger or smaller than root node
# if element smaller insert it into left sub tree for all consecutive elements
# if element larger insert into right sub tree for all consecutive insertion
# search: compare element to search with the root node
# if search element smaller, move to left sub tree and ignore right sub tree; search left sub tree until found
# if search element larger, move to right sub tree and ignore left sub tree; search right sub tree until found
# remove element; remove leaf node, remove node with 1 child, remove node with children (root)
# 1. remove leaf node: notify the parent node that its' leaf node has been deleted
# 2. remove leaf node with 1 child: notify parent instead of pointing to node to be deleted
# point to the child of the node to be deleted
# eg. 12-55-59 to delete 55; notify to 12 to point to 59 instead of pointing to 55
# 3. remove node with 2 children (root): look for successor or predecessor node in entire tree
# successor: smallest in right sub tree; predecessor: largest in left sub tree
# once found swap the successor or predecessor with root element
# repeat step for removing node with 0 children to until root removed

# binary search tree traversal
# pre order traversal: root->left->right
# post order traversal: left->right->root
# in order traversal: left->root->right (it gives sorted list of elements)

class Node:
    
    def __init__(self, data, parent):
        self.data=data
        self.left=None
        self.right=None
        self.parent=parent

class BinarySearchTree:

    def __init__(self):
        self.root=None

    def insert(self, data):
        if self.root is None:
            self.root=Node(data, None)
        else:
            self.insert_node(data, self.root)
    
    def insert_node(self, data, node):
        # move to left sub tree if data smaller than root
        if data<node.data:
            if node.left is not None:
                self.insert_node(data, node.left)
            else:
                node.left=Node(data, node)
        # move to right sub tree if data larger than root
        else:
            if node.right is not None:
                self.insert_node(data, node.right)
            else:
                node.right=Node(data, node)

    def traverse(self):
        if self.root is not None:
            self.inOrderTraversal(self.root)
    
    def inOrderTraversal(self, node):
        if node.left is not None:
            self.inOrderTraversal(node.left)
        print(node.data)
        if node.right is not None:
            self.inOrderTraversal(node.right)

    def getMaxValue(self):
        if self.root is not None:
            return self.getMaxTreeValue(self.root)
    
    def getMaxTreeValue(self, node):
        # continue until right most node of right sub tree is null
        if node.right is not None:
            # return the value of the right most node
            return self.getMaxTreeValue(node.right)
        else:
            return node.data
        
    def getMinValue(self):
        if self.root is not None:
            return self.getMinTreeValue(self.root)
    
    def getMinTreeValue(self, node):
        if node.left is not None:
            return self.getMinTreeValue(node.left)
        else:
            return node.data
        
    def remove_node(self, data, node):
        if node is None:
            return
        
        # check if left or right sub tree contains node to delete
        if data<node.data:
            self.remove_node(data, node.left)
        elif data>node.data:
            self.remove_node(data, node.right)
        else:
            if node.left is None and node.right is None:
                print("Removing leaf node %d" % node.data)
                parent=node.parent

                if parent is not None and parent.left==node:
                    parent.left=None
                if parent is not None and parent.right==node:
                    parent.right=None

                if parent is None:
                    self.root=None
                
                del node
            
            elif node.left is None and node.right is not None:
                print("---Removing node with single right child---")
                parent=node.parent

                if parent is not None:
                    if parent.left==node:
                        parent.left=node.right
                    if parent.right==node:
                        parent.right=node.right
                else:
                    self.root=node.right
                
                node.right.parent=parent
                del node

            elif node.right is None and node.left is not None:
                print("---Removing node with single left child---")
                parent=node.parent

                if parent is not None:
                    if parent.left==node:
                        parent.left=node.left
                    if parent.right==node:
                        parent.right=node.left
                else:
                    self.root=node.left
                
                node.left.parent=parent
                del node

            else:
                print("---Removing node with 2 children---")
                predecessor=self.get_predecessor(node.left)

                temp=predecessor.data
                predecessor.data=node.data
                node.data=temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node
    
    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)

bst=BinarySearchTree()
bst.insert(10)
bst.insert(3)
bst.insert(28)
bst.insert(0)
bst.insert(18)
bst.insert(-2)

bst.remove(28)

bst.traverse()

print("Max value in bst",bst.getMaxTreeValue(bst.root))
print("Min value in bst",bst.getMinTreeValue(bst.root))