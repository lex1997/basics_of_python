def gen1(stop):
    n = 1
    while n <= stop:
        yield n
        n += 1

def gen2(start):
    n = start
    while n > 0:
        yield n
        n -= 1

def func(n):
    yield from gen1(n)
    yield from gen2(n)


for n in func(5):
    print('step')
    print(n, end="\n")