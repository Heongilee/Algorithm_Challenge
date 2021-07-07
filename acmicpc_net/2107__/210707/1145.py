import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    n = 1
    while True:
        if sum(map(lambda e: 1 if n % e == 0 else 0, arr)) >= 3: break
        n += 1
    print(n)