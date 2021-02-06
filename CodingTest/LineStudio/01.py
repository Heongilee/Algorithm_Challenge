import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
import heapq as hq

def incDate(m, d):
    endDate = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #1월부터 12월 말일
    d += 1
    if(d > endDate[m]):
        d = 1
        m += 1
    return m, d

def incPos(sx, sy):
    sy += 1
    if(sy > 6):
        sy = 0
        sx += 1
    return sx, sy
    
def solution(holidays, k):
    board = [[0] * 7 for _ in range(60)]
    pq = []
    res = 0

    for h in holidays:
        sx, sy = 0, 5
        cm, cd = 1, 1
        mon, dat = map(int, h.split("/"))
        while(mon != cm or dat != cd):
            # 현재 날짜 카운트
            cm, cd = incDate(cm, cd)
            # 캘린더 카운트
            sx, sy = incPos(sx, sy)
            if(sy == 0 or sy == 6):
                board[sx][sy] = 1
        board[sx][sy] = 1
    
    x, y = 0, 0
    while(x < 60):
        if(board[x][y] == 1):
            cnt = 0
            while(board[x][y] == 1):
                cnt += 1
                x, y = incPos(x, y)
            if any (e == -cnt for e in pq):
                continue
            else:
                hq.heappush(pq, -cnt)
        else:
            x, y = incPos(x, y)

    # 최대힙을 이용해 k번째 휴일 결과에 담기.
    for _ in range(k):
        res = -hq.heappop(pq)
    return res
    
if __name__ == '__main__':
    #              ['Thu', 'Fri', 'Mon', 'Fri', 'Sat', 'Fri', 'Mon', 'Wen', 'Sun']
    res = solution(["01/14","01/15","01/18","01/22","01/23","01/29","02/01","02/03","02/07"], 1)
    print(res)
    res = solution(["01/14","01/15","01/18","01/22","01/23","01/29","02/01","02/03","02/07"], 2)
    print(res)
    res = solution(["01/14","01/15","01/18","01/22","01/23","01/29","02/01","02/03","02/07"], 3)
    print(res)
    res = solution(["01/14","01/15","01/18","01/22","01/23","01/29","02/01","02/03","02/07"], 4)
    print(res)
    res = solution(["01/14","01/15","01/18","01/22","01/23","01/29","02/01","02/03","02/07"], 5)
    print(res)