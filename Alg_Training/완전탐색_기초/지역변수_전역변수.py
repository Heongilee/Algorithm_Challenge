import sys
sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

'''
#* 지역변수와 전역변수 *

* 함수 안에서 변수가 사용되면 그 변수가 먼저 함수의 지역변수인가를 확인한다.
* 만약, 함수안의 지역변수가 아니라면 메인 줄 이하에서 선언된 전역변수인가를 확인한다.
* 그래도 없다면 에러를 출력한다.
'''

def DFS1():
    print(N)
    #N = 6  #! 이 줄 하나 때문에 DFS1()은 N을 지역변수로 본다 -> 바로 윗 줄에서 생성하기도 전에 사용하려고 하기 때문에 에러 발생.
    print(N)
    return

def DFS2():
    if N == 5:
        #N = N + 1   #! 기존 값의 1을 더하는 명령도 '(변수) = ???'을 만나 지역변수를 생성한다고 본다. -> 윗 줄에서 에러 발생.
        print(N)
    return

def DFS2_sol():
    global N    # 이 줄로 이제 변수 생성을 해도 재사용되고 기존값의 1을 더하는 연산도 가능해진다 -> 전역변수라고 말했기 때문.
    if N == 5:
        N = N + 1
        print(N)
    return
def DFS3():
    array[0] = 0    #* 이 경우는 인덱스 참조 방식이기 때문에 리스트 변수의 생성과는 다르다.
    print(array)
    
def DFS3_sol():
    global array    #* 따라서, 전역변수임을 나타내주면 해결 가능하다.
    array = array + [4, 5]  #! 이 경우는 리스트 변수의 생성으로 보기 때문에 에러가 발생한다.
    print(array)
    
if __name__ == "__main__":
    N = 5   # main에서 초기화한 변수는 전역변수이다. 
    array = [1, 2, 3]
    DFS1()
    DFS2()
    DFS2_sol()
    DFS3()
    DFS3_sol()