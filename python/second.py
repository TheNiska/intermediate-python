import logging as lg


def do_stuff():
    print('doing stuff')
    lg.warning('warning 2')

    try:
        x = 2 / 0
    except Exception as e:
        lg.error(e)
