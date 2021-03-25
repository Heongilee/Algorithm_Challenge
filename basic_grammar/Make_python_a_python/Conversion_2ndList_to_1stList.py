mylist = [[1, 2], [3, 4], [5, 6]]

'''
# 방법 1
ans = sum(mylist, [])

# 방법 2
import itertools as it
ans = list(it.chain.from_iterable(mylist))

# 방법 3
import itertools as it
ans = list(it.chain(*mylist))

# 방법 4 (이 방법이 가장 직관적임)
ans = [e for arr in mylist for e in arr]

# 방법 5
from functools import reduce
ans = list(reduce(lambda x, y: x + y, mylist))
'''

# 방법 6
from functools import reduce
import operator
ans = list(reduce(operator.add, mylist))



print(ans)
# 결과 출력
# [1, 2, 3, 4, 5, 6]

