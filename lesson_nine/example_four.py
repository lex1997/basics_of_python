# list1 = []
# for i in range(1,11):
#     list1.append(i)
#


list1 = set([i**2 for i in range(1, 11) if i % 2 != 0])

# dict1 = {x: y for x, y in [('A', 2), ('B', 4), ('C', 5)] if x in 'C'}

# dict2 = {}.fromkeys('xyz', "abc")
print(type(list1))
