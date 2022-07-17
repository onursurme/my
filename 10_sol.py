# bir list'in toplamını recursive hesaplayan bir fonks yaz





























def summ(data):
    if len(data)==0:   # veya len(data)==1 ise return data[0]
        return 0
    return data[0]+summ(data[1:])

data=[0,1,2,3,4,5]
print(data[0:-1])
print(data[-1])
print(data[3:])
print(summ(data))

# bir list alıp onun tersi şekilde sıralanmış yeni bir list dönderen recursive bir fonks yaz
# girdi : data   çıktı : data2

def reverse(data):
    if len(data)==2:
        return [data[1]]+[data[0]]
#     if len(data)==1:    bu çalışmaz, neden?
#         return data
    return [data[-1]]+reverse(data[1:-1])+[data[0]]  # bunda baştaki if len==1 olmuyor, len==2 olmak zorunda
    # return [data[-1]]+reverse(data[0:-1])  bu da olur  . bunda başktaki len 1 de 2 de olabiliyor

def reverse_2(data):
#     if len(data)==1:    bu da çalışır
#         return data
    if len(data)==2:
        return [data[1]]+[data[0]]
    return [data[-1]]+reverse_2(data[0:-1])

print(reverse(data))

data2=[1,2,3]
print("data2[1:-1] = ",data2[1:-1])



# girdi : data,start,end  (start=reverse edilecek kısmın başlangıç indeksi, end=reverse edilecek kısmın bitiş endeksi)
# çıktı : yok (data reverse edilecek)

def reverse2(data,start,end):
    if start>=end:
        return
    data[start],data[end]=data[end],data[start]
    reverse2(data,start+1,end-1)

data=[1,2,3,4,5,6]
print(data)
reverse2(data,1,2)
print(data)
print()

# reverse2'nin reverse3(data,start=0,end=0) halini yaz

def reverse3(data,start=0,end=0): # en iyisi bu oldu. kitapta da böyle yapmışlar
    if start==0 and end==0: # yani fonksiyon ilk kez çağrıldıysa
        end=len(data)-1
    if start>=end:  #kitapta if start<end deyip altına son 2 satırı yazmışlar,benimkinde return açık görünüyor
        return
    data[start],data[end]=data[end],data[start]
    reverse3(data,start+1,end-1)

print(data)
reverse3(data,0,1)
print(data)
print()

# reverse4(data,start,end):   recursive olacak, burada end dahil değil (end-1'e kadarki kısım reverse edilecek
# (ipucu: def satırı ile birlikte toplam 4 satır)

def reverse4(data,start,end):
    if start<end-1:
        data[start],data[end-1]=data[end-1],data[start]
        reverse4(data,start+1,end-1)

print(data)
reverse4(data,0,5)
print(data)
print()

# def reverse5(data)  data'ya dokunmadan yeni bir list oluşturan versiyon, recursive

def reverse5(data):
    if len(data)==1:
        return [data[0]]
    return [data[-1]]+reverse5(data[0:-1])

# def reverse5(data):  böyle de olur
#    if len(data)==0:
#        return []
#    return [data[-1]]+reverse5(data[:-1])

print(data)
print(reverse5(data))
print()

# iterative, reverse6(data), data'yı reverse eder, ilk ve son elemanı yer değiştir, 2. ve sondan 2. elemanı yer değiştir,...

def reverse6(data):
    start=0
    end=len(data)-1
    while start<end:
        data[start],data[end]=data[end],data[start]
        start+=1
        end-=1

# def reverse6(data): # daha önce böyle yazmışım. mantık şu: yapılacak değişim sayısı len(data)'nın yarısı kadar
#     for x in range(len(data)//2):
#         data[x],data[len(data)-1-x]=data[len(data)-1-x],data[x]
# şu da olur :         data[x],data[-1-x]=data[-1-x],data[x]

print(data)
reverse6(data)
print(data)
print()

# iterative, reverse7(data,start,stop) (ipucu : reverse4 (kitaptaki) tail recursive)

def reverse7(data,start,end):
    while start<end-1:
        data[start],data[end-1]=data[end-1],data[start]
        start,end=start+1,end-1
# şu da olur : 
# def reverse7(data,start,stop):
#    for x in range((stop-start+1)//2):
#        data[x+start],data[stop-x]=data[stop-x],data[x+start]

print(data)
reverse7(data,0,5)
print(data)
print()