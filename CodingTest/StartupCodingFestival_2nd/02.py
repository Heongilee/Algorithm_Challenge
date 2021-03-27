import sys
sys.stdin = open("./CodingTest/input.txt", "rt")
input = sys.stdin.readline

def findParent(e):
    if(e != parent[e]):
        parent[e] = findParent(parent[e])
    return parent[e]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)

    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

if __name__ == '__main__':
    n = int(input())
    city = dict()  #key : 지역 이름, value : 인덱스
    graph = []

    idx = -1
    for _ in range(n):
        a, b, w = input().split()
        graph.append((a, b, int(w)))

        if city.get(a, -1) == -1:
            city[a] = city.get(a, idx) + 1
            idx += 1
        if city.get(b, -1) == -1:
            city[b] = city.get(b, idx) + 1
            idx += 1
    
    graph.sort(key=lambda x:x[2])
    parent = list(range(len(city)))
    cost = 0
    for a, b, w in graph:
        a = city.get(a)
        b = city.get(b)
        if findParent(a) != findParent(b):
            unionParent(a, b)
            cost += w
        
    print(cost)