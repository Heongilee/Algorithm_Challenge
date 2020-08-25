#######################################################################
# Big-O : log N
######################################################

import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
N, M = map(int, input().split())
a = list(map(int, input().split()))

s = 0
e = len(a) - 1
i = (e - s) // 2

mid = 0
a.sort()
while(a[i] != M):
    if(a[i] > M):
        e = i
    elif(a[i] < M):
        s = i
    i = (e + s) // 2
print(i + 1)
'''
############################################################################
N, M = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
lt = 0
rt = N - 1
while(lt<=rt):
    mid = (lt + rt) // 2
    if(a[mid] == M):
        print(mid + 1)
        break
    elif(a[mid] > M):
        rt = mid - 1
    else:
        lt = mid + 1