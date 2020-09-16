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