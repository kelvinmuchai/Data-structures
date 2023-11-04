def mergesort(array):
     if len(array)<2:
         return array
     middleindex = len(array)//2
     leftarray = array[:middleindex]
     rightarray = array[middleindex:]
     return merge(mergesort(leftarray),mergesort(rightarray))


def merge(leftarray , rightarray):
     result  = []
     leftIndex = 0
     rightIndex  = 0

     while (leftIndex < len(leftarray) and rightIndex < len(rightarray)):
          if leftarray[leftIndex] < rightarray[rightIndex]:
               result.append(leftarray[leftIndex])
               leftIndex += 1
          else:
               result.append(rightarray[rightIndex])
               rightIndex += 1

def fact(n):
     start = 1
     if n == 0:
          return 1
     else:
          for i in range(1,n+1):
               start *= i
          return start

print(fact(20))


def factorial(n):
     #Assuring that n is a positive integer or 0.
     if n >= 1:
          return n * fact(n-1)
     else:
          return 1
     
print(factorial(20))