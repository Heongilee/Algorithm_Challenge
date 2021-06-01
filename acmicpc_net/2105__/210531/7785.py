import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    dic = dict()
    for _ in range(n):
        name, state = input().rstrip().split()
        dic[name] = 1 if state == "enter" else 0

    res = []
    for K, V in dic.items():
        if V == 1: res.append(K)
    print("\n".join(sorted(res, reverse=True)))