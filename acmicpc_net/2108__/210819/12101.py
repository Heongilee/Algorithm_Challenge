import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS(S):
    global j
    if S > n:
        return
    if S == n:
        j += 1
        if j == k:
            print("+".join(map(str, myList)))
            sys.exit(0)
    for i in range(1, 4):
        myList.append(i)
        DFS(S + i)
        myList.pop()

if __name__ == '__main__':
    myList = []
    j = 0
    n, k = map(int, input().split())

    DFS(0)
    print(-1)