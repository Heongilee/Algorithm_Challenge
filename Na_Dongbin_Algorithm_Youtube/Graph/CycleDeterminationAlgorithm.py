import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

def findParent(e):
    if(e != P[e]): # Path Compression
        P[e] = findParent(P[e])
    return P[e]

def unionParent(a, b):
    global Cycle
    a = findParent(a)
    b = findParent(b)

    # 두 노드의 부모노드가 이미 같다면, 사이클이 존재한다는 뜻이다. 
    if(a == b):
        Cycle = True

    if(a < b):
        P[b] = a
    else:
        P[a] = b

if __name__ == "__main__":
    Cycle = False
    v, e = map(int, input().split())
    P = list(range(v + 1))
    
    # e개의 간선 정보를 받아 Union 연산을 취함.
    for _ in range(e):
        a, b = map(int, input().split())
        unionParent(a, b)
    
    print(P, "cycle?: ", Cycle)