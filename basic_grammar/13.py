###################################################################################
# 1. 리스트에서 특정 값을 가지는 원소 모두 제거하기
'''
## 실행 결과 ##
[1, 2, 4]
'''
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 제거하고싶은 원소를 담은 집합 자료형

result = [i for i in a if i not in remove_set]
print(result)

###################################################################################
# 2. 사전(Dictionary) 자료형 다루기
'''
## 실행 결과 ##
{'사과': 'Apple', '바나나': 'Banana', '코코넛': 'Coconut'} , 딕셔너리에 "사과"가 존재합니다.
dict_keys(['사과', '바나나', '코코넛']) || ['사과', '바나나', '코코넛']
dict_values(['Apple', 'Banana', 'Coconut']) || ['Apple', 'Banana', 'Coconut']
'''
    # 두 리스트로 사전 자료형 초기화 하기
K = ["사과", "바나나", "코코넛"]
V = ["Apple", "Banana", "Coconut"]

result = dict(zip(K, V))
print(result, end=' , ')

    # 딕셔너리의 키 값 탐색하기
if "사과" in result:
    print("딕셔너리에 \"사과\"가 존재합니다.")

    # 키 리스트, 값 리스트로 분리시키기.
print(result.keys(), end=' || ')
print(list(result.keys()))
print(result.values(), end=' || ')
print(list(result.values()))

###################################################################################
# 3. 집합 자료형
# ** 데이터 조회 및 수정이 상수시간에 처리 가능.

# 초기화 방법 2 가지
'''
## 실행 결과 ##
{1, 2, 3}
{1, 2, 3, 4}
'''
set1 = set([1, 2, 2, 3, 3, 3])
print(set1)

set2 = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(set2)

# 집합에 단일 원소 추가
set2.add(5)
print(set2)

# 집합에 여러개 원소 추가
set2.update([6, 7])
print(set2)

###################################################################################
# 4. 빠르게 입력 받기
# ** Input이 많을 경우, 입력 받는것만으로도 많은 시간을 잡아먹는 경우가 있다.
# ** sys.stdin.readline() 함수를 통해 빠르게 입력받을 수 있다.
'''
sys.stdin.readline()
Hello World (엔터)

# 엔터키를 떼어냄.
sys.stdin.readline().rstrip()
Hello World
'''
'''
import sys
data = sys.stdin.readline().rstrip()

print(data)
'''
###################################################################################
# 5. f-string 출력
# ** Python 3.6 이상

answer = 7
print(f"정답은{answer}입니다.")
###################################################################################
# 6. Counter 라이브러리
# ** 등장 횟수를 카운트하는 라이브러리.
from collections import Counter

my_list = ['red', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'green']
counter = Counter(my_list)
print("counter['red'] : ", counter['red'])

dic_counter = dict(counter) # 사전 자료형으로 변환.
