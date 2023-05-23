# find the middle node of a given linked list

class Node:

    def __init__(self, data):
        self.data=data
        self.nextNode=None

class LinkedList:

    def __init__(self):
        self.head=None
        self.size=0

    def insert(self, data):
        self.size+=1
        new_node=Node(data)

        if not self.head:
            self.head=new_node
        else:
            new_node.nextNode=self.head
            self.head=new_node

    def getMiddleNode(self):
        # initialize two pointers that traverse nodes at different spped
        # slow traverse one element at a time
        slow=self.head
        #fast traverse 2 nodes at a time
        fast=self.head

        while fast.nextNode is not None and fast.nextNode.nextNode is not None:
            # slow pointer raches the midlle when fast pointer reaches the end
            fast=fast.nextNode.nextNode
            slow=slow.nextNode
        
        return slow
    
    def traverseList(self):
        actual_node=self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node=actual_node.nextNode

if __name__=="__main__":

    ll=LinkedList()
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    print("The middle node of linked list",ll.getMiddleNode().data)