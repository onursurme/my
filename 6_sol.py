import os

# disk_usage(path) : path ile verilen bir yolda kullanılan harddisk alanını byte olarak recursive hesaplar
# path bir file'a aitse file'ın boyutunu, bir klasörse klasörün boyutunu döner
# os.path.getsize(path) : file veya klasörün size'ı (klasörün altklasörlerini görmez)
# os.path.isdir(path) : path bir directory'ye aitse true döner
# os.listdir(path): path bir klasöre ait olmak şartıyla içindeki dosya ve klasörlerin listesini verir
# os.path.join(path1, path2)  path1 ve path2'yi birleştirip yeni path döner. ör: c:\m7 ile bicycle'ı birleştirip c:\m7\bicycle döner


path = 'C:\\m7\\apple'
# raw string deniyor. boşluk karakteri varsa path'de raw string olarak yazınca sorun çıkmıyor
path2 = r'C:\m7\apple\adobe illustrator mac'
path3 = r'C:\m7\0 Julia'
path4 = r'C:\m7\bicycle'
# print(os.path.getsize(path2)) # mac'deki windows'da çalışmadı nedense, sıfır dönüyor
#print("listdir : ",os.listdir(path2))

# print("os.stat : ",os.stat(path2))  # içindeki st_size sıfır nedense, scandir kullanmak gerekiyor
# print("os.stat : ",os.stat(path2).st_size)  # sıfır veriyor hatalı olarak
print(disk_usage(path4))
print(os.path.getsize(path4))