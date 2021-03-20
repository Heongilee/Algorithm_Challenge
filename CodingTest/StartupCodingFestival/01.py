import sys
sys.stdin = open("./CodingTest/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    T = [list(input().split(" ~ ")) for _ in range(n)]
    T.sort(key=lambda x: x[0])
    res = []

    Table = dict()

    for i in range(len(T)):
        Table[T[i][0]] = 0
        Table[T[i][1]] = 0
    
    for k, v in Table.items():
        for j in range(len(T)):
            if T[j][0] <= k <= T[j][1]:
                Table[k] = Table.get(k, 0) + 1

    for k, v in Table.items():
        if v >= n:
            res.append(k)
    
    if len(res) == 2:
        print(' ~ '.join(sorted(res)))
    else:
        print(-1)
