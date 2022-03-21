import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

lt = 0
rt = N-1

while lt <= rt:
    mid = (rt+lt)//2
    if num[mid] == M:
        print(mid+1)
        break
    elif num[mid]>M:
        rt = mid-1
    else:      
        lt= mid+1

