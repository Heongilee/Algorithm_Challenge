import sys
sys.stdin = open("./Alg_Training/input.txt", "rt")

if __name__ == "__main__":
    N, K = map(int, input().split())
    D = [0] * (K + 1)

    for i in range(N):
        v, w = map(int, input().split())    # Jewel, Weight
        for j in range(v, K + 1):
            D[j] = max(D[j], D[j - v] + w)

    print(D[K])