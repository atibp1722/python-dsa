# compariosn based algorithm; O(NlogN) run time
# stable sorting: maintains relatie order of items with eqial values
# not inplace: needs O(N) additional memory
# 1. divide: divide the list into 2 sub list recusively
# 2. sort the sublist recusively and merge sort them
# 3. if onyl 1 item in sublist; consider it as sorted
# 4. merge sublist to get final sorted list

# eg 32,12,0,2,1,12,20
# split it into 2 parts left and right
# left 32,12,0 right 3,1,12,20
# further split the sublist into even smaller sub list until every sub list contains exactly one item

def MergeSort(nums):

    # keep spiltting the list until sublist contains 1 item
    if len(nums)==1:
        return
    
    # divide the list into left and rght sub list
    middle=len(nums)//2
    left=nums[:middle]
    right=nums[middle:]

    MergeSort(left)
    MergeSort(right)

    # the divided sub lsit is not to be compared with each other
    # put items in correct place by comparing elemen fro left and right using index of each item

    i=0
    j=0
    k=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            # left sub list's value added to main list
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
        k+=1

    
    while i<len(left):
        nums[k]=left[i]
        i+=1
        k+=1

    while i<len(right):
        nums[k]=right[j]
        j+=1
        k+=1

if __name__=="__main__":

    n=[14,10,15,0,10,4,9,12]
    print(f"Before sort {n}")
    MergeSort(n)
    print(f"After sort {n}")