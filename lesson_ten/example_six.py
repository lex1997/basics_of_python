def func():
    while True:
        n = yield
        print(n)

r = func()
r.throw(RuntimeError, "Ошибка на итерации")
# r.send(None)
# r.send(1)
# r.send(2)
# r.close()
# r.send(6)