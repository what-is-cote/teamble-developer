import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 실패
# k, n=map(int, input().split())
# lan=[]
# for _ in range(k):
#   lan.append(int(input()))
# lan.sort()

# lt=0
# rt=k-1

# while lt<=rt:
#   mid=(lt+rt)//2
#   cnt=0
#   for l in lan:
#     cnt+=l//lan[mid]
#   if cnt==n:
#     print(lan[mid])
#     break
#   elif cnt<n:
#     rt=mid-1
#   else:
#     lt=mid+1
    
  
# ----------강의 풀이----------#
# 답은 1~최대랜선길이 사이
def Count(len):
  cnt=0
  for x in Line:
    cnt+=(x//len)
  return cnt

k, n=map(int, input().split())
Line=[]
res=0 # 최대길이
largest=0
for _ in range(k):
  tmp=int(input())
  Line.append(tmp)
  largest=max(largest, tmp)
lt=1
rt=largest
while lt<=rt:
  mid=(lt+rt)//2
  if Count(mid)>=n:
    res=mid
    lt=mid+1
  else:
    rt=mid-1
    
print(res)