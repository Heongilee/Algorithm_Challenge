import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N, K = map(int, input().split())

a = []
sum = []

# 입력
a = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if(i != j and j != k and k != i):
                sum.append(a[i] + a[j] + a[k])

sum.sort()

cnt = 0
elem = 0
while(cnt < K):
    elem = sum[len(sum) - 1]
    while(sum[len(sum) - 1] == elem):
        sum.pop()
    cnt += 1

print(elem)
'''
###########################################################################
# set 자료구조를 사용함 -> 리스트와 달리 중복을 제거한 리스트 느낌.

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(a[i] + a[j] + a[m]) #중복을 제거하면서 res set에 담는다.

# set 자료구조는 sorting 기능이 없기 때문에 set -> list -> sorting 순서로 가야함.
res = list(res)
res.sort(reverse=True)
print(res[k - 1])