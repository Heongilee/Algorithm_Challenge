# import sys
# sys.stdin = open(".\\Alg_Training\\input.txt", "rt")

# N, M = map(int, input().split())

# # NxM의 0으로 초기화된 2차원 행렬
# a = [[0] * M for _ in range(N)]

# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         a[i - 1][j - 1] = i + j

# cnt_arr = []
# max_cnt = -1
# for elem in range(2, N + M + 1):
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if(elem == a[i][j]):
#                 cnt += 1
#     item = (elem, cnt)
#     cnt_arr.append(item)
#     if(cnt > max_cnt):
#         max_cnt = cnt

# for n, cnt in cnt_arr:
#     if(cnt == max_cnt):
#         print(n, end=' ')
##############################################################################
N, M = map(int, input().split())
