import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def DFS(v):
    global escape
    if v == des:        # 목적지를 찾으면 출력
        escape = True
        print("yes")
        return
    if not graph[v]:    # leaf 노드라면 back
        return
    for i in graph[v]:  # 자식들 탐색
        DFS(i)
        if escape: return


if __name__ == '__main__':
    n, q = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    for _ in range(q):
        src, des = map(int, input().split())
        escape = False
        DFS(src)
        if not escape: print("no")