import sys, os
from collections import deque
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# n=int(input())
# num=list(map(int, input().split()))
# num=deque(num)

# max=0
# res=[]
# while num:
#   if num[0]<max and num[-1]<max:
#     break
#   elif len(num)==1:
#     res.append("L")
#     break
#   elif num[0]>max and num[-1]>max:
#     if num[0] < num[-1]:
#       max=num[0]
#       num.popleft()
#       res.append("L")
#     else:
#       max=num[-1]
#       num.pop()
#       res.append("R")
#   elif num[0]>max:
#     max=num[0]
#     num.popleft()
#     res.append("L")
#   elif num[-1]>max:
#     max=num[-1]
#     num.pop()
#     res.append("R")
    
# print(len(res))
# for r in res:
#   print(r, end='')  
    

# ----------강의 풀이----------#
# 정렬할 수 X => lt, rt 써도 됨

n=int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]

while lt<=rt:
  if a[lt]>last:
    tmp.append((a[lt], 'L'))
  if a[rt]>last:
    tmp.append((a[rt], 'R'))
  tmp.sort()
  if len(tmp)==0: # 더 이상 숫자를 추가할 수 없는 경우
    break
  else:
    res=res+tmp[0][1]
    last=tmp[0][0]
    if tmp[0][1]=='L':
      lt+=1
    else:
      rt-=1
  tmp.clear()
print(len(res))
print(res)