# cetvel çizdir
# draw_line, draw_interval ve draw_ruler fonksiyonlarını yaz
# draw_line : tick_length ve tick_label='' parametrelerini alır ve tek bir satır çizer
# draw_interval : center_length parametresini alır, recursive olarak 2 majorlength arasını doldurur
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









def draw_line(tick_length,tick_label=''):  # print('-'*tick_length+tick_label) şeklinde tek satır yeterli aslında
    line='-'*tick_length
    if tick_label: # ben if tick_label!='': şeklinde yazmıştım önce
        line += ' ' + tick_label
    print(line)
    
def draw_interval(center_length):
    if center_length==0:
        return
    draw_interval(center_length-1)
    draw_line(center_length)
    draw_interval(center_length-1)

def draw_ruler(num_inches,majorlength):
    for x in range(num_inches):
        draw_line(majorlength)
        draw_interval(majorlength-1)
    draw_line(majorlength)
    # şöyle de olur : 
    #    draw_line(majorlength)
    #for x in range(num_inches):
    #    draw_interval(majorlength-1)
    #    draw_line(majorlength)

draw_ruler(1,3)