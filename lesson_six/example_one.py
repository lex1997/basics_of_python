x = 60
y = 5


def sum(x):
    """
    функция суммирования y
    :param x: числовое значение
    :return: возвращает кортежь или строку
    """
    global y
    y += 1
    if x:
        return y, 'jvvjhcjh', True
    else:
        return 'x is empty'


# a, b, c = sum(1)
# for i in a, b, c:
#     print(i)

result = lambda x,y,z: (y**x)//z
print(result(4, 7, 5))

