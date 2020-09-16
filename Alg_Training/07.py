import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
Case #01 : Success
Case #02 : Success
Case #03 : Success
Case #04 : Time Limit Exceeded
Case #05 : Time Limit Exceeded

점수 결과 : 60
'''

'''
def DFS(L):
    global minimum
    global flag
    if(L > minimum):
        res.pop()
        return
    if(sum(res) > M):
        res.pop()
        return
    if(sum(res) == M):
        if(L < minimum):
            minimum = L
            flag = True
        res.pop()
        return
    else:
        for i in range(len(a)):
            res.append(a[i])
            DFS(L + 1)
            if(flag == True):
                flag = False
                break
        if(len(res) != 0):
            res.pop()
        return
        
if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    M = int(input())
    flag = False    # leaf node에서 1, 2, 5중 하나에서 minimum이 만들어졌다면 나머지는 볼 필요 없다.
    minimum = 2147000000
    res = []
    DFS(0)
    print(minimum)
'''
############################################################################
def DFS(L, sum):
    global min
    if(sum > M):
        return
    if(L > min):
        return
    if(sum == M):
        if(L < min):
            min = L
        return
    else:
        for c in a:
            DFS(L + 1, sum + c)
            

if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    M = int(input())
    min = 2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(min)