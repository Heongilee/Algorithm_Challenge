import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS(j):
    for k in range(n):
        if not visited[k] and board[j][k] == 1:
            visited[k] = True
            result[i][k] = 1
            DFS(k)

if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        visited = [False] * n
        DFS(i)
    print("".join([" ".join(map(str, result[k])) + ("\n" if k != len(result) - 1 else "") for k in range(len(result))]))