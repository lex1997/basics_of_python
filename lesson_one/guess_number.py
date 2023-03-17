import random

number = random.randint(1, 10)
print(number)
count_try = 3
print("Угадайте загаданное число")
for i in range(3):
    user_number = int(input("Введите ваш вариант числа: "))
    print(type(user_number))
    if user_number == number:
        print("Вы угадали!!!")
        break
    else:
        print("Вы не угадали, попробуйте еще раз")

