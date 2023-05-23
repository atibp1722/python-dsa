# divide and conquer algorithm: divide problem into even smaller sub problem
# comparison based algorithm
# inplace sorting but not stable
# O(NlogN) average case run time complexity
# useful for sortng primitive type pbjects

# has 2 phases:
# 1. parition: generate pitvot item, it partitions the elements into 2 sub lists
# left contains item smaller than pivot
# right contains items larger than pivot
# pivot can be found by taking miidle element of list
# or genrate randomly by taking item from range [first_index, last_index] of list
# rearrange the items until it satisfy the partition conidition
# 2. recusrion: call partition recursively for left and right sub list

class QuickSort:

    def __init__(self, data):
        self.data=data

    def sort(self):
        self.quickSort(0, len(self.data)-1)

    def quickSort(self, low , high):
        if low>=high:
            return
        
        pivot=self.partition(low, high)
        self.quickSort(low, pivot-1)
        self.quickSort(pivot+1, high)
    
    def partition(self, low, high):
        pivot=(low+high)//2

        self.data[pivot], self.data[high]=self.data[high], self.data[pivot]
        for j in range(low, high):
            if self.data[j]<=self.data[high]:
                self.data[low], self.data[j]=self.data[j], self.data[low]
                low+=1
        
        self.data[low], self.data[high]=self.data[high], self.data[low]
        return low
    
if __name__=="__main__":

    n=[3,2,-3,0,-2,1,-1]
    print(f"Before sort {n}")
    quick=QuickSort(n)
    quick.sort()
    print(f"After sort {n}")