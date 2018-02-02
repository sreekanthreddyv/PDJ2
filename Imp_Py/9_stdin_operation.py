from sys import stdin

val = stdin.read()

res = reduce(lambda x, y: x*y, range(1, int(val)+1))
print(res)

