N, M = map(int, input().split())
N = list(map(int, str(N)))

S = []
for x in N:
    while (S) and (M > 0) and (S[-1] < x):
        S.pop()
        M -= 1
    S.append(x)

if (M != 0):
    S = S[:-M]

print(''.join(map(str, S)))