import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

if __name__ == "__main__":
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if(arr[j - 1] > arr[j]): # 자기보다 큰 녀석을 만나면 앞으로 이동.
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else: # 자기보다 작은 데이터(j - 1)를 만나면 멈춤.
                break
    print(arr)