import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n=int(input())
l=[]
for _ in range(n):
  l.append(tuple(list(map(int, input().split()))))
  
l.sort(key=lambda l:l[1])

cnt=0
last=0
for i in range(n):
  if l[i][0]>=last:
    cnt+=1
    last=l[i][1]
  else:
    continue
print(cnt)

  
# ----------강의 풀이----------#
# 빨리 끝나야 많이 진행할 수 있기 때문에 끝나는 시각 기준으로 정렬
# n=int(input())
# meeting=[]
# for _ in range(n):
#   s, e=map(int, input().split())
#   meeting.append((s, e))
# meeting.sort(key=lambda x : (x[1], x[0])) # meeting 요소의 1번째 인덱스 (1순위, 2순위)

# et=0 # endtime
# cnt=0
# for s, e in meeting:
#   if s>=et:
#     et=e
#     cnt+=1

# print(cnt)