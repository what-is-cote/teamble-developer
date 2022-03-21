import os , sys

os.system('clear')
sys.stdin=open("noeyes/section_3/8.txt", "rt")

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

count = int(input())
c = [list(map(int,input().split())) for _ in range(count)]


for command in c:
  
  idx = command[0] - 1
  flag = command[2]

  if(command[1] == 1):
    
    while(flag > 0):
      temp = arr[idx][n-1]

      for j in range(n-1,-1,-1):
        if(j != 0):
          arr[idx][j] = arr[idx][j-1]
      
      arr[idx][0] = temp
      flag-=1

    # 이거 쓰면 간단하다..
    # arr.append(arr.pop(0))


  else:

    while(flag > 0):
      temp = arr[idx][0]

      for j in range(n):
        if(j != n-1):
          arr[idx][j] = arr[idx][j+1]
      
      arr[idx][n-1] = temp
      flag-=1


s = 0
e = n
result =  0
for i in range(n):

  if(i < n//2):
    for j in range(s,e):
      result += arr[i][j]
    s+=1
    e-=1
      
  else:
    for j in range(s,e):
      result += arr[i][j]
    s-=1
    e+=1
  
print(result)