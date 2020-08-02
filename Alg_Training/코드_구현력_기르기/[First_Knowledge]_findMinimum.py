arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')   #파이썬에서 사용가능한 가장 큰 값으로 초기화 됨.
arrMin = arr[0]

for i in range(len(arr)):
    if(arr[i] < arrMin):
        arrMin = arr[i]
