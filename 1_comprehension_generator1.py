# [ k*k for k in range(1, n+1) ] list comprehension
# { k*k for k in range(1, n+1) } set comprehension
# ( k*k for k in range(1, n+1) ) generator comprehension
# { k : k*k for k in range(1, n+1) } dictionary comprehension

# 1den 3e kadarki sayıların karelerini veren generator comprehension yaz, sonra toplamını bul
# 1+4+9=14
























total=sum(k*k for k in range(1,4))
print(total)

# aynı generator'a bir isim ver ve sonra toplamını bul








ilk3kare=(k*k for k in range(1,4))
total=sum(ilk3kare)
print(total)