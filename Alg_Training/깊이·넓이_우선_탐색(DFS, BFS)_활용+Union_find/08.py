import sys
from collections import deque
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == '__main__':
    dx = [-1, 0, +1, 0]
    dy = [0, +1, 0, -1]
    
    N = int(input())
    tree = list(list(map(int, input().split())) for _ in range(N))
    chk = list(list([0] * (N)) for _ in range(N))
    sum = 0
    dQ = deque([])
    chk[N//2][N//2] = 1
    sum += tree[N//2][N//2]
    dQ.append((N//2, N//2))
    
    # BFS
    L = 0
    while L != N // 2:
        size = len(dQ)
        for i in range(size):
            x, y = dQ.popleft()
            for j in range(4):  # E W S N
                X = x + dx[j]
                Y = y + dy[j]
                if(chk[X][Y] != 1):
                    chk[X][Y] = 1
                    sum += tree[X][Y]
                    dQ.append((X, Y))
        L += 1
    print(sum)