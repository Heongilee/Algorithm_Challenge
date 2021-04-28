# 백준 1213번
# https://www.acmicpc.net/problem/1213
import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")

if __name__ == '__main__':
    t = list(input())
    dic = dict()
    res = ["_"] * len(t)

    for e in t:
        dic[e] = dic.get(e, 0) + 1

    lt, rt = 0, len(t) - 1
    i = 65
    while lt < rt:
        if i > 90: break

        alpha = chr(i)
        while dic.get(alpha, 0) >= 2:
            res[lt] = alpha
            lt += 1
            res[rt] = alpha
            rt -= 1
            dic[alpha] = dic.get(alpha, 0) - 2
            if dic.get(alpha, 0) == 0: del dic[alpha]
        i += 1

    for i in range(65, 91):
        alpha = chr(i)
        if dic.get(alpha, 0) % 2 != 0:
            res[lt] = alpha
            dic[alpha] = dic.get(alpha, 0) - 1
            if dic.get(alpha, 0) == 0: del dic[alpha]
            break

    if len(dic) != 0:
        print("I'm Sorry Hansoo")
        sys.exit(0)

    print(''.join(res))