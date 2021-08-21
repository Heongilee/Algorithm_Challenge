import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())    # 1 <= N, M <= 100,000
    myList = [input().rstrip() for _ in range(n)]
    pkmon1 = dict(zip(range(1, n + 1) , myList))
    pkmon2 = dict(zip(myList , range(1, n + 1)))
    
    for _ in range(m):
        query = input().rstrip()
        if query.isdigit():
            print(pkmon1.get(int(query)))
        else:
            print(pkmon2.get(query))