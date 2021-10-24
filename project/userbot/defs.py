from random import choice as ch, randint as ri

def ran(gg):
    i = 0
    while i < ri(1, 20):
        r = ch(gg)
        i += 1
    return r