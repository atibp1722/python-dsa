# python has no array data structure implementation
# it has lists which basically is a dynamic array
# memory address = list_index + element_index + data_size

# adding element: if becomes full, larger portion of memory has to be allocated
# small size: memory not wasted but array ahs tobe resized frequently
# larger size: memory is wasted but no need to woory about array resizing

# add element at arbitary position: O(n) running time as all items needs to be linearly shifted 
# worse case: all elements needs to be shifted

# remove last elmement: O(1) running time as access is needed to only the last index

# remove element at arbitary position: index of element to remove is not known
# after removing elements "hole" is created at index where element was removed from
# deal with hole: find element in O(n) time and remove it in O(1) time and shift the other elements in O(n) time

# summary: manipulate the last element is easy as it takes only O(1) time
# manipulate element at arbitary places takes O(n) time so it is time consuming process

# array implementation using list

array=[1,2.5,3,'a',5]
print(array[0])
print(array[1])
print(array[:])
print(array[0:3])
print(array[:-1])
array[4]="hello"
print(array[4])
print(array[:])
# print(array)
print("")

num=[1,4,2,6,5]
high=num[0]
for val in num:
    if val>high:
        high=val
print("Max element in the list",high)
low=num[0]
for val in num:
    if val<low:
        low=val
print("Min element in the list",low)