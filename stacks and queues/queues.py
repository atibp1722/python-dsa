# data structure using FIFO principle; first element inserted in is the first element to be removed
# used by OS and in multi threading problem solving
# enqueue(insert) in done from the rear and dequeue(remove) is done drom the front
# it is vital in CPU scheduling 
# used when resources has to shared among multiple processes(threads)

class Queue:

    def __init__(self):
        self.queue=[]
    
    # enqueue() to insert element at end of queue
    # O(1) time as element is added to end of queue
    def enqueue(self, data):
        self.queue.append(data)
    
    # dequeue() to remove element from beginning of queue
    # O(1) time as element is removed from front of the queue
    def dequeue(self):
        if len(self.queue)<1:
            return -1
        data=self.queue[0]
        del self.queue[0]
        return data
    
    #check if queue empty
    def is_empty(self):
        return self.queue==[]
    
    # peek to view element
    def peek(self):
        return self.queue[0]
    
    # show size of the queue
    def size_queue(self):
        return len(self.queue)
    
queue=Queue()
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print('Original size of queue %d' % queue.size_queue())
print('Dequeue element %d' % queue.dequeue())
print('Dequeue element %d' % queue.dequeue())
print('Dequeue element %d' % queue.dequeue())
print('Peek queue element %d' % queue.peek())
print('Current size of queue %d' % queue.size_queue())