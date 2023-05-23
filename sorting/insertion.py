# O(N^2) run time
# faster thean selection sort
# adaptive: fast when array already substantailly sorted
# stable: preserves the order of same valued items
# start at 0 index and copmare item with all previous items
# if prev item > actual item perform swap

def InsertionSort(num):

    for i in range(len(num)):
        j=i
        # check all previous items in the list
        # check if previous item is greater than actual item
        while j>0 and num[j-1]>num[j]:
            num[j-1],num[j]=num[j],num[j-1]
            j-=1

if __name__=="__main__":

    n=[4,0,-1,3,1,2]
    print(f"Before sort {n}")
    InsertionSort(n)
    print(f"After sort {n}")