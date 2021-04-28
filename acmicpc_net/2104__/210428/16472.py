import sys
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

####################################################################
# other solution
###############################################################
'''
if __name__ == '__main__':
    n = int(input())
    string = input().rstrip()

    chk = [0] * 26      # 알파벳 개수 체크 리스트
    L = len(string)     
    lt, rt = 0, 0       # 투 포인터
    charCnt = 0         # 중복되지 않은 문자열 갯수
    res = None          # 최대 문자열 길이
    dq = deque()        # 인식한 문자열이 큐에 쌓임.

    while lt < L and rt < L:
        # rt
        while rt < L:
            if charCnt == n and not chk[ord(string[rt]) - ord('a')]:
                break
            if not chk[ord(string[rt]) - ord('a')]:
                charCnt += 1
            chk[ord(string[rt]) - ord('a')] += 1
            dq.append(string[rt])
            rt += 1

        res = max(res, len(dq)) if res != None else len(dq)

        # lt
        front = dq[0]
        chk[ord(front) - ord('a')] -= 1
        dq.popleft()
        if not chk[ord(front) - ord('a')]:
            charCnt -= 1
        lt += 1
    print(res)
'''
    
####################################################################
# my solution 02 (AC)
###############################################################
if __name__ == '__main__':
    n = int(input())
    string = input().rstrip()
    arr = []
    res = None

    # arr 만들기
    i = 0
    while i < len(string):
        c = string[i]
        p = i
        while p < len(string) and string[p] == c: p += 1
        arr.append((c, p - i))
        i = p
    
    for i in range(len(arr)):
        S = set()
        p = i
        cnt = 0
        while p < len(arr):
            S.add(arr[p][0])
            if len(S) > n:
                S.remove(arr[p][0])
                break
            cnt += arr[p][1]
            p += 1
        res = max(res, cnt) if res != None else cnt
    print(res)

####################################################################
# my solution 01 (78% TLE)
###############################################################
'''
if __name__ == '__main__':
    n = int(input())
    string = input()
    res = None
    for i in range(len(string)):
        S = set()
        p = i
        cnt = 0
        while p < len(string):
            S.add(string[p])
            if len(S) > n:
                S.remove(string[p])
                break
            cnt += 1
            p += 1
        
        res = max(res, cnt) if res != None else cnt
    print(res)
'''