def decarator(func):
    print('декаротор')
    def wrapper():
        print('-- до функции', func.__name__)
        func()
        print('-- после функции', func.__name__)
    return wrapper

@decarator
def wrapped():
    print('-- обернутая функция')


print('- старт программы...')
wrapped()
print('-конец программы')
