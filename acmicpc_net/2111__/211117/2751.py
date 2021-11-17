import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(int(input()) for _ in range(n))
    arr.sort()
    print("\n".join(map(str, arr)))