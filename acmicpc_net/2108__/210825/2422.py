import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

#############################################################################################
# 100% AC (Pypy 3)
########################################################################################
def DFS(S, L):
    global cnt
    if L == 3:
        cnt += 1
        return
    for i in range(S, n + 1):
        if all (i not in comb[sack[j]] for j in range(len(sack))) and not chk[i]:
            chk[i] = True
            sack.append(i)
            DFS(i + 1, L + 1)
            sack.pop()
            chk[i] = False

if __name__ == '__main__':
    n, m = map(int, input().split())
    cnt = 0
    if n < 3:
        print(cnt)
    else:   
        sack = []
        chk = [None] + [False] * n
        comb = list([] for _ in range(n + 1))
        for _ in range(m):
            a, b = map(int, input().split())
            comb[a].append(b)
            comb[b].append(a)
        DFS(1, 0)
        print(cnt)


#############################################################################################
# 9% TLE (Pypy 3)
########################################################################################
'''
def createBitMasker(t):
    item = '0b' + ('0' * (n - 1)) + '1'
    item = int(item, 2) << (n - t)
    return item

def DFS(S, L):
    global chk, cnt
    if L == 3:
        if all (chk & t != t for t in myList):
            cnt += 1
        return
    for i in range(S, n + 1):
        t = createBitMasker(i)
        if chk & t != t:
            chk = chk | t
            DFS(i, L + 1)
            chk = chk ^ t

if __name__ == '__main__':
    n, m = map(int, input().split())    # 아이스크림 종류 n, 섞으면 안되는 조합 수 m
    myList = []
    cnt = 0
    for line in sys.stdin:
        a, b = map(int, line.rstrip().split())
        aa = createBitMasker(a)
        bb = createBitMasker(b)
        cc = aa | bb
        myList.append(cc)
    chk = int('0b' + ('0' * n), 2)
    DFS(1, 0)
    print(cnt)
'''

#############################################################################################
# 9% TLE (Pypy 3)
########################################################################################
'''
import itertools as it
if __name__ == '__main__':
    n, m = map(int, input().split())    # 아이스크림 종류 n, 섞으면 안되는 조합 수 m
    myList = [tuple(map(int, line.rstrip().split())) for line in sys.stdin]
    cnt = 0
    # [(1, 2), (3, 4), (1, 3)]

    for X in it.combinations(range(1, n + 1), 3):
        for a, b in myList:
            if a in X and b in X:
                break
        else:
            cnt += 1
    print(cnt)
'''