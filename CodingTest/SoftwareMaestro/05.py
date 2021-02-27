import sys
sys.stdin = open("./CodingTest/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    board = []
    time_limit = 0
    score = 0

    for _ in range(n * n):
        l = list(map(int, input().split()))
        for e in l:
            time_limit = max(time_limit, e)
        board.append(l)
    
    board.sort(key=lambda e: e[0], reverse=True)
    for t in range(1, time_limit + 1):
        for j in range(n * n):
            if t in board[j][2:]:
                score += board[j][0]
                break
    print(score)
