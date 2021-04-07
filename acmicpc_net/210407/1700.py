import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    plug = [0] * n
    cnt = 0
    
    for i in range(k):
        # 범위안에 있으며, 빈 플러그를 찾을동안 또는 이미 꽃은 플러그가 있는지 찾을동안 증가.
        j = 0
        while j < n and plug[j] != 0 and plug[j] != arr[i]: j += 1

        # 플러그에 자리가 없으면
        if j == n:      
            # 1순위 : 다시 사용되지 않는 플러그를 우선적으로 뽑음
            cnt += 1
            for r in range(n):
                if plug[r] not in arr[i + 1:]:
                    plug[r] = arr[i]
                    break
            else:
                # 2순위 : 꽃혀있는것들 중 가장 나중에 사용되는 것을 뽑음
                target_idx = -1 # 플러그 리스트 중 가장 나중에 사용될 플러그의 인덱스가 저장됨.
                dis = 0
                for s in range(n):
                    for t in range(i + 1, k):
                        if plug[s] == arr[t]:
                            # plug 원소 중 dis길이가 가장 긴 target_idx를 찾는 과정.
                            if t - i > dis:
                                dis = t - i
                                target_idx = s
                            break
                plug[target_idx] = arr[i]
            continue
        if plug[j] == arr[i]:  continue  # 꽃으려고 하는 플러그가 있으면 건너 뜀.
        plug[j] = arr[i]

    print(cnt)