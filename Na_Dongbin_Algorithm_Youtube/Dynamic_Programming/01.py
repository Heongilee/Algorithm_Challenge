import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

if __name__ == "__main__":
    n = int(input())
    k = list(map(int, input().split()))
    D = [0] * n
    D[0] = k[0]
    D[1] = max(k[0], k[1])

    for i in range(2, n):
        D[i] = max(D[i - 1], D[i - 2] + k[i])
        
    print(D[n - 1])

    
    