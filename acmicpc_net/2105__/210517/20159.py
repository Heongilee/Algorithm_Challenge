import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


if __name__ == '__main__':
    
#############################################################################
# 3% TLE (Python 3)
########################################################################
'''
    if __name__ == '__main__':
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    res = None
    
    for p in range(1, n + 1, 2):
        prev = [arr[j] for j in range(1, p) if j % 2 != 0]
        under = [arr[-1]]
        next = [arr[j] for j in range(p, n) if j % 2 == 0]

        res = max(res, sum(prev + under + next)) if res != None else sum(prev + under + next)

    print(res)
'''
#############################################################################
# 3% TLE (Python 3)
########################################################################
'''
def DFS(L, card, jungHun): 
    global res

    # 카드 분배
    while card:
        if L <= 0 and card[0] < card[-1]:
            jungHun.append(card.pop())
            tmp = card.popleft()    # 재귀를 마치고 정훈이가 받아가야 할 카드
            DFS(L + 1, cp.deepcopy(card), cp.deepcopy(jungHun))
            card.append(jungHun.pop())
            jungHun.append(tmp)
            card.popleft()          # 상대가 받아가야할 카드
        else:
            jungHun.append(card.popleft())
            card.popleft()
        
    res = max(res, sum(jungHun)) if res != None else sum(jungHun)
    return

if __name__ == '__main__':
    n = int(input())
    card = deque(list(map(int, input().split())))
    res = None

    DFS(0, card, [])
    print(res)
'''