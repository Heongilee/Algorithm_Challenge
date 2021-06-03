import sys
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())    # 1 ≤ K < N ≤ 500,000
    digits = deque(list(input().rstrip()))
    S = []
    cnt = 0

    while digits:
        t = int(digits.popleft())

        while cnt < k and S and S[-1] < t:
            S.pop()
            cnt += 1
        S.append(t)
    print("".join(map(str, S[:n - k])))
###################################################################
# 5% TLE 
#
# TODO : 반례 찾기
##############################################################
'''
if __name__ == '__main__':
    n, k = map(int, input().split())    # 1 ≤ K < N ≤ 500,000
    digits = list(input().rstrip())

    lt = 0
    mid = lt + k
    rt = n - 1
    maxV = max(digits)
    cnt = 0

    while lt <= rt:
        if cnt >= k: break
        if digits[lt] == str(maxV): break
        lt += 1
        cnt += 1
    
    digits = digits[lt:rt + 1]
    if cnt >= k:
        print("".join(digits))
    else:
        pq = sorted(digits)
        
        while cnt < k:
            digits.remove(pq.pop(0))
            cnt += 1
        print("".join(digits))
'''