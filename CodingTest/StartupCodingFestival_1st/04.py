import sys
sys.stdin = open("./CodingTest/input.txt", "rt")

PREF_STRING = ['A', 'B', 'C', 'D', 'E']
if __name__ == '__main__':
    pref = dict(zip(PREF_STRING, list(map(float, input().split()))))
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    prior = [list(input()) for _ in range(n)]
    res = []

    # 열람 안한 콘텐츠
    Y = [[prior[x][y], x, y] for x in range(n) for y in range(m) if board[x][y] == 'Y']

    # 열람했지만, 끝까지 안 본 콘텐츠
    O = [[prior[x][y], x, y] for x in range(n) for y in range(m) if board[x][y] == 'O']

    for i in range(len(Y)):
        k, x, y = Y[i][0], Y[i][1], Y[i][2]
        Y[i].insert(1, pref[k])
    
    for i in range(len(O)):
        k, x, y = O[i][0], O[i][1], O[i][2]
        O[i].insert(1, pref[k])
    
    Y.sort(key=lambda x:x[1], reverse=True)
    O.sort(key=lambda x:x[1], reverse=True)

    for i in range(len(Y)):
        res.append(' '.join(map(str, Y[i])))

    for i in range(len(O)):
        res.append(' '.join(map(str, O[i])))
    
    print('\n'.join(res))
