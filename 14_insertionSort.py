# def insertion_sort(A):   A sıralanacak list, artan şekilde sırala, iterative
# 1. den başlayarak her elemanı sırayla kendinden öncekilerle tek tek karşılaştırıp kaydır
















def insertion_sort2(A):    # kitaptaki
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)): # from 1 to n-1
        cur = A[k] # current element to be inserted
        j = k # find correct index j for current
        while j > 0 and A[j-1] > cur: # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur # cur is now in the right place
        

def insertion_sort(data):    # benim yazdığım
    for i in range(1,len(data)):
        cur=i
        for j in range(i-1,-1,-1):
            print(data,end=' ')
            if data[cur]<data[j]:
                data[cur],data[j]=data[j],data[cur]
                cur-=1
            print(cur+1,j,data)


data=[4,3,2,1,7]
insertion_sort(data)
print(data)
print()

data2=[4,3,2,1,7,5]
insertion_sort2(data2)
print(data2)
