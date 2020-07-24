N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 테투리 만들기
a.insert(0, [0] * (N + 2))
for i in range(1, N + 1):
    a[i].insert(0, 0)
    a[i].append(0)
a.append([0] * (N + 2))

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1
                
print(cnt)