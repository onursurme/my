# def insertion_sort(A):   A sıralanacak list, artan şekilde sırala, iterative
# 1. den başlayarak her elemanı sırayla kendinden öncekilerle tek tek karşılaştırıp kaydır

def insertion_sort(A):
    for x in range(1,len(A)):
        y=x-1
        while y>-1:
            if A[x]<A[y]:
                A[x],A[y]=A[y],A[x]
                y-=1
                x-=1
            else:
                y=-1
                
def insertion_sort2(A):
    for x in range(1,len(A)):
        while A[x]<A[x-1]:
            A[x],A[x-1]=A[x-1],A[x]
            x-=1
            if x==0:
                break
                
data=[5,6,4,3,1,2,9,0,3,5]
print(data)
insertion_sort2(data)
print(data)