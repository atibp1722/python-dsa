# data structure using LIFO principle; last item inserted is first item to be removed
# adt that can be implmemented using array(list) or linked list
# most modern programming languages are stack oriented

# memory management of stack: stack memory is special region in the RAM
# stores active function and local variables
# tells python program whre to return after fit finishes running a function

# heap memory: also a special region in the RAM
# larger size than stack memory, it can store objects in it

# how stack memory works
# def funn1():
#   a=1
# firstly, stack memory create frame called 'func1' and variable 'a' will also be created in the frame
# def func2(b):
#   c=2
#   func3()
# a new frame 'func2' is created on top of 'func1' and variables ;b' and 'c' also created for 'func2'
# new frame 'func3' also created in top of 'func2'
# stack first finishes the work of 'func3' and makes it eligible for garbage collection by flushing it out
# control is then transfered to 'func2' the process continues till all frames have been flushed

# stack implementation

class Stack:
    def __init__(self):
        self.stack=[]
    
    # push() method to add element at end of stack
    def push(self, data):
        self.stack.append(data)
    
    #pop() method to remove the element at end of stack
    def pop(self):
        # check if stack already empty
        if len(self.stack)<1:
            return -1
        data=self.stack[-1]
        # removes the last element from the stack
        del self.stack[-1]
        return data
    
    # ppek() method to see the last element without removing it
    def peek(self):
        return self.stack[-1]
    
    # check if stack empty
    def is_empty(self):
        return self.stack==[]
    
    # check size  of the stack
    def stack_size(self):
        return len(self.stack)
    
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Original stack size %d" % stack.stack_size())
print("Popped element %d" % stack.pop())
print("Popped element %d" % stack.pop())
print("Peek %d" % stack.peek())
print("Current stack size %d" % stack.stack_size())