import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")
sys.setrecursionlimit(10 ** 6)
'''
def quickSort(arr, start, end):
    if(start >= end):
        return arr
    pivot = start
    lt = start + 1
    rt = end
    while(lt <= rt):
        # pivot보다 큰 데이터를 찾을때 까지 반복
        while(lt <= end and arr[lt] <= arr[pivot]):
            lt += 1
        # pivot보다 작은 데이터를 찾을때 까지 반복
        while(rt > start and arr[rt] >= arr[pivot]):
            rt -= 1

        # 엇갈렸다면, 작은 데이터(rt)와 피벗을 교체
        if(lt > rt):
            arr[rt], arr[pivot] = arr[pivot], arr[rt]
        # 엇갈리지 않았다면, 큰 데이터(lt)와 작은 데이터(rt)를 교체
        else:
            arr[lt], arr[rt] = arr[rt], arr[lt]
    quickSort(arr, start, rt - 1)
    quickSort(arr, rt + 1, end)

if __name__ == "__main__":
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    quickSort(arr, 0, len(arr) - 1)
    print(arr)
'''
###################################################################################
def quickSort(arr):
    # 리스트에 원소를 하나 이하로 가진다면, 종료
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 첫 번째 원소를 pivot으로 설정
    tail = arr[1:]  # pivot을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분은 pivot보다 작은 데이터들로 구성
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분은 pivot보다 큰 데이터들로 구성

    return quickSort(left_side) + [pivot] + quickSort(right_side)

if __name__ == "__main__":
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    res = quickSort(arr)
    print(res)
