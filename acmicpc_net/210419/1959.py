import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

################################################################
# answer 02
###########################################################
def lastSnail(m, n):
    if m == 2:
        return 2
    if n == 2:
        return 3
    
    if m == 1:
        return 0
    if n == 1:
        return 1
    
    return 0

if __name__ == '__main__':
    m, n = map(int, input().split())
    
    # 완전탈피횟수(ecdysisCnt)가 아래와 같은 이유는 
    # m과 n 중에 최솟값이 행과 열을 2칸씩 없앴을 때 가장 빨리 0으로 수렴하는 값이기 때문이다.
    ecdysisCnt = min(m, n) // 2
    m -= ecdysisCnt * 2
    n -= ecdysisCnt * 2

    # 이 케이스에 걸리는 경우는 완전탈피횟수(ecdysisCnt)만큼 돌았을때 
    # lastSnail 배열이 완전히 소멸되는 경우이다. 
    # 따라서, lastSnail 함수로 처리할 배열을 남겨두기 위해 한 단계 backing한다고 생각하면 쉽다.
    if m == 0 or n == 0:    
        ecdysisCnt -= 1
        m , n = m + 2, n + 2
    
    # 완전탈피 1번을 수행했을때, 총 4개의 커브 포인트가 생긴다. 
    # 거기에 완전탈피를 할 수 없는 경우(lastSnail)를 따져 결과에 더하면 답이 된다.
    # 그리고 수행 후 나의 위치는 (이전위치_ROW + 1, 이전위치_COL + 1) 이 된다. 
    curveCnt = 4 * ecdysisCnt + lastSnail(m, n)
    r, c = 1, 1
    r, c= r + ecdysisCnt, c + ecdysisCnt

    # ※ PR 참고
    if m == 2 or n == 2:
        r += 1
    if m == 1:
        c += n - 1
    if n == 1:
        r += m - 1
    
    print(curveCnt)
    print(r, c)

################################################################
# answer 01  (이해 개빡세당...)
###########################################################
'''
if __name__ == '__main__':
    m, n = map(int, input().split())
    res = (min(m, n) - 1) * 2 + (1 if(m > n) else 0)

    print(res)
    if m == n:
        if m % 2 == 1:  # 1. m = 5, n = 5
            print((m - 1) // 2 + 1, (m - 1) // 2 + 1)
        else:
            print(m // 2 + 1, m // 2)
    else:
        if n > m:
            if m % 2 == 0:
                print(m // 2 + 1, m // 2)
            else:   # 2
                print((m - 1) // 2 + 1, (m - 1) // 2 + 1 + n - m)
        else:
            if n % 2 == 0:  # 3
                print(n // 2 + 1, n // 2)
            else:   # 1
                print((n - 1) // 2 + 1 + m - n, (n - 1) // 2 + 1)
'''
################################################################
# my solution (Pypy3 시간 초과, Python3 시간 초과)
###########################################################
'''
if __name__ == '__main__':
    m, n = map(int, input().split())
    border = [n, m - 1, n - 1, m - 2]
    dir = 0
    cnt = 0
    res = 0
    x, y = 0, -1
    
    while True:
        cnt += border[dir]
        if dir % 2 == 0:
            y += (1 if (dir == 0) else -1) * border[dir]
        else:
            x += (1 if (dir == 1) else -1) * border[dir]

        print(border)
        if cnt >= m * n: break
        border[dir] -= 2
        dir += 1
        if dir == 4: dir = 4 - dir
        res += 1

    print(res)
    print(x + 1, y + 1)
'''