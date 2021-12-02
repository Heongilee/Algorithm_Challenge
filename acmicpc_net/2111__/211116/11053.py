import sys
# sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    D = [0] * n
    D[0] = 1
    for i in range(1, n):
        maxV = 0
        for j in range(i):
            if arr[j] < arr[i] and D[j] > maxV:
                maxV = D[j]
        D[i] = maxV + 1
    print(max(D))