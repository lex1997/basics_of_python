import time

#
# for i in (0, 1):
#     print(i)
#     print(10)
# print('Hello')

# i = 0
# while i < 6:
#     i += 1
#     print('Hello world')
# h = 'Hello world'
# hi = 'Hello'
# if hi in h:
#     print(True)
# char = input('Введите слово: ')
# new_char = ''
# for i in char:
#     if i == 'и' or i == 'о':
#         break
#     else:
#         new_char += i
#     print(10)
#
# print(new_char)
for minute in range(60):
    for sec in range(10):
        print(f"{minute} minute {sec} sec")
        time.sleep(1)


# d = {1, 2, 3, 4}
# print(type(d))
#
# str
# 'sgerg45453232ergerg'