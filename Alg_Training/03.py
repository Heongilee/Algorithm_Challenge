import sys
import time
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
###############################################
# Top-down 방식
##########################################
'''
def DFS(h):
    # cut-edge
    if(D[h] > 0):
        return D[h]
    if(h == 1 or h == 2):
        return h
    else:
        D[h] = DFS(h - 1) + DFS(h - 2)
        return D[h]
    
if __name__ == "__main__":
    N = int(input())
    D = [0] * (N + 1)
    
    res = DFS(N)
    print(res)
'''
#########################################################################
# Bottom-up 방식
##########################################
if __name__ == "__main__":
    N = int(input())
    D = [0] * (N + 1)
    
    D[1] = 1
    D[2] = 2
    
    for len in range(3, N + 1):
        D[len] = D[len - 1] + D[len - 2]
    print(D[N])