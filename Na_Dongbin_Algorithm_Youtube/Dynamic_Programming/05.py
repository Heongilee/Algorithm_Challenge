import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)

    D = [0] * (n + 1)
    D[1] = 1
    res = 0

    for i in range(1, n + 1):
        M = 0 
        for j in range(i - 1, 0, -1):
            if(arr[j] > arr[i] and D[j] > M):
                M = D[j]
        D[i] = M + 1

    print(n - D[n])
