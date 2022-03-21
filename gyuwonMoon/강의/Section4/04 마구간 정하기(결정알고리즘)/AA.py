import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 실패!!
# n, c=map(int, input().split()) # 마구간 개수, 말 마리수
# x=[]
# largest=0
# for _ in range(n):
#   tmp=int(input())
#   x.append(tmp)
#   largest=max(largest, tmp)

# lt=1
# rt=largest-1
# mid=(lt+rt)//2

  
# ----------강의 풀이----------#
def Count(len):
  cnt=1
  ep=Line[0]
  for i in range(1, n):
    if Line[i]-ep>=len:
      cnt+=1
      ep=Line[i]
  return cnt

n, c=map(int, input().split()) # 마구간 개수, 말 마리수
Line=[]
for _ in range(n):
  tmp=int(input())
  Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
while lt<=rt:
  mid=(lt+rt)//2
  if Count(mid)>=c:
    res=mid
    lt=mid+1
  else:
    rt=mid-1
print(res)