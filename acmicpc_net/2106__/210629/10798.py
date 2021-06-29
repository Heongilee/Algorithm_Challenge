import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    col = 0
    board = []
    
    for _ in range(5):
        t = list(input().rstrip())
        if len(t) > col: col = len(t)
        while len(t) != 15: t.append("")
        board.append(t)

    for c in range(col):
        for r in range(5):
            print(board[r][c], end='')
    print()