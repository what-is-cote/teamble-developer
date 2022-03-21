import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

start = 0
end = len(num) - 1
mid = (end + start) // 2

while(start <= end):
    if num[mid] == M:
        print(mid + 1)
        break
    elif num[mid] > M:
        end = mid - 1
    else:      
        start = mid + 1
    mid = (end + start) // 2
