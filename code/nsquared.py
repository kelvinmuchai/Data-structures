#O(n^2) 
#example code -:
def squared(n):
   for i in n:
       for j in n:
           print(j,i)
a = [i for i in range(10)]
squared(a)