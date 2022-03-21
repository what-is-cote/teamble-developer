import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 실패!!
# n, m=map(int, input().split()) # 곡 개수, 디비디 개수
# length=list(map(int, input().split())) # 각 곡의 길이
    
  
# ----------강의 풀이----------#
# 답은 1~sum(Music) => lt~rt
def Count(capacity):
  cnt=1
  sum=0
  for x in Music:
    if sum+x>capacity: # 용량 초과
      cnt+=1
      sum=x
    else:
      sum+=x
  return cnt

n, m=map(int, input().split()) # 곡 개수, 디비디 개수
Music=list(map(int, input().split())) # 각 곡의 길이
maxx=max(Music)
lt=1
rt=sum(Music)
res=0
while lt<=rt:
  mid=(lt+rt)//2
  if mid>=maxx and Count(mid)<=m:
    res=mid
    rt=mid-1
  else:
    lt=mid+1
print(res)