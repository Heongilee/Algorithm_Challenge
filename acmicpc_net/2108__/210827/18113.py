import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

INF = int(10e8)
if __name__ == '__main__':
    # L < 2K, then -K
    # L <= K, then 폐기
    # 손질된 김밥 // ? == P (P는 양의 정수), 최소 M개 만듦
    n, k, m = map(int, input().split())
    myList = [] # 손질된 김밥의 길이가 들어있는 리스트
    for line in sys.stdin:
        l = int(line.rstrip())
        if l <= k:
            continue
        elif l < 2 * k:
            l -= k
        else:
            l -= 2 * k
        myList.append(l)
    lt, rt = 1, INF
    ans = None
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = sum(map(lambda L: L // mid, myList))
        if cnt < m:
            rt = mid - 1
        elif cnt >= m:
            lt = mid + 1
            ans = mid
    print(ans if ans != None else -1)