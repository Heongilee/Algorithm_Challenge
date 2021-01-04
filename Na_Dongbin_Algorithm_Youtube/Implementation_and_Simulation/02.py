import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt")
'''
def countOneSecond(h, m, s):
    S = []
    tmp = int(s)
    tmp += 1
    if(tmp // 10 == 0):
        S.append('0')
        S.append(str(tmp))
        s = "".join(S)
        S.clear()
    else:
        s = str(tmp)
    
    if(s == '60'):
        s = '00'
        tmp = int(m)
        tmp += 1
        if(tmp // 10 == 0):
            S.append('0')
            S.append(str(tmp))
            m = "".join(S)
            S.clear()
        else:
            m = str(tmp)

    if(m == '60'):
        m = '00'
        tmp = int(h)
        tmp += 1
        if(tmp // 10 == 0):
            S.append('0')
            S.append(str(tmp))
            h = "".join(S)
            S.clear()
        else:
            h = str(tmp)
    
    return h, m, s

if __name__ == "__main__":
    ch = '3'
    n = int(input())
    h = '00'
    m = '00'
    s = '00'
    cnt = 0

    while True:
        h, m, s = countOneSecond(h, m, s)
        if (ch in s) or (ch in m) or (ch in h):
            cnt += 1
        if int(h) == n and m == '59' and s == '59':
            break
        
    print(cnt)
'''
#####################################################################################
if __name__ == '__main__':
    time = [0, 0, 0]
    
    N = int(input())
    count = 0
    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    print(count)