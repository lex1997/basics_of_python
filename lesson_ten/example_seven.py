def func():
    data = bytearray()
    line = None
    linecount = 0
    while True:
        part = yield line
        linecount += part.count(b'\n')
        data.extend(part)
        if linecount > 0:
            index = data.index(b'\n')
            line = bytes(data[:index+1])
            data = data[index+1:]
            linecount += 1
        else:
            line = None

# r = func()
# print(r.send(None))
# print('+')
# print(r.send(b"python"))
# print('+')
# print(r.send(b"is cool\nit"))
# print('+')
# print(r.send(b"works\n"))
# print(r.send(b"\n"))
def fib(n):
    fib0 = 1
    yield fib0
    fib1 = 1
    yield fib1
    for i in range(n - 2):
        fib0, fib1 = fib1, fib0 + fib1
        yield fib1


# Тест
for num in fib(10):
    pass
print(num)