# print("*" * 8)
# print("*" * 8)
# print("*" * 8)
# print("*" * 8)
# print("*" * 8)
# print("*" * 8)
# print("*" * 8)

def shnyaga(shirina, vysota=10) -> str:
    """

    :param shirina:
    :param vysota:
    :return:
    """
    count = 0
    for _ in range(vysota):
        count += 1 * shirina
        print("*" * shirina)

    return str(count)
#
# shnyaga(
#     shirina=10,
#     vysota=20
# )
# shnyaga(4, 5)
#
# shnyaga()
#
# shnyaga()
b = shnyaga(10)
print(type(b))
