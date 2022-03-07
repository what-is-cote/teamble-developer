import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n=int(input())

maximum=-2147000000
for _ in range(n):
  num=list(map(int, input().split()))
  
  if num[0]==num[1]==num[2]:
    tmp=10000+num[0]*1000
  elif num.count(num[0])==2:
    tmp=1000+num[0]*100
  elif num.count(num[1])==2:
    tmp=1000+num[1]*100
  else:
    tmp=max(num)*100
  
  if tmp>maximum:
    maximum=tmp

print(maximum)

# ----------강의 풀이----------#
# n=int(input())

# res=0
# for i in range(n):
#   tmp=input().split()
#   tmp.sort()
#   a, b, c=map(int, tmp)
  
#   if a==b and b==c:
#     money=10000+a*1000
#   elif a==b or a==c:
#     money=1000+a*100
#   elif b==c:
#     money=1000+b*100
#   else:
#     money=c*100 # c가 가장 큼(오름차순)
  
#   if money>res:
#     res=money

# print(res)