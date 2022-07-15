import sys

# bir sistemde iç içe kaç recursive çağrı yapılabileceğinin sınırını test eden bir program yaz
# global bir count=0 değişkeni olsun
# her recursive çağrıda count 1 artsın ve ekrana yazılsın







































def a():
    global count
    count+=1
    print(count)
    a()
   
count=0
a()