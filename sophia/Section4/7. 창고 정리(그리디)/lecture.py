from re import T
import sys, os
# sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

L = int(input())
height = list(map(int, input().split()))
M = int(input())

height.sort()

for i in range(M):
    height[0] += 1
    height[L-1] -= 1
    height.sort() 
    
print(height[L-1] - height[0])