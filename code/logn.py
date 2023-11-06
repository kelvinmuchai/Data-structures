#O(log n)
#logarithms
#a^b = c
#base case in comp science is always 2
#log 8 = 3
#It is equal to 2^3 = 8
def logfunc(n):
    while n>1:
        n = n/2
    return n 
n = 8
print(logfunc(n))

#An example of an algorithm with a time complexity of logn is binary search.
