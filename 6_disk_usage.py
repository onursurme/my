import os

# disk_usage(path) : path ile verilen bir yolda kullanılan harddisk alanını byte olarak recursive hesaplar
# path bir file'a aitse file'ın boyutunu, bir klasörse klasörün boyutunu döner
# os.path.getsize(path) : file veya klasörün size'ı (klasörün altklasörlerini görmez)
# os.path.isdir(path) : path bir directory'ye aitse true döner
# os.listdir(path): path bir klasöre ait olmak şartıyla içindeki dosya ve klasörlerin listesini verir
# os.path.join(path1, path2)  path1 ve path2'yi birleştirip yeni path döner. ör: c:\m7 ile bicycle'ı birleştirip c:\m7\bicycle döner
# mantık şu : recursive yazmasaydın nasıl yazacaktın? klasörün içindekilerden biri bir klasörse, içerdeki o klasör için de aynı
# şeyleri yazmaya başlayacaktın, sonra onun içinde de bir klasör varsa onun için de aynı şeyleri yazacaktın, ...
# öyleyse aynı şeyleri yazmak yerine fonksiyonu tekrar çağırmak mantıklı

























def disk_usage(path):  # kitaptaki
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)                  # account for direct usage
    if os.path.isdir(path):                        # if this is a directory,
        for filename in os.listdir(path):            # then for each child:
            childpath = os.path.join(path, filename)  # compose full path to child.
            # üssteki ve alttaki satır total += disk_usage(os.path.join(path,filename)) şeklinde tek satır olarak yazılabilir
            total += disk_usage(childpath) # add child's usage to total
    print('{0:<9}'.format(total), path)     # descriptive output (optional)
    return total


def disk_usage_my(path):  # ben yazdım ve çalışmıyor, diğerleri çalışıyor
    total = os.path.getsize(path)
    print("total of ", path, " =", total)
    subs = os.listdir(path)
    print("subs=", subs)
    subdirs = [x for x in subs if os.path.isdir(os.path.join(path, x))]
    print("subdirs=", subdirs)
    # input()
    for y in subdirs:
        total += disk_usage_my(os.path.join(path, y))
    return total

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

def get_dir_size(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


path = 'D:\\m7\\bicycle'
# raw string deniyor. boşluk karakteri varsa path'de raw string olarak yazınca sorun çıkmıyor
path2 = r'D:\m7\apple\adobe illustrator mac'
path3 = r'D:\m7\0 Julia'
path4 = r'D:\m7\bicycle'
# print(os.path.getsize(path2)) # mac'deki windows'da çalışmadı nedense, sıfır dönüyor
#print("listdir : ",os.listdir(path2))

# print("os.stat : ",os.stat(path2))  # içindeki st_size sıfır nedense, scandir kullanmak gerekiyor
# print("os.stat : ",os.stat(path2).st_size)  # sıfır veriyor hatalı olarak
print(disk_usage_my2(path))
print(get_dir_size(path), " (get_dir_size)")
# print(os.scandir(path))
