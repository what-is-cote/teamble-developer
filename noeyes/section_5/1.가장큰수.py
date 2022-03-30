import os , sys

sys.stdin=open("noeyes/section_5/1.가장큰수.txt", "rt")

data, n = map(int,input().split())
data = list(map(int,str(data)))
result = []
count = 0
# 5 2 7 6 8 2 3 
for i in range(0,len(data)):

  if(count > n):
    result.append(data[i])
    continue  

  while(result and data[i] > result[-1] and count < n):
    result.pop()
    count += 1

  result.append(data[i])

end = n - count
if(end):
  print(''.join(map(str,result[:-end])))
else:
  print(''.join(map(str,result)))




