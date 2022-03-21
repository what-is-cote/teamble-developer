import os , sys

# os.system('clear')
# sys.stdin=open("noeyes/section_4/4.마구간정하기.txt", "rt")

def CheckDistance(d):
  count = 1
  lt = 0
  rt = lt + 1

  while rt < n - 1:

    if (d <= huts[rt] - huts[lt]):
      count += 1
      lt = rt
      rt = lt + 1 
    else: 
      rt += 1
  
  return count

n, c = map(int,input().split())
huts = []
for i in range(n):
  huts.append(int(input())) 

huts.sort()
lt = huts[0]
rt = huts[n-1]
result = 0
while lt <= rt:
  
  d = int((lt + rt) / 2 + 0.5)
  count = CheckDistance(d)
  if count >= c:
    result = count  
    lt = d + 1
  else:
    rt = d - 1

print(result)