import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    D = [arr[0]] + [0] * (len(arr) - 1)
    for i in range(1, len(arr)):
        D[i] = max(map(lambda j: D[j] if arr[j] < arr[i] else 0, range(i))) + arr[i]
    print(max(D))