import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

INF = int(10e6)
if __name__ == '__main__':
    dq = [0] * INF
    lt, rt = 0, -1

    for _ in range(int(input())):
        line = input().split()

        if line[0] == 'push':
            rt += 1
            dq[rt] = int(line[1])
        elif line[0] == 'pop':
            if lt > rt:
                print(-1)
                continue
            print(dq[lt])
            lt += 1
        elif line[0] == 'size':
            print(rt - lt + 1)
        elif line[0] == 'empty':
            print(1 if lt > rt else 0)
        elif line[0] == 'front':
            print(-1 if lt > rt else dq[lt])
        elif line[0] == 'back':
            print(-1 if lt > rt else dq[rt])
        else:
            sys.exit(0)