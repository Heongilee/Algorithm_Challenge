import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

def DFS(N):
    if(N == 0):
        return  # 그냥 함수를 종료시켜라 라는 의미.
    else:
        DFS(N // 2)
        print(N % 2, end='')
    return
    
if __name__ == "__main__":
    N = int(input())
    DFS(N)  #Depth First Search