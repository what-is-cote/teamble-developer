from re import T
import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

L = int(input())
height = list(map(int, input().split()))
M = int(input())

height.sort(reverse=True)

for i in range(M):
    height[0] -= 1
    height[L-1] += 1
    if height[0] < height[1] or height[L-1] > height[L-2]:
        height.sort(reverse=True)
        
print(height[0] - height[L-1])