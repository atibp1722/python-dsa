# reverse elements

def reverse_array(n):
    # index values for start and end index
    start=0
    end=len(n)-1

    while end>start:
        # perform swap
        n[start], n[end]=n[end], n[start]
        start+=1
        end-=1

if __name__=="__main__":
    n=[1,3,5,7,9]
    reverse_array(n)
    print(n)
print("")
 
# palindrome check

def palindrome_check(s):

    original=s
    reversed=reverse_string(s)

    if original==reversed:
        return True
    else:
        return False

def reverse_string(data):
    start=0
    end=len(data)-1

    while end>start:
        # convert all to list
        data=list(data)
        data[start], data[end]=data[end], data[start]
        start+=1
        end-=1

    return "".join(data)

if __name__=="__main__":
    print(palindrome_check("cat"))

# Alternate solution
# def palindrome_check(string):
#     if string == string[::-1]:
#         return True
#     else:
#         return False

# if __name__=="__main__":
#     print(palindrome_check('dad'))
print("")

#reverse number

def reverse_integers(n):
    reverse=0
    remainder=0

    while n>0:
        remainder=n%10
        reverse=(reverse*10)+remainder
        n=n//10
    
    return reverse

if __name__=="__main__":
    print(reverse_integers(12345))
print("")

# anagram check

def anagram_check(string1, string2):
    if len(string1) != len(string2):
        return False

    # sort the string values to compare them
    string1=sorted(string1)
    string2=sorted(string2)    

    # check letters having the same index
    for val in range(len(string1)):
        if string1[val] != string2[val]:
            return False
    return True

if __name__=="__main__":
    string1=['o','k','b','a']
    string2=['b','o','k','a']
    print(anagram_check(string1, string2))
print("")

# finding duplicate elements

def duplicate_elements(n):
    for val in n:
        if n[abs(val)]>=0:
            n[abs(val)] = -n[abs(val)]
        else:
            print("Repeated element %s"% str(abs(val)))

if __name__=="__main__":
    n=[1,3,5,2,4,3,5]
    duplicate_elements(n)