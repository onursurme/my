def double_inputs():
    i=0
    while True:
        #print("From generator {}".format((yield i)))  # print(yield i)  neden hata veriyor?
        print((yield i)) # print(yield i) hata verir, parantez lazım

gen = double_inputs()
#next(gen)       # run up to the first yield
gen.send(None)
print(gen.send(10))    # goes into 'x' variable

# alttaki next olmasa sonraki send next gibi görev yapar, None yazar, sonra 108.6 yazar
next(gen)       # run up to the next yield
gen.send(6)     # goes into 'x' again

#next(gen)       # run up to the next yield
gen.send(94.3)