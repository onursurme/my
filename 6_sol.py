import os

# disk_usage(path) : path ile verilen bir yolda kullanılan harddisk alanını byte olarak recursive hesaplar
# path bir file'a aitse file'ın boyutunu, bir klasörse klasörün boyutunu döner
# os.path.getsize(path) : file veya klasörün size'ı (klasörün altklasörlerini görmez)
# os.path.isdir(path) : path bir directory'ye aitse true döner
# os.listdir(path): path bir klasöre ait olmak şartıyla içindeki dosya ve klasörlerin listesini verir
# os.path.join(path1, path2)  path1 ve path2'yi birleştirip yeni path döner. ör: c:\m7 ile bicycle'ı birleştirip c:\m7\bicycle döner


















def disk_usage_my1(path):  # iterateive
    pass



def disk_usage_my2(path):  # çalışıyor
    sm=0
    if not os.path.isdir(path):  # path dosyaysa (klasör değilse)
        print(path,os.path.getsize(path))
        sm+= os.path.getsize(path)
    else: # path bir klasör ise:
        print(path)
        for x in os.listdir(path):
            sm+= disk_usage_my2(os.path.join(path,x))
    return sm

# raw string deniyor. boşluk karakteri varsa path'de raw string olarak yazınca sorun çıkmıyor
path = r'D:\m7\bicycle'
print(disk_usage_my2(path))
print(disk_usage_my1(path))