import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def DFS(L, sum):
    if(sum > tot // 2):
        return
    if(L == N):
        if sum == (tot - sum):
            print("YES")
            sys.exit(0) # 프로그램을 아예 종료시켜 버리는 함수.
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)
    

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))
    tot = sum(a)
    DFS(0, 0)
    print("NO")