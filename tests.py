# from game import is_correct_number
# from  game import get_hint
#
# print(is_correct_number("dwqdqw"), "dwqdqw")
# print(is_correct_number("432s"), "432s")
# print(is_correct_number("123456"), "123456")
# print(is_correct_number("0324"), "0324")
# print(is_correct_number("2243"), "2243")
# print(is_correct_number("1234"), "1234")
#
#
# print(get_hint("1234","4321")) # 4:0
# print(get_hint("5681","5681")) # 4:4
# print(get_hint("5678","9078")) # 2:0'
import random

a = [11,12,13,23,22,33,21]


def get_game_id():
    used_ids = []
    id_threat = 12
    for thread in a: #threading.enumerate():
        used_ids.append(thread) # used_ids.append(thread.getName())
    while id_threat in used_ids:
        threat = 0
        print("while")
        for i in range(0,2):
            threat += random.randint(1, 3) * pow(10, i)
        id_threat = threat
    return id_threat


print(get_game_id())

