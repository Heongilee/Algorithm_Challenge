import sys
sys.stdin = open("./CodingTest/input.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    board = list(map(int, input().split()))
    chk = [1] * n   # 1 to 0
    res = 0

    lt = 0
    rt = n
    while(sum(chk) != 1):
        mid = (lt + rt) // 2
        a = max(board[lt:mid + 1])
        b = max(board[mid + 1:rt])

        if(a > b):
            res += a
            for i in range(lt, mid + 1):
                chk[i] = 0
            lt = mid - 1
        else:
            res += b
            for i in range(mid + 1, rt):
                chk[i] = 0
            rt = mid + 1
    print(res)