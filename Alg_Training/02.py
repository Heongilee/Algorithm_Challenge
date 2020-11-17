import sys
import time
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")
sys.setrecursionlimit(10 ** 6)

def DFS(len):
    # cut-edge : 이미 메모리제이션된 값을 참조할 경우, 바로 값을 리턴할 것.
    if(D[len] > 0):
        return D[len]
    if(len == 1 or len == 2): # 종착점 : 직관적으로 알 수 있는 충분히 작은 문제의 해
        return len
    else:
        # 점화식
        D[len] = DFS(len - 1) + DFS(len - 2)
        return D[len]
    
if __name__ == "__main__":
    start_time = time.time()
    N = int(input())
    D = [0] * (N + 1)
    res = DFS(N) # Memorization Table
    print(res)
    end_time = time.time()
    print(f"time: {round(end_time - start_time, 10)} sec")
#####################################################################
