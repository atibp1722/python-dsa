# O(N^2) run time
# known for simplicity and performance advantage over complex sorting algorthms
# useful when additional meory is not required
# it searches to the minimum value in the list
# swap it with the left most item 
# this process continues until all items are in correct order
# not stable sort algorithm
# always outperforms ubble sort

# eg consider list: -2,1,13,5,8,-5
# -5 is the smallest item; swap it with left most item -2
# -5 is now sorted in its correct place
# updated list: -5,1,13,5,8,-2
# again repeat search for smallest now it is -2 swap with left most [except -5] i.e. 1
# updated list: -5,2,13,5,8,1
# repeat search until all elements are in correct order

def SelectionSort(num):
    for i in range(len(num)-1):
        index=i
        # searching for the min value in the list
        for j in range(i, len(num)):
            if num[j]<num[index]:
                # update to the min value
                index=j
        
        # dont swap the item with itself
        if index!=i:
            num[index],num[i]=num[i],num[index]

if __name__=="__main__":
    
    n=[5,1,4,-1,0,3,2]
    print(f"Before sort {n}")
    SelectionSort(n)
    print(f"After sort {n}")