def fib_gen():
    a = 0
    b =1
    while True:
        c = a
        a= b
        b = c + a
        yield c
# real work star
f=fib_gen()
for i in range(20):
    print(next(f),end=' ')
