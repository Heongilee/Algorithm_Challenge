import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def DFS(x):
    if(x > 0):  # Base case
        DFS(x - 1)
        print(x, end=' ')

# main 함수 영역임을 의미 -> 딱히 별 의미 없음.
if __name__ == "__main__":
    N = int(input())
    DFS(N)