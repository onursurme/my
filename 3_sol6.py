def double_inputs():
    i=0
    while True:
        #print("From generator {}".format((yield i)))  # print(yield i)  neden hata veriyor?
        print((yield i)) # print(yield i) hata verir, parantez lazım

gen = double_inputs()
#next(gen)       # run up to the first yield
gen.send(None)
input("first stop.")

gen.send(3)
input("2nd stop.")

print(gen.send(10))    # goes into 'x' variable
input("3nd stop.")

# alttaki next olmasa sonraki send next gibi görev yapar, None yazar, sonra 108.6 yazar
next(gen)       # run up to the next yield
input("4th stop.")

gen.send(6)     # goes into 'x' again
input("4th stop.")

#next(gen)       # run up to the next yield
gen.send(94.3)