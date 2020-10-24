import itertools
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

tmpList = list(itertools.product(iterable1, iterable2, iterable3))
res = list(map(lambda x : ''.join(x), tmpList))
print(res)