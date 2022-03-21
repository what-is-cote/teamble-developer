import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n, m=map(int, input().split())
num=list(map(int, input().split()))
num.sort()

s=0
e=n-1

while True:
  idx=(s+e)//2
  if num[idx]==m:
    print(idx+1)
    break
  elif num[idx]<m:
    s=idx+1
  else:
    e=idx-1
    
  
# ----------강의 풀이----------#
# while lt<=rt:
#   mid=(lt+rt)//2
#   if num[mid]==m:
#     print(mid+1)
#     break
#   elif num[mid]>m:
#     rt=mid-1
#   else:
#     lt=mid+1