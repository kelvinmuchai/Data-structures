#Binary search and O(log n) --->
#In binary search the array must be ordered.
#array = [1,2,7,12,43,44,54,100,124]
#To find the value 100 in the array
#1.To search with binary search, we start by finding the midpoint.
#2.In the above array after we dind the midpoint we know that to the left the valuess are decreasing and to the right viceversa.
#3.hence we have a starting point and we use the values to the right.
#4.After we find the half where 100 is,we use the half where 100 might be.
#5.We continue this process until we find 100.#

#THE PYTHON CODE IS AS FOLLOWS :
#This program is recursive --:
def binary_search(data,target,low,high):
    if low > high:
        return False
    else:  
       
        mid = (low + high ) // 2
        if target == data[mid]:
            return f'The number {target} is at index {data.index(data[target])}'
            #print(data[target])

        elif target < data[mid]:
            #print(data[:mid-1])
            return binary_search(data,target,low,mid-1)
           
        else:
            #print(data[:mid+1])
            return binary_search(data,target,mid+1,high)
        
data = [i for i in range(60)]
target = 48
low = 0
high = len(data)-1
print(binary_search(data,target,low,high))