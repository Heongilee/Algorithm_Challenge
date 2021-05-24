# 유사 딕셔너리 DEFAULTDICT() 활용법
#   defaultdict()의 인자로 주어진 객체(default-factory)의 기본값을 딕셔너리의 초기값으로 지정가능함.
#   숫자, 리스트, 셋등으로 초기화 할 수 있어 여러 용도로 쓰인다.

from collections import defaultdict

# 디폴트값이 0(정수)인 딕셔너리 선언
int_dict = defaultdict(int)
print(type(int_dict))           # <class 'collections.defaultdict'>
print(int_dict)                 # defaultdict(<class 'int'>, {})

# 값을 지정하지 않은 키는 그 값이 0으로 된다.
print(int_dict['key1'])         # 0

# 값을 지정하면 그 값이 지정된다.
int_dict['key2'] = 'value2'
print(int_dict['key2'])         # value2

# 디폴트값이 빈 리스트인 딕셔너리 선언
list_dict = defaultdict(list)
print(type(list_dict))
print(list_dict)

print(list_dict['key1'])        # []

list_dict['key2'] = 'value2'
print(list_dict)                # defaultdict(<class 'list'>, {'key1': [], 'key2': 'value2'})

# 디폴트값이 빈 셋인 딕셔너리
set_dict = defaultdict(set)
print(set_dict)

print(set_dict['key1'])         # set()

set_dict['key2'] = 'value2'
print(set_dict)                 # defaultdict(<class 'set'>, {'key1': set(), 'key2': 'value2'})