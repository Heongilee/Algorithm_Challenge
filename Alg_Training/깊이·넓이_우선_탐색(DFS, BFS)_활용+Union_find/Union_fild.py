import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
sys.setrecursionlimit(10 ** 6)

def find(x):
    if(x == parent[x]):
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    if(x != y):
        if(x < y):
            parent[y] = x
        else:
            parent[x] = y

def isSameParent(x, y):
    x = find(x)
    y = find(y)
    
    return True if (x == y) else False

if __name__ == '__main__':
    v, e = map(int, input().split())
    E = []
    visit = [0] * (v + 1)
    parent = list(range(v + 1))
    weight = 0
    
    for _ in range(e):
        u, v, w = map(int, input().split())
        E.append([u, v, w])
    
    E.sort(key=lambda x: x[2])
    
    for i in range(v - 1):
        if(not isSameParent(E[i][0], E[i][1])):
            union(E[i][0], E[i][1])
            weight += E[i][2]
    
    print(weight)
            
    
    