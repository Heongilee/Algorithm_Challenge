import sys, copy as cp
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def moveBlock(dir):
    # 상
    if dir == 0:
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if block[i][j]:
                    temp = block[i][j]
                    block[i][j] = 0
                    if block[idx][j] == 0:
                        block[idx][j] = temp
                    elif block[idx][j] == temp:
                        block[idx][j] = temp * 2
                        idx += 1
                    else:   
                        idx += 1
                        block[idx][j] = temp
    # 하
    elif dir == 1:
        for j in range(n):
            idx = n-1
            for i in range(n - 2, -1, -1):
                if block[i][j]:
                    temp = block[i][j]
                    block[i][j] = 0
                    if block[idx][j] == 0:
                        block[idx][j] = temp
                    elif block[idx][j] == temp:
                        block[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        block[idx][j] = temp
    # 좌
    elif dir == 2:
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if block[i][j]:
                    temp = block[i][j]
                    block[i][j] = 0
                    if block[i][idx] == 0:
                        block[i][idx] = temp
                    elif block[i][idx] == temp:
                        block[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        block[i][idx] = temp
    # 우
    else:
        for i in range(n):
            idx = n-1
            for j in range(n - 2, -1, -1):
                if block[i][j]:
                    temp = block[i][j]
                    block[i][j] = 0
                    if block[i][idx] == 0:
                        block[i][idx] = temp
                    elif block[i][idx] == temp:
                        block[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        block[i][idx] = temp

def DFS(L):
    global res, block
    if L == 5:
        blockToList = [elem for b in block for elem in b]
        res = max(res, max(blockToList)) if res != None else max(blockToList)
        return

    tmp_block = cp.deepcopy(block)
    for d in range(4):
        moveBlock(d)
        DFS(L + 1)
        block = cp.deepcopy(tmp_block)

if __name__ == '__main__':
    n = int(input())
    block = [list(map(int, input().split())) for _ in range(n)]
    res = None

    DFS(0)
    print(res)