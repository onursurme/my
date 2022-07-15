# binary_search fonks recursive yaz. parametreleri data, target, low, high.
# data artan sıralı bir list, target aranan değer, low ve high ise aramanın başlayacağı ve biteceği index değerleri
# tüm data aranacaksa 0 ve len(data)-1
# target data'da varsa indeks değerini döner, yoksa False döner























def binary_search(data,target,low,high):
    if low > high:
        return False
    mid=(low+high)//2
    print(low,mid,high)
    print(data[low],data[mid],data[high])
    if data[mid] == target:
        return mid
    elif data[mid]>target:
        return binary_search(data, target, low, mid - 1)    # buradaki return önemli !!!  -1 de önemli
    else:                                                   # return önemli çünkü bu fonksiyon kendi iş yapmıyor, return ediyor
        return binary_search(data, target, mid + 1, high)   # buradaki return önemli !!!  +1 de önemli
                                                       # -1 veya +1 olmasa low ve high eşitken mid de eşit olur, ve tekrar low,mid ile
                                                       # veya mid,high ile çağırınca yine aynı değerlerle çağrılmış olur ve sonsuz
                                                       # döngü olur. sürekli daralmalı ki sonunda low>high olsun

data=[2, 4, 9, 11, 12, 22, 29, 43, 45, 46, 47, 54, 64, 65, 73, 74, 89, 91, 95, 97]
print(binary_search(data,95,0,19))

# binary_search fonksiyonunu iterative yaz

def binary_search2(data,target,low,high):
    while low<=high:
        mid=(low+high)//2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

data=[2, 4, 9, 11, 12, 22, 29, 43, 45, 46, 47, 54, 64, 65, 73, 74, 89, 91, 95, 97]
print("binary_search2 (iterative) sonucu : ",binary_search2(data,4,0,19))