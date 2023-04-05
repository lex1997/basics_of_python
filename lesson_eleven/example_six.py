def decorator_1(func):
    print('декаратор 1')
    def wrapper():
        print('перед функцией дек1')
        func()
    return wrapper

def decorator_2(func):
    print('декаратор 2')
    def wrapper():
        print('перед функцией дек2')
        func()
    return wrapper

@decorator_1
@decorator_2
def basic_1():
    print('basic_1')

@decorator_1
def basic_2():
    print('basic_2')

print('>> старт')
basic_1()
basic_2()
print('>> конец')

