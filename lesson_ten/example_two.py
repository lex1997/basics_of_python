def func(num):
    while num > 0:
        yield num
        num -= 1

for num in func(5):
    if num == 2:
        break
    print(num)
# result = func(5)
# print(next(result))
# print(next(result))
# print(next(result))

# def func():
#     yield 22
#     return 44
#
# result = func()
#
# print(next(result))
# print(result)
# print(next(result))
