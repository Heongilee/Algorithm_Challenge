import sys
sys.stdin = open("./Alg_Training/input.txt", "rt")

# Knap-sack 알고리즘 (1차원 리스트로 해결)
if __name__ == '__main__':
    N, M = map(int, input().split())
    D = [0] * (M + 1)

    for i in range(N):
        pv, pt = map(int, input().split())

        for j in range(M, pt - 1, -1):
            D[j] = max(D[j], D[j - pt] + pv)
    print(D[M])