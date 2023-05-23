# associative arrays(map and dictioanry) comprised of key value pairs
# each key can appear at most one time in the collection (no duplicate keys allowed)
# aims to reach O(1) running time for most operations

# operations
# add(key, value)
# remove(key, value)
# lookup(key) look for data with speific given key
# data stored is unordred, so it cannot support sorting operation

# hastable
# uses random access
# h(x) function used to map key to array index to be able to use random indexing
# h(x) define relationhip between key and array index
# h(x) transform key into array index
# h(x) distributes keys uniformally into the array index
# just make sure the index is in the range [0,n-1] where n is the size of the array

# collison
# occurs when h(x) tries to map two keys into the same array index
# 2 techniques for resolving:
# 1. chaining: store item in same index in a linked list
# it basically extends the array index into a linked list where additional keys are stored consecutively
# worst case is it takes O(N) time for arbitary operation as it now a linked list
# 2. open addressing: generate new index for the item
# a. linear probing: if collison at index 'k'; try k+1, k+2... until empty index found
# b. quadriatic probing: if collison at index 'k'; try index that k[1]^2,k[2]^2... steps away from collison
# c. rehasing: if collsion at index 'k'; use h(x) again to generate new index

# dynamic errors
# more items in the hastable more chances of collison occuring
# define a parameter of hastable called load factor
# load factor = m/n [m is the size of array, n is the number of items]
# small load factor: few items so chances of collision are low; but lot of memory is wasted
# large load factor: hashtable nearly full, high proablity of collisions, memory not wasted
# if java detects load factor >0.75 it automatically resizes hash table
# if python detects load factor >0.66 it automatically resizes hash table

class HashTable:

    def __init__(self):
        self.capacity=10
        self.keys=[None]*self.capacity
        self.values=[None]*self.capacity

    def hash(self, key):
        hash_sum=0
        for val in key:
            hash_sum=hash_sum+ord(val)
        return hash_sum%10
    
    def insertItem(self, key, data):
        index=self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index]==key:
                self.values[index]=data
                return
            index=(index+1)%self.capacity
        self.keys[index]=key
        self.values[index]=data

    def getItem(self, key):
        index=self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index]==key:
                return self.values[index]
            index=(index+1)%self.capacity
        return None
    
if __name__=="__main__":
    
    table=HashTable()
    table.insertItem('Ram',20)
    table.insertItem('Hari',22)
    table.insertItem('Rita',25)
    table.insertItem('Gita',21)
    table.insertItem('Sita',28)

    print(table.getItem("Rita"))