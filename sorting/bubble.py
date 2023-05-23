# sorting is putting all the elements of underlying data structure in certain order
# run time complexity
# O(N^2)-quadriatic run time: bubble, insertion, selection sort
# O(NlogN)-linearithmic run time: merge, quick sort
# O(N)-linear run time: bucket, radix sort

# type of sorting algorithms
# in place: doesnot require any addiitional memory
# recursive: divide and conquer approach
# stable: maintain relative order of items with equal values

# bubble sort
# repeatedly iterate through the list and compare pair of adjacent items and swap if they are in wrong order
# too slow for practical problems
# O(N^2) running time
# stable sorting algorithm

class BubbleSort:

    def __init__(self, nums):
        self.nums=nums

    def sort(self):
        for i in range (len(self.nums)-1):
            for j in range (len(self.nums)-i-1):
                if self.nums[j]>self.nums[j+1]:
                    self.swap(j, j+1)

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

if __name__=="__main__":

    n=[7,6,2,1,0,8,-1,3]
    bubble=BubbleSort(n)
    print(f"Before sort {n}")
    bubble.sort()
    print(f"After sort {bubble.nums}")