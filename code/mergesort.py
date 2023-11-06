#Merge sort and O(nlogn) -->
def mergesort(array):
     if len(array)<2:
         return array
     middleindex = len(array)//2
     leftarray = array[:middleindex]
     rightarray = array[middleindex:]

     leftarray = mergesort(leftarray)
     rightarray = mergesort(rightarray)

     return merge(leftarray,rightarray)
   

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
          result.extend(leftarray[leftIndex:])
          result.extend(rightarray[rightIndex:])

          return result
     
my_list = [3,6,7,8,34,87,32]
sorted_list = mergesort(my_list)
print(sorted_list)

