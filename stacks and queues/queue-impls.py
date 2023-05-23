# queue with enqueue and dequeue operations using separate stacks for each operation

class Queue:

    def __init__(self):
        self.enqueueStack=[]
        self.dequeueStack=[]

    # add item to the stack 
    def enqueue(self, data):
        self.enqueueStack.append(data)

    # remove items from stack to get the first item inserted as queue uses FIFO principle
    def dequeue(self):
        if ( len(self.enqueueStack)==0 and len(self.dequeueStack)==0 ):
            raise Exception("Empty stack nothing to do.")
        # check if dequeue stack empty
        if len(self.dequeueStack)==0:
            # run a loop until last element is reached
            while len(self.enqueueStack)!=0:
                # add all the removed from enqueue stack into the deque stack 
                self.dequeueStack.append(self.enqueueStack.pop())
        
        # returns the ifrst item that was added
        return self.dequeueStack.pop()

if __name__=="__main__":

    queue=Queue()

    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    
    print(queue.dequeue())

    queue.enqueue(99)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())