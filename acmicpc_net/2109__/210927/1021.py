import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    myList = list(range(1, n + 1))
    query = list(map(int, input().split()))

    cnt = 0
    for q in query:
        tmpLt = myList[:]
        # 왼쪽으로 돌리기
        lt = 0
        while tmpLt[0] != q:
            tmpLt = tmpLt[1:] + [tmpLt[0]]
            lt += 1
        rt = 0
        tmpRt = myList[:]
        while tmpRt[0] != q:
            tmpRt = [tmpRt[-1]] + tmpRt[:len(tmpRt) - 1]
            rt += 1
        if lt < rt:
            tmpLt = tmpLt[1:]
            cnt += lt
            myList = tmpLt
        else:
            tmpRt = tmpRt[1:]
            cnt += rt
            myList = tmpRt
    print(cnt)