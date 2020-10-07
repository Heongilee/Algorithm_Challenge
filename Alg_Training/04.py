import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
'''
Case #01 : Success
Case #02 : Success
Case #03 : Success
Case #04 : Success
Case #05 : Success

점수 결과 : 100
-----------------------------------------------------------------------
time_space_table:
  d1.in : mem=4604k time=34ms
  d2.in : mem=4608k time=153ms
  d3.in : mem=4608k time=1927ms
  d4.in : mem=4608k time=55ms
  d5.in : mem=4608k time=1910ms
  d6.in : mem=4608k time=1923ms
  d7.in : mem=4608k time=1922ms
  d8.in : mem=4608k time=1929ms
  d9.in : mem=4612k time=1925ms
 d10.in : mem=4624k time=1930ms
 << 정보올림피아드 문제 1382번 (4MB, 1000ms 제한)
'''

def DFS(tot, S):
    global cnt
    # 남은 동전들을 다 더해봤을 때 T를 못 만들겠다면, 가지를 계속 뻗어나갈 필요가 없다.
    if(tot + sum(map(lambda x: x[0] * x[1], v[S:])) < T):
        return
    # if(tot > T):
    #     return
    if(tot == T):
        cnt += 1
    else:
        for i in range(S, K):
            if(v[i][1] != 0):
                v[i][1] -= 1
                # v[i] = v[i][:1] + (v[i][1] - 1, )
                DFS(tot + v[i][0], i)
                v[i][1] += 1
                # v[i] = v[i][:1] + (v[i][1] + 1, )
                
if __name__ == '__main__':
    T = int(input())
    K = int(input())
    v = [] #(동전의 종류, 동전의 개수)
    cnt = 0
    for _ in range(K):
        pi, ni = map(int, input().split())
        v.append([pi, ni])
    v.sort(reverse=True)
    
    DFS(0, 0)
    print(cnt)
#######################################################################################
'''
Case #01 : Success
Case #02 : Time Limit Exceeded
Case #03 : Time Limit Exceeded
Case #04 : Success
Case #05 : Success

점수 결과 : 60
----------------------------------------------------------------------------
time_space_table:
  d1.in : mem=4568k time=72ms
  d2.in : mem=4572k time=920ms
  d3.in : mem=4576k time=1890ms
  d4.in : mem=4576k time=163ms
  d5.in : mem=4576k time=1919ms
  d6.in : mem=4576k time=1942ms
  d7.in : mem=4576k time=1924ms
  d8.in : mem=4576k time=1923ms
  d9.in : mem=4576k time=1917ms
 d10.in : mem=4576k time=1917ms
 << 정보올림피아드 문제 1382번 (4MB, 1000ms 제한)
'''
'''
def DFS(L, tot):
    global cnt
    # if(tot + sum(map(lambda idx:P[idx] * N[idx], range(L, k))) < t):
    #     return
    if(tot > t):
        return
    if(L == k):
        if(tot == t):
            cnt += 1
        return
    else:
        for i in range(N[L] + 1):
            DFS(L + 1, tot + (P[L] * i))
    
if __name__ == '__main__':
    t = int(input())
    k = int(input())
    P = list()  # 동전의 종류
    N = list()  # 동전의 개수
    cnt = 0
    for _ in range(k):
        pi, ni = map(int, input().split())
        P.append(pi)
        N.append(ni)
    DFS(0, 0)
    print(cnt)
'''