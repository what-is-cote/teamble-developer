import os
import sys
os.system('clear')
sys.stdin=open("section_2/3.txt", "rt")

N, K = map(int,input().split())
arr = list(map(int,input().split()))
result = set()

for i in range(0,N-K+1):
  for j in range(i+1, N-K+1+2):
    for k in range(j+1, N-K+3):
      result.add(arr[i]+arr[j]+arr[k])

result = list(result)
result.sort(reverse=True)

print(result[K-1])


