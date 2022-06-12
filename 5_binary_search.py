import random

# binary_search fonks recursive yaz. parametreleri data, target, low, high
# data artan sıralı bir list, target aranan değer, low ve high ise aramanın başlayacağı ve biteceği index değerleri
# tüm data aranacaksa 0 ve len(data)-1
# target data'da varsa indeks değerini döner, yoksa False döner



















def binary_search(data, target, low, high):  # kitaptaki. tail recursion olduğu için altta iterative haline de dönüştürdüm
    if low > high:
        return False # interval is empty; no match
    else:            # bence bu else'e gerek yok, if sağlandıysa zaten return oluyor ve buraya gelmiyor
        mid = (low + high) // 2
        print(low,mid,high)
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)  # buradaki return önemli !!!  -1 de önemli
        else:                                                 # return önemli çünkü bu fonksiyon kendi iş yapmıyor, return ediyor
            return binary_search(data, target, mid + 1, high) # buradaki return önemli !!!  +1 de önemli
                                            # -1 veya +1 olmasa low ve high eşitken mid de eşit olur, ve tekrar low,mid ile
                                            # veya mid,high ile çağırınca yine aynı değerlerle çağrılmış olur ve sonsuz döngü olur
                                            # sürekli daralmalı ki sonunda low>high olsun

data=[2, 4, 9, 11, 12, 22, 29, 43, 45, 46, 47, 54, 64, 65, 73, 74, 89, 91, 95, 97]
print(binary_search(data,95,0,19))
input()

def binary_search2(data,target,low,high): # benim ilk yazdığımSUBOPTIMAL (tail recursion, çünkü son çalışan satır sadece bir recursive çağrı)
                                         # bu nedenle kolayca iterative hale getirilebilir
    if low==high-1:
        if data[high]==target:
            return high
        if data[low]==target:
            return low
        return
    mid=int((low+high)/2)
    print(low,mid,high)
    #print(data[low],data[mid],data[high])
    #input()
    if data[mid]>target:
        return binary_search2(data,target,low,mid)
    elif data[mid]<target:
        return binary_search2(data,target,mid,high)
    else:
        return mid

def binary_search3(data,target,low,high): # ben yazdım, çalışıyor
    mid=(low+high)//2
    print("mid = ", mid)
    print("data["+str(mid)+"]="+str(data[mid]))
    if data[mid]==target:
        print("buldum")
        return mid
    if mid==low and mid==high:
        return False
    if data[mid]>target:
        print(str(low)+" "+str(mid))
        return binary_search(data,target,low,mid)
    else:
        print(str(mid+1)+" "+str(high))
        return binary_search(data,target,mid+1,high)

data=[2, 4, 9, 11, 12, 22, 29, 43, 45, 46, 47, 54, 64, 65, 73, 74, 89, 91, 95, 97]
print(binary_search2(data,95,0,19))
input()



# binary_search fonks iterative yaz. parametreleri data, target, low, high











def binary_search4(data,target,low,high): # recursive olmayan şekilde yazdım (tail recursive olduğu için kolayca bu hale dönüşüyor)
    while not low>high:  # veya while low<=high:
        mid = (low+high) // 2
        print(low,mid,high)
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

def binary_search5(data,target,low,high):
    while True:
        if low>high:
            return False
        mid=(low+high)//2
        if data[mid]==target:
            return mid
        elif data[mid]>target:
            high=mid-1
        else:
            low=mid+1
    
data=[2, 4, 9, 11, 12, 22, 29, 43, 45, 46, 47, 54, 64, 65, 73, 74, 89, 91, 95, 97]
#data = random.sample(range(1, 100), 20)
#data.sort()
#print(data)
#input()
print(binary_search4(data,96,0,19))