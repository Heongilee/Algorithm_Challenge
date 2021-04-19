import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

################################################################
# answer (이해 개빡세당...)
###########################################################
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