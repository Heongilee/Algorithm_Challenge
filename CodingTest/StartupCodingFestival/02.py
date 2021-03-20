import sys
sys.stdin = open("./CodingTest/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    board = list(map(int, input()))
    D = [0] * n
    
    D[0] = 0 if not board[0] else 1
    D[1] = 0 if not board[1] else 1

    for i in range(2, n):
        D[i] = D[i - 1] + D[i - 2] if board[i] != 0 else 0
    
    print(D[n - 1])