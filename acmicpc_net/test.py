#################################################################
# Swapping Algorithm without tmp
############################################################
'''
def solution(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == '__main__':
    a = 214748
    b = 356419

    print("Before:\t", a, b)
    a, b = solution(a, b)
    print("After:\t", a, b)
'''
#################################################################
# *, ** means
############################################################
'''
def f2(**kwargs):
    print(kwargs, type(kwargs))
    print(kwargs.keys())
    print(kwargs.values())

    for K, V in kwargs.items():
        print("Key :", K, ", Value :", V)

f2(K1 = "V1", K2 = "V2", K3 = "V3", K4 = "V4")
'''
#################################################################
# Priority Queue
############################################################
'''
from queue import PriorityQueue

if __name__ == '__main__':
    pq_infiniteSize = PriorityQueue()   # 사이즈가 무한대인 빈 우선순위 큐 생성
    pq_maximumSize = PriorityQueue(maxsize=5)   # 사이즈가 6인 빈 우선순위 큐 생성

    # TIP: 정렬기준을 바꾸고자 한다면 아래와 같이 데이터 구조를 저장해보자!
    # (우선순위, 값)
    pq_maximumSize.put((3, 'L'))
    pq_maximumSize.put((0, 'A'))
    pq_maximumSize.put((2, 'P'))
    pq_maximumSize.put((4, 'E'))
    pq_maximumSize.put((1, 'P'))

    # 출력문
    for i in range(5):
        t = pq_maximumSize.get()[1]
        print(t, end='')
    print()
'''
#################################################################
# Test zone
############################################################
k = 'a' * 30

print(k)