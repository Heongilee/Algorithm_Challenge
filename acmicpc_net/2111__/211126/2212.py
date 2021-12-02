import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    print(sum(sorted([arr[i] - arr[i + 1] for i in range(n - 1)], reverse=True)[k - 1:]))