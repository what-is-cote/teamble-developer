import os , sys

sys.stdin=open("noeyes/section_4/2.랜선자르기.txt", "rt")

def Count():
  count = 0
  for line in arr:
    count += line // length
  
  return count
os.system('clear')

k ,n = map(int,input().split())
arr = []
maximum = 0;

for i in range(k):
  temp = int(input())
  arr.append(temp)

maximum = max(arr)
lt = 1
rt = maximum

while lt <= rt:

  length = int((lt + rt) / 2 + 0.5)

  if Count() >= n:
    temp = length
    lt = length + 1
  
  else:
    rt = length - 1

print(length)