# just like binary search tree; avl tree also tree data structure
# it has guarenteed O(logN) running time
# in avl tree, hrights of two child sub trees of any nodes may vary by atleast one
# it is more rigidly balances hence it is faster
# operations same as bst; insertion and deletion
# but after after every operations checks needs to be done to ensure tree is balanced
# if tree not balanced, make rotations until balance is achieved

# height of an avl tree
# height of a node is longest path from the actual node to the leaf node
# height of null nodes is -1; leaf node height is always 0
# height = max(left subtree, right subtree) + 1
# if height(left subtree) == height(right subtree) then tree is balance
# else tree unbalanced; make rotations
# abs(left subtree height - right subtree height) > 1; tree is unbalanced
# left heavy when left subtree contains ore nodes than right subtree and vice versa

# avl tree rotations
# left: negative balance factor;make left rotation to balance the tree
# right: postitive balance factor;make right rotation to balance the tree
# left-right: leaf node becomes the new root node;previous root node is now right subtree
# right-left: leaf node becomes the new root node;previous root node is now left subtree

class Node:

    def __init__(self, data, parent):
        self.data=data
        self.left=None
        self.right=None
        self.parent=parent
        self.height=0

class AVLTree:

    def __init__(self):
        self.root=None
    
    def insert(self, data):
        # check if tree empty at first
        if self.root is None:
            # if empty, make the data inserted as the root node
            self.root=Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # check if data is smaller than root node
        if data<node.data:
            #if true, insert it to he left subtree
            if node.left is not None:
                self.insert_node(data, node.left)
            else:
                # create a new left node
                node.left=Node(data, node)
                node.height=max(self.calculateHeight(node.left), self.calculateHeight(node.right))+1
        else:
            if node.right is not None:
                self.insert_node(data, node.right)
            else:
                # create a new right node
                node.right=Node(data, node)
                node.height=max(self.calculateHeight(node.left), self.calculateHeight(node.right))+1
        
        #after every insertion check whether balance factor is affected or not
        # it is done by using the height

        self.handleViolation(node)

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)   

    def remove_node(self, data, node):
        if node is None:
            return
        
        # check if left or right sub tree contains node to delete
        if data<node.data:
            self.remove_node(data, node.left)
        elif data>node.data:
            self.remove_node(data, node.right)
        else:
            # node to delete has been found
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

                self.handleViolation(parent)
            
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

                self.handleViolation(parent)

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

                self.handleViolation(parent)

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
    
    def calculateHeight(self, node):
        if node is None:
            return -1
        return node.height
    
    def calculateBalanceFactor(self, node):
        if node is None:
            return 0
        return self.calculateHeight(node.left)-self.calculateHeight(node.right)

    def checkViolation(self, node):
        balance=self.calculateBalanceFactor(node)
        # check which direction rotation has to be made
        if balance>1:
            # it is left heavy tree as it is positive
            if self.calculateBalanceFactor(node.left)<0:
                # it it left-right rotation so rotate it right once
                self.rotateLeft(node.left)
            # right rotataion has to be made regardless of condition being met or not    
            self.rotateRight(node)
        if balance<-1:
            # it is right heavy tree as it is positive
            if self.calculateBalanceFactor(node.right)>0:
                # it it right-left rotation so rotate it right once
                self.rotateRight(node.right)
            # left rotataion has to be made regardless of condition being met or not    
            self.rotateLeft(node)

    def handleViolation(self, node):
        while node is not None:
            node.height=max(self.calculateHeight(node.left), self.calculateHeight(node.right))+1
            self.checkViolation(node)
            node=node.parent

    def rotateRight(self, node):
        print("Rotating the right node",node.data)

        temp_left=node.left
        t=temp_left.right
        temp_left.right=node
        node.left=t

        if t is not None:
            t.parent=node

        temp_parent=node.parent
        node.parent=temp_left
        temp_left.parent=temp_parent

        if temp_left.parent is not None and temp_left.parent.left==node:
            temp_left.parent.left=temp_left
        if temp_left.parent is not None and temp_left.parent.right==node:
            temp_left.parent.right=temp_left

        if node==self.root:
            self.root=temp_left

        node.height=max(self.calculateHeight(node.left), self.calculateHeight(node.right))
        temp_left.height=max(self.calculateHeight(temp_left.left), self.calculateHeight(temp_left.right))+1

    def rotateLeft(self, node):
        print("Rotating the left node",node.data)

        temp_right=node.right
        t=temp_right.left
        temp_right.left=node
        node.right=t

        if t is not None:
            t.parent=node

        temp_parent=node.parent
        node.parent=temp_right
        temp_right.parent=temp_parent

        if temp_right.parent is not None and temp_right.parent.left==node:
            temp_right.parent.left=temp_right
        if temp_right.parent is not None and temp_right.parent.right==node:
            temp_right.parent.right=temp_right

        if node==self.root:
            self.root=temp_right

        node.height=max(self.calculateHeight(node.left), self.calculateHeight(node.right))
        temp_right.height=max(self.calculateHeight(temp_right.left), self.calculateHeight(temp_right.right))+1

    
    def traverse(self):
        if self.root is not None:
            self.inOrderTraverse(self.root)

    def inOrderTraverse(self, node):
        if node.left:
            self.inOrderTraverse(node.left)

        lft=''
        rgt=''
        prnt=''

        if node.left is not None:
            lft=node.left.data
        else:
            lft="Null"
        if node.right is not None:
            rgt=node.right.data
        else:
            rgt="Null"
        if node.parent is not None:
            prnt=node.parent.data
        else:
            prnt="Null"
        
        print("%s Left: %s Right: %s Root: %s Height: %s" % (node.data, lft, rgt, prnt, node.height))

        if node.right:
            self.inOrderTraverse(node.right)


if __name__=="__main__":

    avl=AVLTree()
    avl.insert(32)
    avl.insert(10)
    avl.insert(55)
    avl.insert(1)
    avl.insert(19)
    avl.insert(41)
    avl.insert(16)
    avl.insert(12)

    avl.remove(55)
    avl.remove(19)