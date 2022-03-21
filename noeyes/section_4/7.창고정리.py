from operator import indexOf
import os , sys
import re

# sys.stdin=open("noeyes/section_4/7.창고정리.txt", "rt")

n = int(input())
box = list(map(int,input().split()))
t = int(input())

box.sort(reverse=True)

s = 0
e = n-1
for i in range(t):
 
 box[s] -= 1
 box[e] += 1
 
 s = indexOf(box,max(box))
 e = indexOf(box,min(box))
 
print(box[s]-box[e])
 
