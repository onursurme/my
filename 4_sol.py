# cetvel çizdir
# draw_line, draw_interval ve draw_ruler fonksiyonlarını yaz
# draw_line : tick_length ve tick_label='' parametrelerini alır ve tek bir satır çizer
# draw_interval : center_length parametresini alır, recursive olarak 2 majorlength arasını doldurur (iterative olanını da yaz)
# draw_ruler (asıl fonksiyon): num_inches ve majorlength parametrelerini alır, diğer 2 fonksiyonu kullanır
# ör : draw_ruler(2,5)


# -----
# -
# --
# -
# ---
# -
# --
# -
# ----
# -
# --
# -
# ---
# -
# --
# -
# -----
# -
# --
# -
# ---
# -
# --
# -
# ----
# -
# --
# -
# ---
# -
# --
# -
# -----

def draw_line(tick_length,tick_label=''):
    print('-'*tick_length+tick_label)
    
def draw_interval(center_length):
    if center_length==0:
        return
    draw_interval(center_length-1)
    draw_line(center_length)
    draw_interval(center_length-1)

def draw_interval2(center_length):  # iterative
    num=1 # number of lines in the interval to be printed
    if center_length<2:
        num=center_length
    if center_length>1:
        for x in range(2,center_length+1):
            num=num*2+1
    #print(num)
    mid=(num+1)/2
    for x in range(1,num+1):
        # buradan sonra binary search gibi gideceğiz, ortayı bulacağız, 1 eksilteceğiz,...        
        draw_line(center_length-binser(num,x))

def binser(n,x):  # draw_interval2 yani iterative olan için yazıldı
    # interval'de n tane line olacakken x inci line'ın uzunluğu center_length'ten kaç eksik olmalı
    # mantık şu : her ortaya gitme adımı uzunluğu bir azaltıyor
    steps=0
    start,stop=1,n
    while True:
        mid=(start+stop)/2
        if x==mid:
            return steps
        if x>mid:
            start=mid+1
            steps+=1
        else:
            stop=mid-1
            steps+=1

def draw_ruler(num_inches,majorlength):
    for x in range(num_inches):
        draw_line(majorlength)
        draw_interval2(majorlength-1)
    draw_line(majorlength)
    
draw_ruler(2,3)