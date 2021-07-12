import sys, itertools as it
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
'''
리눅스 eof ctrl + D
윈도우 eof ctrl + Z

5
3 1 4 3 2 
(ctrl + D)

32
'''
print(sum(list(it.accumulate(sorted(list(map(int, [*open(0)][1].rstrip().split())))))))

