import sys
sys.stdin = open(".\\Na_Dongbin_Algorithm_Youtube\\input.txt", "rt")

if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']

    N = int(input())
    com = list(map(str, input().split()))
    board = [[0] * N for _ in range(N)]
    start = (0, 0)

    for i in range(len(com)):
        for j in range(4):
            if(com[i] == dir[j]):
                xx = start[0] + dx[j]
                yy = start[1] + dy[j]
                if(0 <= xx < N and 0 <= yy < N):
                    start = (xx, yy)
    print(start[0] + 1, start[1] + 1)