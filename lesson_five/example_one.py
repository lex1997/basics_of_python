lst = [3, 6, 1, 8, 5, 3, 3]
lst_plus = list(range(1,10))
# print(lst)
# print(lst_plus)
# print(max(lst), min(lst))
# print(sum(lst))
lst.insert(0, 20)
# print(lst)
# print(lst)

tpl = tuple(lst)
tpl = list(tpl)
tpl.insert(0, 20)
tpl = tuple(tpl)
# print(tpl)
# print(*tpl)
new_lst = []
for i in lst:
    new_lst.append(str(i))

# print(new_lst)

jn = '_'.join(new_lst)
# print(jn)

sp = jn.split('_')
# print(sp)
dct = {
    'ключ': 'значение',
    'ключ1': 'значение234234',
}
# print(dct)
# for i in dct:
#     print(i)

b = dct.copy()

b['новый_ключ'] = 777
# print(dct.keys())
# print(dct)
# print(b)
# print(dct)
# print(key)

# st = set(lst)
# st.add(21)
# print(st)
#
# f = st.pop()
# print(st)
print(f)