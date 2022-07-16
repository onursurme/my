# binary_sum(S,start,stop):  S isimli array'in toplamını döner
# S'i sağ ve sol diye iki parçaya böler, recursive olarak parçaların toplamından S'in toplamını bulur
# stop son indeksin 1 büyüğü (Python'da slice'lar 2. indeksin 1 küçüğünde bitiyor. range(0,3)'ün 0,1,2 olması gibi)


























def binary_sum(S,start,stop):
    if start==stop-1:
        return S[start]
    mid=(start+stop)//2
    return binary_sum(S,start,mid)+binary_sum(S,mid,stop)

data1=[1,2,3,4,5,6,7]
for x in range(1,7):
    print(x," : ",binary_sum(data1,0,x))
print()
for x in range(4,7):
    print(x," : ",binary_sum(data1,3,x))
