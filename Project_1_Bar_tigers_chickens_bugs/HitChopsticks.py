import random

gustures = ['虫子', '鸡', '老虎', '杠子']


def name_to_number(name):
    if name in gustures:
        return gustures.index(name)
    else:
        return -1


def number_to_name(num):
    if num < gustures.__len__():
        return gustures[num]
    else:
        return '所喊无效！'


def shut_out(name):
    if name == '随机':
        return random.randint(0, 3)
    else:
        return name_to_number(name)


def play_one_round(player1_name, player1_code, player2_name, player2_code, print_msg=True):
    """

    :param player1_name:
    :param player2_name:
    :param player1_code:
    :param player2_code:
    :param print_msg:
    """
    if player1_code >= gustures.__len__():
        if print_msg:
            print(player1_name + '玩家所喊无效！')
        return -1

    if player2_code >= gustures.__len__():
        if print_msg:
            print(player2_name + '玩家所喊无效！')
        return -1

    code_res = player1_code - player2_code
    if code_res == 1 or code_res == -3:
        res = 1
    elif code_res == -1 or code_res == 3:
        res = 2
    else:
        res = 0

    if print_msg:
        print(player1_name + '喊的为：' + number_to_name(player1_code))
        print(player2_name + '喊的为：' + number_to_name(player2_code))
        if res == 0:
            print(player1_name + '和' + player2_name + '打成平手！')
        elif res == 1:
            print(player1_name + '获胜！')
        else:
            print(player2_name + '获胜！')

    return res


def probability_calculate():
    i = 0
    player_win = [0, 0, 0]

    while i < 1280:
        play_res = play_one_round('甲', shut_out('随机'), '乙', shut_out('随机'), print_msg=False)
        player_win[play_res] += 1
        i += 1

    print('甲、乙随机比赛128次，验证对决结果的概率为')
    print('甲方获胜的概率为：%f' % (float(player_win[1] / (player_win[0] + player_win[1] + player_win[1]))))
    print('双方平局的概率为：%f' % (float(player_win[0] / (player_win[0] + player_win[1] + player_win[1]))))
    print('甲方失败的概率为：%f' % (float(player_win[2] / (player_win[0] + player_win[1] + player_win[1]))))


random.seed()
probability_calculate()
