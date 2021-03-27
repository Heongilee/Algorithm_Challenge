import sys
sys.stdin = open("./CodingTest/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    pos = [(x, y) for x in range(n) for y in range(n) if board[x][y] == 1]

    size = [-1] + [0] * n

    for s in range(1, n + 1):
        for x, y in pos:
            ok = True
            if x + s > n:
                ok = False
            else:
                for i in range(x, x + s):
                    if y + s > n:
                        ok = False
                        break
                    else:
                        if all (e == 1 for e in board[i][y:y + s]):
                            continue
                        else:
                            ok = False
                            break
            if ok:
                size[s] += 1

    # 출력문
    print("total:", sum(size[1:]))
    for i in range(1, n + 1):
        if size[i] == 0:
            break
        else:
            print("size[", end='')
            print(i, end='')
            print("]: ", end='')
            print(size[i], end='')
            print()