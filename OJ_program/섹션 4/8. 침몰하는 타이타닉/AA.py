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