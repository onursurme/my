# binary_sum(data) , data bir list






























def binsum(data):
    if len(data)==1:
        return data[0]
    return binsum(data[0:len(data)//2])+binsum(data[len(data)//2:len(data)])




# binary_sum(S,start,stop):  S isimli array'in toplamını döner
# S'i sağ ve sol diye iki parçaya böler, recursive olarak parçaların toplamından S'in toplamını bulur
# stop son indeksin 1 büyüğü (Python'da 2. indeksin 1 küçüğünde bitiyor. range(0,3)'ün 0,1,2 olması gibi)




























def binary_sum(S, start, stop):      # kitaptaki
    if start >= stop:                # zero elements in slice (recursive çağrılarda bu koşula gerek yok ama
                                     # kullanıcıdan ilk çağrıda böyle gelebilir)
        print("start>=stop",start,stop)
        return 0
    elif start == stop-1:                  # one element in slice
        print("start==stop-1",start,stop)
        return S[start]
    else:                                  # two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop) # ilk yarı mid-1'de biter, 2. mid ile başlar




def binary_sum1(S,start,stop):  # benim ilk yazdığım. kitaptakine baya benzer yazmışım, hatam son indeksi dahil etmem
                                # halbuki son indeksten 1 öncesinde bitmeli. Bende mid+1 var,
                                # stop length kadar olmalı, çünkü Python'da slicing yaparken S[0:0] boş, S[0:1] ise S[0] oluyor
                                # yani 2. elemanın bir eksiğine kadar gidiliyor
    if stop>len(S)-1:
        return "overflow"
    mid=(start+stop)//2
    #print("start mid stop=",start,mid,stop)
    if stop==0:
        #print("returning 0th element : ",S[0])
        return S[0]
    if start==len(S):
        #print("returning 0")
        return 0
    if start==stop:
        #print("returning ",start,"th element : ",S[start])
        return S[start]
    #print("call for :",start,mid)
    #print("call for :",mid+1,stop)
    return binary_sum1(S,start,mid)+binary_sum1(S,mid+1,stop)  # slice'da son sayının 1 küçüğüne kadar diye düşününce ilk
           # yarı mid değil mid-1'e kadar gider, ikinciyi mid+1 değil mid ile başlatmak gerekir, tıpkı alttaki fonksiyondaki gibi
           # ama ben slice'ı 2. sayıya kadar (1 eksiğine kadar değil) diye kabul ettiğim için böyle oldu



data1=[1,2,3,4]
for x in range(0,4):
    print(x," : ",binary_sum1(data1,0,x))
print()
for x in range(0,5):
    print(x," : ",binary_sum(data1,0,x))
