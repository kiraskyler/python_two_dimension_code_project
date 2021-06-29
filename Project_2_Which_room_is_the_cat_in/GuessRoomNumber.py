# 重要：
# 本课题及以后的课题有基础模板，但是资料光盘被我扔垃圾桶了，网上也找不到资料，所以资能尽可能地按照书中要求编程
# 可能需要按基础模板修改

import simpleguitk
import random

secret_number = 0  #
room_number_max = 25  # [0, 25)
remaining_guesses = 5  # 5次机会
new_game_started = True
msg_game_start = "开始输出，回车确定"


def get_remaining_guesses():
    return '剩余' + str(remaining_guesses) + '次'


def guess_room_number(user_input):
    global remaining_guesses
    global new_game_started

    if not new_game_started:
        lable.set_text("游戏已经结束！重新点击房间")
        input.set_text('')
        return

    user_input_number = int(user_input)
    remaining_guesses -= 1

    if user_input_number == secret_number:
        new_game_started = False
        lable.set_text("恭喜你猜中啦！点击房间重新开始！")
        input.set_text('')
    else:
        if remaining_guesses <= 0:
            new_game_started = False
            print('游戏结束，你没有猜对！')
            input.set_text('')
        elif user_input_number < secret_number:
            lable.set_text('小了点，再来' + ', ' + get_remaining_guesses())
            input.set_text('')
        else:
            lable.set_text('大了点，再来' + ', ' + get_remaining_guesses())
            input.set_text('')


def new_game(room_num, guesses):
    global remaining_guesses
    global new_game_started
    global secret_number
    global room_number_max

    room_number_max = int(room_num)
    secret_number = random.randint(0, room_number_max)
    remaining_guesses = int(guesses)
    new_game_started = True
    lable.set_text(msg_game_start + ', ' + get_remaining_guesses())
    input.set_text('')


def room_25():
    new_game(25, 5)


def room_36():
    new_game(36, 6)


def room_100():
    new_game(100, 7)


frame = simpleguitk.create_frame("hello word", 100, 100)
input = frame.add_input("输入小猫在哪个房间", guess_room_number, 100)
button_25 = frame.add_button("25个房间", room_25, 50)
button_36 = frame.add_button("36个房间", room_36, 50)
button_100 = frame.add_button("100个房间", room_100, 50)
lable = frame.add_label(msg_game_start + ', ' + get_remaining_guesses())
new_game(25, 5)
frame.start()
