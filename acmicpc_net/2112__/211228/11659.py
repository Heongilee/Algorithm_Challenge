import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

# i번째 까지의 합 구하기
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result

def update(i, diff):
    while i <= n:
        tree[i] += diff
        i += (i & -i)

def interval_sum(lt, rt):
    return prefix_sum(rt) - prefix_sum(lt - 1)
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    tree = [0] * (n + 1)
    
    # build tree
    for i in range(1, n + 1): update(i, arr[i])
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        # a부터 b까지 구간 합 구하기
        r = interval_sum(a, b)
        print(r)