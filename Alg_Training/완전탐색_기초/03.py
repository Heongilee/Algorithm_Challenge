import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

# 숫자 N의 부분집합 개수는 2^N - 1(공집합 제외)개이다.
def DFS(v):
    if(v == N + 1):
        for i in range(1, len(ch)):
            if(ch[i] != 0):
                print(i, end=' ')
        print()
        return
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)
        
    
# Python에서 main의 기능
# Array나 list의 원소를 함수를 통해 접근 가능
# Main 함수에서 선언한 지역변수를 함수를 통해 접근 가능
if __name__ == "__main__":
    N = int(input())
    ch = [0] * (N + 1)
    DFS(1)