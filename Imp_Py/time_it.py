import timeit
import time


def test():
    for val in range(1, 100):
        t = [x**2 for x in range(val)]
        # time.sleep(0.5)
    # print("jj")

# from __main__ import test

# val = min(timeit.repeat(setup="from __main__ import test", stmt="test()", number=1000, repeat=5))

# print(val)


x = 99


def selector():
    global x
    # though, that this means the assignment also changes the global X , not a 8local X
    print(x)
    x = 77


selector()
print(x)

y = 66


def sele():
    from __main__ import y
    print(y)
    y = 55


sele()
print(y)
