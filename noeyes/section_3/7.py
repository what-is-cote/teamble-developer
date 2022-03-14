import os , sys

os.system('clear')
sys.stdin=open("noeyes/section_3/7.txt", "rt")

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
count = 0
for i in range(n):

  if(i <= n//2):
    for j in range(n//2 - i, n//2 + i+1):
       count += arr[i][j]
  
  else:
    for j in range(n//2 - (n-i -1), n//2 + (n-i-1) + 1):
       count += arr[i][j]

print(count)