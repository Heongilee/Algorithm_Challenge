import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

'''
N, M = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
b = [0] * N

res = 0
for i in range(N - 1):
    if(b[i] != 0):
        continue
    myJ = -1
    for j in range(i + 1, N):
        if((a[i] + a[j] <= M) and (b[myJ] == 0)):
            myJ = j
    if(myJ != -1):
        res += 1
        b[i] += 1
        b[myJ] += 1
        
print(res + 1)
'''
##########################################################################
'''
N, M = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
cnt = 0
while a:
    if((len(a) - 1 != 0) and (a[0] + a[- 1] <= M)):
        a.pop(0)
        a.pop()
    else:
        a.pop()
    cnt += 1
    
print(cnt)

'''
# COMMENT : pop 연산을 할 때 마다 자료들의 shifting이 일어나기 때문에 비효율적임.
##########################################################################
# DEQUE : 리스트의 앞 쪽에서도 I/O 가능, 뒤 쪽에서도 I/O 가능.
# 예를 들어, 앞 쪽 자료의 deque연산을 수행했다고 할 경우 자료들의 shifting이 아닌, 포인터 이동을 하기 때문에 효율적.

# 사용법 : 
'''
from collections import deque   # 헤더에 선언.
d = []
d = deque(d)

d.popleft()     # 앞쪽 자료를 꺼냄.
d.pop(idx)      # idx + 1 번째 자료를 꺼냄.
d.pop()         # 맨 뒤쪽 자료를 꺼냄.
'''

from collections import deque
N, M = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a = deque(a)
cnt = 0
while a:
    if((len(a) - 1 != 0) and (a[0] + a[- 1] <= M)):
        a.popleft()
        a.pop()
    else:
        a.pop()
    cnt += 1
    
print(cnt)
##########################################################################
