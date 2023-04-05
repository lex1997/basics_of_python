# a = 'hello'
# iterator = iter(a)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

tuple1 = ('ключ', 'гайка', 'болт')
myit = iter(tuple1)
for i in tuple1:
    print(next(myit))

