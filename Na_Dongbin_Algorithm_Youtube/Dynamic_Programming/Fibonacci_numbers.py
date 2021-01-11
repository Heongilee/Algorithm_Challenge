import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)

def solution_BottomUp(n):
    D = [0] * (n + 1)
    D[1] = 1
    D[2] = 1
    for i in range(3, n+1):
        D[i] = D[i - 1] + D[i - 2]
    return D[n]

def DFS(n):
    if(n == 1 or n == 2):
        return 1
    if(D[n] != 0):
        return D[n]
    D[n] = DFS(n - 1) + DFS(n - 2)
    return D[n]

def solution_TopDown(n):
    return DFS(n)


if __name__ == "__main__":
    # res = solution_BottomUp(10)
    n = 99
    D = [0] * (n + 1)
    res2 = solution_TopDown(n)
    # print(res, end=' ')
    print(res2)