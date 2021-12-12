import random
import sys


# coding:utf-8


def tree(branchLen, t):
    if branchLen > 2:
        if 8 <= branchLen <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branchLen / 3)
        elif branchLen < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branchLen / 2)
        else:
            t.color('sienna')
            t.pensize(branchLen / 10)

        t.forward(branchLen)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        tree(branchLen - 10 * b, t)
        t.left(40 * a)
        tree(branchLen - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branchLen)
        t.down()
