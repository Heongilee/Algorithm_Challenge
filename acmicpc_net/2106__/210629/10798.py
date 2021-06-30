import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    arr = []
    for _ in range(5):
        t = list(input().rstrip())
        while len(t) != 15: t.append("")
        arr.append(t)
    print("".join([arr[r][c] for c in range(15) for r in range(5)]))