# a, b, c, d = 2, 3.4, 'rgererger', True
#
# for i in (a, b, c, d):
#     print(type(i))

class Comment:
    """
    Коментарии пользователей на вебсайте
    """
    def __init__(self, user, date, time, message):
        self.user = user
        self.date = date
        self.time = time
        self.message = message

    def print_comment(self):
        """
        Выводит информацию о комментарие
        """
        print(
            f'Пользователь {self.user} \n'
            f'написал {self.message} \n'
            f'{self.date} в {self.time}'
        )




