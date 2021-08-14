import sys
from collections import defaultdict
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    dic = defaultdict(int)
    for _ in range(n):
        t = input().rstrip()
        dic[t] += 1
    for _ in range(n - 1):
        t = input().rstrip()
        dic[t] -= 1
    for k, v in dic.items():
        if v >= 1:
            print(k)
            sys.exit(0)