# generalization fo insertion sort algorithm
# sorts pair of items far waay from each other
# progressively gap is reduced until it becomes 1
# relies heavily upom gap sequence
# gap = length[list]//2
# item separated by long distance can travel faster hence reducing the time
# when gap becomes 1, it is an insertion sort
# gap sequence items sorted using insertion sort as underlying sub routine

def ShellSort(num):

    gap=len(num)//2

    while gap>0:
        for i in range(gap, len(num)):
            j=i
            while j>=gap and num[j-gap]>num[j]:
                num[j],num[j-gap]=num[j-gap],num[j]
                j-=gap
        gap=gap//2

if __name__=="__main__":

    n=[3,0,5,-1,4,1,2]
    print(f"Before sort {n}")
    ShellSort(n)
    print(f"After sort {n}")