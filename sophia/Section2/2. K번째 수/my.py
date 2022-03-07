import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

t = int(input())

for i in range(1, t+1):
        n,s,e,k = map(int, input().split())
        input_list = list(map(int, input().split()))
        slice_list = input_list[s-1:e]
        slice_list.sort()
        print('#' + str(i) + ' ' + str(slice_list[k-1]))