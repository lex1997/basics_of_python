from example_two import Cars, ElectroCars

# from example_one import Comment
#
# comment_user_2 = Comment(
#     user='alex',
#     date='26/03/2023',
#     time='20:24',
#     message='питонизация'
# )
#
# comment_user_2.print_comment()
#
# comment_user_3 = Comment(
#     user='ale2',
#     date='26/03/2023',
#     time='20:24',
#     message='питонизация'
# )
# comment_user_2.print_comment()
#
# comment_user_4 = Comment(
#     user='alex6',
#     date='26/03/2023',
#     time='20:24',
#     message='питонизация'
# )
#
# comment_user_2.print_comment()

auto = ElectroCars(
    color='Silver',
    mark='Subaru',
    god='2011',
    probeg=220000
)
auto.printCar()

auto.moove(2500)
auto.printCar()

auto.moove(2500)
auto.printCar()


