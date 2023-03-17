import random

a = 5
b = 4

if a <= b:
    print(True)
elif a == 4:
    print('a=5')
elif a == 5:
    print('a=5')
elif a == 6:
    print('a=5')
else:
    print(False)

fact_days = random.randint(10, 30)

if fact_days // 2:
    chet_days = True
else:
    chet_days = False

if chet_days:
    print('Скидка заемщику')

