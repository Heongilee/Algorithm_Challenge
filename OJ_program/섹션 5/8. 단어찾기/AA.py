from collections import deque

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