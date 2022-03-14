import os
import sys
os.system('clear')
sys.stdin=open("section_2/2.txt", "rt")

T = int(input())

# for i in range(0,T):
#   N, s, e, k =map(int,input().split())
#   arr = list(map(int,input().split()))
  
#   for j in range(s-1,e):
#     for l in range(j+1, e+1):
#       if(arr[j] > arr[l]):
#         arr[l] , arr[j] = arr[j], arr[l]

#   print('#%d %d' %(i+1,arr[k-1+s-1]))

for i in range(0, T):
  N, s, e, k =map(int,input().split())
  arr = list(map(int,input().split()))
  arr = arr[s-1:e]
  arr.sort()
  
  print('#%d %d' %(i+1,arr[k-1]))

