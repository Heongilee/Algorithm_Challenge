import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
input = sys.stdin.readline

def timeAdder(mi, se):
    global h, m, s

    s += se
    if s >= 60:
        tmp, s = s // 60, s % 60
        m += tmp
    
    m += mi
    if m >= 60:
        tmp, m = m // 60, m % 60
        h += tmp

def timeCompare(h1, m1, s1, h2, m2, s2):
    # 1이 더 크면 True 같거나 아니면 False
    if h1 > h2:
        return True
    elif h1 == h2:
        if m1 > m2:
            return True
        elif m1 == m2:
            if s1 > s2:
                return True
            elif s1 == s2:
                return False
            else:   #s1 < s2
                return False
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    n, time= input().split()
    n = int(n)
    myHour, myMinute, mySecond = map(int, time.split(":"))
    playList = [list(map(int, input().split(":"))) for _ in range(n)]
    res = []

    for i in range(n):
        h, m, s = 0, 0, 0
        cnt = 0
        p = i
        while p < n and timeCompare(myHour, myMinute, mySecond, h, m, s):
            timeAdder(playList[p][0], playList[p][1])
            p += 1
            cnt += 1
        '''
        # max값 계산
        if timeCompare(myHour, myMinute, mySecond, h, m, s):
            continue
        '''
        res.append((h, m, s, cnt, i + 1))
    
    if any (myHour == h1 and myMinute == m1 and mySecond == s1 for h1, m1, s1, *etc in res):
        res.sort(key=lambda x : (x[0], x[1], x[2], -x[3]))
        for i in range(len(res)):
            if myHour == res[i][0] and myMinute == res[i][1] and mySecond == res[i][2]:
                res = res[i:]
                break
    else:
        res.sort(key=lambda x: -x[3])
    
    print(res[0][3], res[0][4])