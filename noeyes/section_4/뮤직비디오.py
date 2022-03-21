import os , sys

os.system('clear')
sys.stdin=open("noeyes/section_4/뮤직비디오.txt", "rt")

def CheckNeedDVD():

  dvd = []
  count = 0 

  for i in arr:
    if(sum(dvd) + i <= mid):
      dvd.append(i)
    else:
      dvd = [i]
      count += 1

  count += 1
  return count
    

n, m = map(int,input().split())
arr = list(map(int,input().split()))

SUM = sum(arr)
lt = 1
rt = SUM
result = 0
while lt <= rt:

  mid = int((lt + rt) // 2 + 0.5)
  if(mid < max(arr)):
    continue
  
  if(mid * m >= SUM):
    
    count = CheckNeedDVD()

    if(count == m):
      result = mid
      rt = mid - 1  
    elif(count > m):
      lt = mid + 1      
    else:
      rt = mid - 1
  else:
    lt = mid + 1

print(result)