# coding=utf-8

from score import Score

from live import Live


def start():
    print '1:实时比分, 2:观看文字直播'
    raw_num = None
    while not raw_num:
        try:
            raw_num = int(raw_input('请选择 1 或者 2 : ')) or 1
            assert (raw_num in [1, 2])
        except:
            raw_num = None
    return raw_num


def main(num):
    if num == 1:
        s.run(False)
    else:
        live_id_list, live_desc = s.get_rooms()
        for index, desc in enumerate(live_desc):
            print "场次:%s  %s" % (index, desc.encode('utf-8'))
        match_id = None
        live_count = len(live_id_list)
        while match_id is None:
            try:
                match_id = int(raw_input('请选择正确的场次: '))
                assert (match_id < live_count)
            except:
                match_id = None

        l = Live(live_id_list[match_id])
        l.run()


if __name__ == '__main__':
    s = Score()
    s.run(True)
    main(start())
