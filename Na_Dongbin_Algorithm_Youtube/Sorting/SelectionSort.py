import sys
sys.stdin = open("./Na_Dongbin_Algorithm_Youtube/input.txt", "rt")

if __name__ == "__main__":
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(arr)):
        midx = i  #최소값
        for j in range(i, len(arr)):
            if(arr[j] < arr[midx]):
                midx = j
        arr[i], arr[midx] = arr[midx], arr[i]
    print(arr)

