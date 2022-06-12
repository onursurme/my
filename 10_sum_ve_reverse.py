# bir list'in toplamını recursive hesaplayan bir fonks yaz


























def summ(data):
    if len(data)==0:
        return 0
    return summ(data[:-1])+data[-1]

# bir list alıp onun tersi şekilde sıralanmış yeni bir list dönderen recursive bir fonks yaz
# girdi : data   çıktı : data2
# hint : 2 yol var























def reverse0(data):
    if len(data)==1:
        return [data[0]]
    data2=[data[-1]]+reverse0(data[:-1])
    return data2

def reverse(data):  # reverse4 ile benzer, yeni bir list oluşturuyor
    if len(data)<2:
        return data
    l1=[data[-1]]
    l2=reverse(data[1:-1])
    l3=[data[0]]
    data2=l1+l2+l3
    #print(l1,l2,l3,"(ara basamak)")
    return data2

# girdi : data,start,end  (start=reverse edilecek kısmın başlangıç indeksi, end=reverse edilecek kısmın bitiş endeksi)
# çıktı : yok (data reverse edilecek)
























def reverse2(data,start,end):  # çalışıyor ama start ve end parametrelerinin olmadığı hali de yazılabilir
    if start>=end:
        return
    data[start],data[end]=data[end],data[start]
    reverse2(data,start+1,end-1)

# reverse2'nin reverse3(data,start=0,end=0) halini yaz. start ve end sıfırsa end=len(data)-1 yapılacak


























def reverse3(data,start=0,end=0): # kitapta böyle
    if start==0 and end==0:
        end=len(data)-1
    if start>=end:  #kitapta if start<end deyip altına son 2 satırı yazmışlar
        return
    data[start],data[end]=data[end],data[start]
    reverse3(data,start+1,end-1)

# reverse4(data,start,end):   recursive olacak, burada end dahil değil (end-1'e kadarki kısım reverse edilecek
# (ipucu: def satırı ile birlikte toplam 4 satır)
# bunun 2'den tek farkı end'in dahil olmaması, end-1'e kadarki kısmın reverse edilmesi

























def reverse4(data,start,stop):                # kitaptaki. tail recursion var(yani son satır bir recursive çağrı
                                              # bunda stop len-1 değil len (python'daki slice'lar böyle)
                                              # ben diğerlerini buna uygun yazmadım (stop len-1 bendim yazdıklarımda)
    if start<stop-1:                          # if at least 2 elements
        data[start],data[stop-1]=data[stop-1],data[start] # swap first and last
        reverse4(data,start+1,stop-1)            # recur on rest

# def reverse5(data)  data'ya dokunmadan yeni bir list oluşturan versiyon, recursive



























def reverse5(data):  # data'ya dokunmadan yeni bir list oluşturan versiyonu yazayım dedim
    if len(data)==0:
        return []    # sadece return yazınca nontype ile list'i toplayamam diyor
    return [data[-1]]+reverse5(data[0:-1])   # baştaki data[-1] i köşeli paranteze almazsam list kabul etmiyor
                                             # data[0:-1] deki sıfır gereksiz

# iterative, reverse6(data), data'yı reverse eder, ilk ve son elemanı yer değiştir, 2. ve sondan 2. elemanı yer değiştir,...



























def reverse6(data): # iterative version yazdım
    # bu da olur : 
    # start=0
    # end=len(data)-1
    # while start<end:
    #     data[start],data[end]=data[end],data[start]
    #     start+=1
    #     end-=1
    for x in range(len(data)//2):
        data[x],data[len(data)-1-x]=data[len(data)-1-x],data[x]

# iterative, reverse7(data,start,stop) (ipucu : reverse4 (kitaptaki) tail recursive)


























def reverse7(data,start,stop):   # üstte kitaptaki hali var (reverse4), tail recursion olduğu için ondan türetilen iterative hali
    while start<stop-1:         # if yerine while gelmesine dikkat !!
        data[start],data[stop-1]=data[stop-1],data[start]
        start,stop=start+1,stop-1

data1=[1,2,5,3,9]
data2=[1,2,3,4]
#print(data2[:-1],data2[-1])
print(summ(data1)," sum of data1")
print(summ(data2)," sum of data2")

print(data2, "before reverse is called")
rd1=reverse(data2)
print(rd1, "after reverse is called")
print()

print(data2," before reverse2 is run")
reverse2(data2,0,len(data2)-1)
print(data2," after reverse2 is run")
print()

print(data2," before reverse3 is run")
reverse3(data2)
print(data2," after reverse3 is run")
print()

print(data1," before reverse4 is run")
reverse4(data1,0,len(data1))
print(data1, " after reverse4 is run")
print()

print(data2," before reverse5 is run")
rd5=reverse5(data2)
print(rd5," after reverse5 is run")
print()

print(data1," before reverse6 is run")
reverse6(data1)
print(data1, " after reverse6 is run")
print()

print(data2," before reverse7 is run")
reverse7(data2,0,len(data2))
print(data2," after reverse7 is run")
# data3=[2,3]
# print(data3[0],data3[-1])
# l4=[data2[0]]
# print(l4[0])