import sys
import itertools as it
import copy
sys.stdin = open("./AlgorithmAssets/input.txt", "rt")

class Itertools:
    # 메서드 파라미터 설명 ######################################
    # L : 상태 트리 depth (디폴트 0)
    # s : 조합 연산 시 재귀 안에서 for문 돌때 startIndex
    # pick : array에서 몇개의 원소를 뽑을건지
    ############################################################
    resultsSet = [] # 메서드 호출하고나면 이 안에 담긴다.
    # 생성자
    def __init__(self, array):
        self.array = array
        self.result = []
        self.chk = [False] * len(array)

        # 생성자 파라미터 추가시켜서 다음 메서드를 호출할 것.
        # self.duplicatePermutations(L, pick)
        # self.permutations(L, pick)
        # self.combinations(L, s, pick)
    
    # 중복 순열 출력하는 메서드
    def duplicatePermutations(self, L, pick):
        if L == pick:
            self.resultsSet.append(copy.deepcopy(self.result))
        else:
            for i in range(len(self.array)):
                self.result.append(self.array[i])
                self.duplicatePermutations(L + 1, pick)
                self.result.pop()
    
    # 순열 출력하는 메서드
    def permutations(self, L, pick):
        if L == pick:
            self.resultsSet.append(copy.deepcopy(self.result))
        else:
            for i in range(len(self.array)):
                if not self.chk[i]:
                    self.chk[i] = True
                    self.result.append(self.array[i])
                    self.permutations(L + 1, pick)
                    self.chk[i] = False
                    self.result.pop()

    # 조합 출력하는 메서드
    def combinations(self, L, s, pick):
        if L == pick:
            self.resultsSet.append(copy.deepcopy(self.result))
        else:
            for i in range(s, len(self.array)):
                self.result.append(self.array[i])
                self.combinations(L + 1, i + 1, pick)
                self.result.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())

    it = Itertools(list(range(1, n + 1)))
    # it.duplicatePermutations(0, 2)
    # it.permutations(0, 2)
    # it.combinations(0, 0, 2)
    print(it.resultsSet)


    