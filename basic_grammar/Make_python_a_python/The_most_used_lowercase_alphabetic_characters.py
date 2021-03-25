from collections import Counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
ans = Counter(my_list)

# 리스트_이름[카운트_하려는_원소]
print(ans[1])