import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

if __name__ == "__main__":
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    D = [1000] * (M + 1)
    D[0] = 0
    
    for c in coin:
        for j in range(c, M + 1):
            D[j] = min(D[j - c] + 1, D[j])
    print(D[M])
    