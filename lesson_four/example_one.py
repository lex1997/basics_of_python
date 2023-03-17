import random

char = 'PYTHON IS EAZY PYTHON'
word = 'very'
space = ' '
empty = ''

# for i in char:
#     print(i)
# print(char + space + word)
# print(len(char))
# print(len(empty))

# if space in char:
#     print(space in char)
# else:
#     print(space in char)

# print(word in char)

# print((word + '_') * 10)
#
# container = [1, 2, 3, 4, "sgerg", 5.6]
#
# for iter, i in enumerate(container):
#     print(f"индекс элемента: {iter} \n значение элемента: {i}")

# for item, i in enumerate(container):
#     print(f'Значение элемента: {i} под индексом: {item}')

# print(char.strip('PY'))
# new_char = '6'.join(char)
# print(new_char)
# print(new_char.split(' '))

# l = []
# num = 0
# element = []
# for i in range(11):
#     l.append(list(range(random.randint(0, 15))))
#
# print(l)
#
# print(l[3][7])

word = input()
if word == word[::-1]:
    print('Палиндром')
    if len(word) % 2 == 0:
        print('Чётный палиндром')
    else:
        print('Нечётный палиндром')
else:
    print('придумайте другое слово')