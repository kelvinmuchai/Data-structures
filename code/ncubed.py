#O(n^3)
#example code -:
def cubed(n):
    for i in n:
        for j in n:
            for k in n:
                print(i,j,k)
a = [i for i in range(10)]
cubed(a)