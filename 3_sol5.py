def double_inputs():
    print("generator is started.")
    while True:
        print("next iteration of while.")
        x = yield
        print(f"x={x}")
        yield x * 2

gen = double_inputs()
next(gen)       # run up to the first yield
input("press a key :")
print(gen.send(10))    # goes into 'x' variable
input("press a key :")

# alttaki next olmasa sonraki send next gibi görev yapar, None yazar, sonra 108.6 yazar
next(gen)       # run up to the next yield
input("press a key :")
print(gen.send(6))     # goes into 'x' again
input("press a key :")
#next(gen)       # run up to the next yield
print(gen.send(94.3))