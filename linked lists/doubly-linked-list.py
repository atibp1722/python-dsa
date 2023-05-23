# node can ne categorized into 2 parts; head and tail
# every node stores data itself and references to its next node and also to its previous node
# prev of 1st node and next of last node will always be null 
# needs more memory than singly linked lsit
# eg: 3 -><- 2
# 1st and last nodes can be accessed in O(1) running time
# traversal poosible in both directions; from left to right and right to left
# removing elements is easire due to previous node reference

class Node:

    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    # in dll insertion of new element is done at the end of the list
    def insert(self, data):
        new_node=Node(data)

        # check if list is empty of not
        if self.head is None:
            # if empty the new node is both head and the tail
            self.head=new_node
            self.tail=new_node
        
        # if there are more than 1 element present in the list
        # keep inserting new nodes at the end
        # update tail so it always holds reference of new node that is inserted
        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
    
    # traverse list from left to right
    def traverseForward(self):
        actual_node=self.head

        # iteration to print data until last element has been reached
        while actual_node is not None:
            print(actual_node.data)
            actual_node=actual_node.next

    # traverse list from right to left
    def traverseBackward(self):
        actual_node=self.tail

        # iteration to print data until first element has been reached
        while actual_node is not None:
            print(actual_node.data)
            actual_node=actual_node.prev

if __name__=="__main__":

    dll=DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    print("------Forward traversal------")
    dll.traverseForward()
    print("------Backward traversal------")
    dll.traverseBackward()