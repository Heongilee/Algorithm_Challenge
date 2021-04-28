# 백준 1541번
# https://www.acmicpc.net/problem/1541
#############################################################
# 내 풀이
########################################################
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
if __name__ == '__main__':
    buf = input()
    res = 0

    lt = 0
    rt = lt
    flag = False    # Minus flag

    while(rt < len(buf)):
        if(buf[rt].isdigit()):
            rt += 1
        else:
            res += (-1 if(flag) else 1) * int(buf[lt:rt])
            if(buf[rt] == '-'):
                flag = True
            rt += 1
            lt = rt

    res += (-1 if(flag) else 1) * int(buf[lt:rt])
    print(res)
#############################################################
# 저세상 풀이
########################################################
'''
if __name__ == '__main__':
    buf = input().split("-")
    res = 0

    for e in buf[0].split("+"):
        res += int(e)
    
    for e in buf[1:]:
        for ee in e.split("+"):
            res += -int(ee)
    print(res)
'''