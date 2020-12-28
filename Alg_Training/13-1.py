import sys
import copy as cp
sys.stdin = open("./Alg_Training/input.txt", "rt")

# Knap-sack 알고리즘 (2차원 리스트로 해결)
'''
D = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...], 
[0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, ...], 
[0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 25, 25, ...], 
[0, 0, 0, 0, 0, 10, 10, 10, 15, 15, 15, 15, 25, 25, ...], 
[0, 0, 0, 6, 6, 10, 10, 10, 16, 16, 16, 21, 25, 25, ...], 
[0, 0, 0, 6, 7, 10, 10, 13, 16, 17, 17, 21, 25, 25, ...]
]
'''
if __name__ == '__main__':
    N, M = map(int, input().split())
    D = list([0] * (M + 1) for _ in range(N + 1))

    for i in range(1, N + 1):
        D[i] = cp.copy(D[i - 1])
        pv, pt = map(int, input().split())

        for j in range(pt, M + 1):
            D[i][j] = max(D[i][j], D[i - 1][j - pt] + pv)
    
    print(D[N][M])

