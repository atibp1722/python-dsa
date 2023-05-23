# aims to store elements more efficiently
# independent 'nodes' contains inforamtion and are connected by references
# aceess to first node (head node) is needed and throught it rest nodes can be acceessed
# last node is always containing null
# follow the references until it reaches null; we have reached end of the linked list
# nodes store information and reference to pointing to the next node in the linked list
# needs more memory than arrays
# there is no need to shift elements
# finding arbitary elements takes O(n) running time

# operations in linked lists
# insert element at beginning takes O(1) time and reference needs to be updated
# insert 5 at beginning: 5 -> null insert 2 at beginning 2 -> 5 -> null; 2 holds the reference to 5 
# remove from beginning also O(1) time just update the reference so the element that was removed is not head
# insert at end: takes O(n) time as all elements needs to travsersed until last element is reached
# steps: 
# 1. start at head 
# 2. traverse all elements 
# 3. reach last that is pointing to null
# 4. insert new node after the last node
# 5. make the new last node point to null
# remove at end also takes O(n) time and steps involved are very similar to inserting
# insert and remove at arbitary posotion also takes O(n) time as nodes needs to traversed until poition reached

# summary:
# linked list acquire memory at runtime making it very dynamic and no need for resizing
# it can store different size items
# manipulating first element is ver fast
# needs more memory
# has no random access to elements
# cannot move backwards
# manipulation and arbitary position takes O(n) time

class Node:

    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList:

    def __init__(self):
        self.head=None
        self.numOfNodes=0

    def insertAtBeginning(self, data):
        self.numOfNodes+=1
        new_node=Node(data)

        if not self.head:
            self.head=new_node
        else:
            new_node.nextNode=self.head
            self.head=new_node
    
    def insertAtEnd(self, data):
        self.numOfNodes+=1
        new_node=Node(data)
        actual_node=self.head

        while actual_node.nextNode is not None:
            actual_node=actual_node.nextNode
        actual_node.nextNode=new_node

    def remove(self, data):
        if self.head is None:
            return
        actual_node=self.head
        prevNode=None

        while actual_node is not None and actual_node.data!=data:
            prevNode=actual_node
            actual_node=actual_node.nextNode

        if actual_node is None:
            return
        self.numOfNodes-=1

        if prevNode is None:
            self.head=actual_node.nextNode
        else:
            prevNode.nextNode=actual_node.nextNode

    def linkedListSize(self):
        return self.numOfNodes
    
    def traverseLinkedList(self):
        actual_node=self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node=actual_node.nextNode


linkedlist=LinkedList()
linkedlist.insertAtBeginning(1)
linkedlist.insertAtBeginning(2.75)
linkedlist.insertAtBeginning("a")
linkedlist.insertAtEnd(3)
linkedlist.insertAtEnd(6.9)
linkedlist.traverseLinkedList()
print("Original linked list size", linkedlist.linkedListSize())
print("------------After remove operation------------")
linkedlist.remove(3)
linkedlist.remove(1)
linkedlist.traverseLinkedList()
print("Current linked list size", linkedlist.linkedListSize())