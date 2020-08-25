import sys
from collections import deque
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N = int(input())
a = deque(list(map(int, input().split())))
tmp_min = 0
res = ""
cnt = 0
while a:
    if(a[0] > tmp_min or a[-1] > tmp_min):
        if(a[0] < a[-1]):
            tmp_min = a.popleft()
            cnt += 1
            res += "L"
        else:
            tmp_min = a.pop()
            cnt += 1
            res += "R"
    else:
        break
print(cnt)
print(res)
'''
####################################################################
'''
N = int(input())
a = list(map(int, input().split()))
last = 0
res = ""
lt = 0
rt = N - 1
cnt = 0
while (lt <= rt):
    if(a[lt] < last and a[rt] < last):
        break
    tmp = []
    tmp.append((a[lt], "L"))
    tmp.append((a[rt], "R"))
    tmp.sort()
    tmp = deque(tmp)
    while (tmp[0][0] < last):
        tmp.popleft()
    if(tmp[0][1] == "L"):
        lt += 1
    else:
        rt -= 1
    last = tmp[0][0]
    res += tmp[0][1]
    cnt += 1
    
print(cnt)
print(res)
'''
#######################################################################
N = int(input())
a = list(map(int, input().split()))
lt = 0
rt = N - 1
last = 0
res = ""
tmp = []
while(lt <= rt):
    if(a[lt] > last):
        tmp.append((a[lt], 'L'))
    if(a[rt] > last):
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if(len(tmp) == 0):
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if(tmp[0][1] == 'L'):
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)