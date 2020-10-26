# random 모듈을 rd로 명명하겠다.
import random as rd

'''
### 빈 리스트 생성 ###
empty_list_1 = [] #빈 리스트 생성 (1)
empty_list_2 = list() #빈 리스트 생성 (1)

print(empty_list_1)
print(empty_list_2)

### 리스트 초기화 ###
a = [1, 2 ,3, 4, 5]
print(a)
print(a[0])   #인덱스 참조

# for문을 이용한 참조
for i in range(5):
    print(a[i], end=' ')
print()
for e in a:
    print(e, end=' ')
print()

# range 함수를 이용한 리스트 초기화
b = list(range(1, 11))
print(b)

# 리스트 append시키기.
c = a + b
d = b + a
print(c)
print(d)

# 원소 append 시키기.
print(a)
a.append(6)
print(a)


# 원소 중간에 삽입하기
a.insert(3, 7)  # a 리스트의 3번 인덱스의 7을 삽입하는 것. 그 뒤의 값들은 뒤로 밀려난다.
print(a)

# 원소 빼내기
a.pop()     # 끝에 있는 원소 빼내기
print(a)

a.pop(3)    # 3번 인덱스의 원소 제거하고 뒤의 원소들은 앞으로 당기기
print(a)

# 특정 값을 찾아 삭제하고 싶을 때 리스트.remove(제거할_원소)
a.remove(4) # 4라는 값을 찾아서 삭제해라
print(a)

# 특정 값의 인덱스 번호를 출력하기
print(a.index(2))   # 2라는 값의 인덱스는 1번 인덱스에 있다.

'''
########################################################################################
'''
a = list(range(1, 11))  #a 리스트 초기화
print(a)

# 합, 최대, 최소
print(sum(a))   #a 리스트에 있는 모든 원소들의 합을 출력함.
print(max(a))   #a 리스트의 원소 중 최대값
print(min(a))   #a 리스트의 원소 중 최솟값
print(min(7, 5))    # [함수 오버로딩] 인자값들 중의 최솟값 -> 5 출력.

# random모듈의 Shuffle 함수 사용
print(a)
rd.shuffle(a)
print(a)

# 정렬하기 (Big-O : Nlog(N) )
a.sort()    # ascending
print(a)
a.sort(reverse=True)    # descending
print(a)

# 리스트의 값들을 모두 제거 -> 빈 리스트 출력
a.clear()
print(a)
'''
########################################################################################
# List comprehension

list1 = [i for i in range(1, 11) if i % 2 == 1]
print("list1 : ", list1)

#! 다음과 같은 2차원 배열 초기화는 각 행을 같은 객체로 인식하기 때문에 사용 시 주의해야함.
N = 5
M = 3
'''
list2 = [[0] * N] * M
print("Before list2 : ")
for l in list2:
    print(l)

list2[0][0] = 1
print("After list2 : ")
for l in list2:
    print(l)
'''

list3 = [[0] * N for _ in range(M)]
for l in list3:
    print(l)