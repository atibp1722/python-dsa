# find the largest item in the stack

class Stack:
    
    def __init__(self):
        self.maxStack=[]
        self.mainStack=[]

    # push items into the stacks
    def push(self, data):
        self.mainStack.append(data)
        # check if only 1 element in the stack
        if (len(self.mainStack)==1):
            # add the sole element on to max stack and it is the max element and exit
            self.maxStack.append(data)
            return
        # check if data is greater than element that is already in max stack
        if data>self.maxStack[-1]:
            # if data larger add it to the max stack
            self.maxStack.append(data)
        else:
            # data from main stack not greater than element in max stack
            # then duplicate the last element in the max stack
            self.maxStack.append(self.maxStack[-1])
        
    # pop items from the stack
    def pop(self):
        self.maxStack.pop()
        return self.mainStack.pop()
    
    # get the max item from the max stack
    def get_max_val(self):
        return self.maxStack.pop()
    
if __name__=="__main__":

    stack=Stack()

    stack.push(10)
    stack.push(1)
    stack.push(90)
    stack.push(120)
    stack.push(4)

    print(stack.get_max_val())