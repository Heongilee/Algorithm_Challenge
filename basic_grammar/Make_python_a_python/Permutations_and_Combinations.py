import itertools as it

mylist = ['a', 'b', 'c']
# 순열 구하기
print(list(map(' '.join, it.permutations(mylist))))

# 조합 구하기
print(list(map(' '.join, it.combinations(mylist, 2))))