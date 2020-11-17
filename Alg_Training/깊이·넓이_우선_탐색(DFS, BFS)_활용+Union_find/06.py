import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
def DFS(S, E):
    global res, cnt
    if(E > len(N)):
        return
    if(E == len(N)):
        cnt += 1
        for e in res:
            print(e, end='')
        print()
        return
    else:
        z = 0
        if(E + 1 < len(N) and (N[E + 1] == '0' or N[E] == '0')):
            z += 1
        t = int(N[E:E + z + 1])
        res.append(chr(t + 64))
        if(1 <= t <= 26):
            DFS(E, E + 1)
        res.pop()
        
        t = int(N[E:E + z + 2])
        res.append(chr(t + 64))
        if(1 <= t <= 26):            
            DFS(E, E + 2)
        res.pop()

if __name__ == "__main__":
    N = input()
    res = []
    cnt = 0
    
    DFS(0, 0)
    print(cnt)
'''
################################################################################
def DFS(L, P):
    global cnt
    if L == N:
        cnt += 1
        for j in range(P):
            print(chr(res[j] + 64), end='')
        print()
        return
    else:
        for i in range(1, 27):
            if(code[L] == i):
                res[P] = i
                DFS(L + 1, P + 1)
            elif ((i >= 10) and (code[L] == i // 10 and code[L + 1] == i % 10)):
                res[P] = i
                DFS(L + 2, P + 1)


if __name__ == '__main__':
    code = list(map(int, input()))
    N = len(code)
    code.insert(N, -1)
    res = [0] * (N + 3)
    cnt = 0
    DFS(0, 0)
    print(cnt)