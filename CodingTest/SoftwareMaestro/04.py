import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
INF = int(10e9)

if __name__ == '__main__':
    n = int(input())
    dis = list(map(int, input().split()))
    dis.insert(0, 0)
    res = -INF

    for i in range(1, 4):
        board = [False] * (n + 1)
        cnt = 1
        p = i
        while not board[p]:
            board[p] = True
            p += dis[p]
            cnt += 1
        
        res = max(res, cnt)
    print(res)
        
