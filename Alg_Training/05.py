import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
# <- Time Limit Exceeded
N, M = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 0
cnt = 0
while(i != len(a) - 1 or i != j):
    if(sum(a[i:j + 1]) < M):
        j += 1
    elif(sum(a[i:j + 1]) > M):
        i += 1
    else: # (sum(a[i:j + 1]) == M)
        cnt += 1
        if(i == j):
            j += 1
        else:
            i = j
print(cnt)
'''
########################################################################
N, M = map(int, input().split())
a = list(map(int, input().split()))

L = 0
R = 1
Tot = a[0]
cnt = 0
while(True):
    if(Tot < M):
        if(R >= len(a)):
            break
        Tot += a[R]
        R += 1
    elif(Tot == M):
        cnt += 1
        Tot -= a[L]
        L += 1
    else:   # Tot > M
        Tot -= a[L]
        L += 1
print(cnt)