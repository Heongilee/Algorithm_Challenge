import sys
sys.stdin = open("./Alg_Training/input.txt", "rt")

if __name__ == "__main__":
    N = int(input())
    Coin = list(map(int, input().split()))
    M = int(input())

    D = [2147000000] * (M + 1)
    D[0] = 0

    for c in Coin:
        for j in range(c, M + 1):
            D[j] = min(D[j], D[j - c] + 1)
    print(D[M])