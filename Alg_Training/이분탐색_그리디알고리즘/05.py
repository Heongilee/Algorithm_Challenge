import random as rd
import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
Case #01 : Wrong Answer
Case #02 : Wrong Answer
Case #03 : Time Limit Exceeded
Case #04 : Time Limit Exceeded
Case #05 : Time Limit Exceeded
'''
'''
def isOverlap(x, y, lt, rt):
    if((lt > x and lt < y) or (rt > x and rt < y)):
        return True
    else:
        return False

N = int(input())
a = []
for _ in range(N):
    c, d = map(int, input().split())
    a.append((c, d))

res = 0
for i in range(N):
    cnt = 0
    for j in range(i, N):
        if(i == j):
            continue
        elif(isOverlap(a[i][0], a[i][1], a[j][0], a[j][1])):
            continue
        else:
            cnt += 1
            
    res = max(res, cnt)
print(res)
'''
#########################################################################
'''
그리디 알고리즘(탐욕 알고리즘) ?
-> 문제를 풀어나가는 과정(단계)에 있어서 이 단계에서 가장 좋은 해를 판별해서 선택해 나가는 것.
-> 제일 좋은것을 판별하는 방법?
    -> 정렬을 한다.
'''

N = int(input())
meeting = []

for _ in range(N):
    s, e = map(int, input().split())
    meeting.append((s, e))

# TIP : 튜플에서 앞에 자료 값을 기준으로 정렬을 수행한다.
# meeting.sort()

# 튜플 리스트에서 뒤의 값 자료를 기준으로 정렬하려면 다음과 같이 쓴다. (key 이용.)
meeting.sort(key=lambda x: (x[1], x[0]))

cnt = 0
et = 0
for s, e in meeting:
    if(s >= et):
        et = e
        cnt += 1
        
print(cnt)
