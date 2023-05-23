import random

bucket=10

class RadixSort:

    def __init__(self, data):
        self.data=data

    def getDigits(self):
        return len(str(max(self.data)))
    
    def sort(self):
        for digit in range(self.getDigits()):
            self.radixSort(digit)
    
    def radixSort(self, d):
        count=[[] for _ in range (bucket)]
        for num in self.data:
            index=(num//10**d)%10
            count[index].append(num)
    
        z=0
        for i in range(len(count)):
            while len(count[i])>0:
                self.data[z]=count[i].pop(0)
                z+=1
if __name__=="__main__":

    n=[23,14,56,124,654,0,2,76,868,1024]
    random.shuffle(n)
    print(f"Before sort {n}")
    radix=RadixSort(n)
    radix.sort()
    print(f"After sort {radix.data}")