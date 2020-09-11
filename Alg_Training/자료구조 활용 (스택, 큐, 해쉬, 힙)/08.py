import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
from collections import deque
'''
N = int(input())
a = list(input() for _ in range(N))

for _ in range(N - 1):
    t = input()
    
    for i in range(len(a)):
        if(a[i] == t):
            a[i] = '0'
a.sort(reverse=True)
print(a[0])
'''
#####################################################################
# Dictionary 자료구조는 문자열도 키값으로 쓰일 수 있다는 점이 포인트다.

N = int(input())
poem = dict()  # 빈 딕셔너리 생성.

for i in range(N):
    word = input()
    poem[word] = 1

for i in range(N - 1):
    word = input()
    poem[word] = 0

poem = list(map(lambda x: (x[1], x[0]), poem.items()))
poem.sort(reverse=True)
print(poem[0][1])