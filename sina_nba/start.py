# coding=utf-8

from score import Score

from live import Live

s = Score()
s.run(True)


def start():
    print '1:score, 2:live'
    num = raw_input('please choose number') or 1

    try:
        num = int(num)
        if num not in [1, 2]:
            num = 1
        return num
    except:
        start()


num = start()

if num == 1:
    s.run(False)
else:
    match_id_list = s.get_rooms()
    print match_id_list
    match_id = raw_input('please choose live')

    l = Live(match_id_list[int(match_id)])
    l.run()
