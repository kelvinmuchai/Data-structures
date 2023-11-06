#O(n log n)
def nlogn(n):
    y = n
    while n > 1:
         n = n//2
         i = 1
         while i <= y:
               print(i)
               i += 1
nlogn(8)

''' 
    An example of an algorithm with a 
    time complexity of O(nlogn) is the 
    mergesort algorithm 
'''