import sys
from collections import deque
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
INF = int(10e9)
def BFS(s):
    dq = deque()
    dq.append((s, ''))

    while dq:
        e, o = dq.popleft()

        if e == t:
            return o
        
        if 0 <= e * e <= INF and e * e not in chk:
            dq.append((e * e, o + "*"))
            chk.add(e * e)
        
        if 0 <= e + e <= INF and e + e not in chk:
            dq.append((e + e, o + "+"))
            chk.add(e + e)
        
        if 1 not in chk:
            dq.append((1, o + "/"))
            chk.add(1)

if __name__ == '__main__':
    s, t = map(int, input().split())
    chk = set()
    chk.add(s)

    if s == t:
        print(0)
    else:
        res = -1
        res = BFS(s)
        print(res if res != None else -1)

############################################################
# Time Limit... (5%)
#######################################################
'''
def DFS(e, o):
    global escape, res2
    if e < 1 or e > INF:
        return
    if e == t:
        res2 = o
        escape = True
        return
    else:
        if e != 1: DFS(e * e, o + "*")
        if escape: return
        DFS(e + e, o + "+")
        if escape: return
        # DFS(e - e, o + "-")
        # DFS(e // e, o + "/")

def BFS(v, opr):
    global res1
    dq = deque()
    dq.append((v, opr))

    while dq:
        e, o = dq.popleft()

        if e == t:
            break
        if e == 1:
            DFS(e, o)
        
        if e * e <= t:
            dq.append((e * e, o + "*"))
        if e + e <= t:
            dq.append((e + e, o + "+"))
        # dq.append((e - e, o + "-"))   # 얘는 왜 있는지 모르겠다...
        if e != 0: dq.append((e // e, o + "/"))

    res1 = o
    if res2 != "":
        return res1 if len(res1) < len(res2) else res2
    else:
        return res1

if __name__ == '__main__':
    s, t = map(int, input().split())
    escape = False
    res1 = ""
    res2 = ""

    if s == t:
        print(0)
    elif (t % s != 0 and t % 2 != 0) and (t != 1 and t != 0):
        print(-1)
    else:
        res = BFS(s, "")
        print(res)
'''