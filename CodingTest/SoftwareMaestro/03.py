import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
INF = int(10e9)

def painting(s, e):
    for i in range(s, e + 1):
        visited[i] = True

if __name__ == '__main__':
    n, m, e = map(int, input().split())
    nuts = list(map(int, input().split()))
    cnt = 0 # 현재 먹은 땅콩 개수
    visited = [False] * (max(nuts) + 1)

    while cnt != m:
        t = 0               # 최소 거리의 땅콩 인덱스
        minimum = INF  # 최소 거리
        for i in range(len(nuts)):
            if abs(nuts[i] - e) < minimum and not visited[nuts[i]]:
                minimum = abs(nuts[i] - e)
                t = nuts[i]
        painting(e, t) if(e < t) else painting(t, e)
        e = t
        cnt += 1
    print(visited.count(True) - 1)
        

