import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n=int(input())
people=[]
for _ in range(n):
  h, w=map(int, input().split())
  people.append((h, w))

cnt=n
for h, w in people:
  for i in range(n):
    if people[i][0] > h and people[i][1] > w:
      cnt-=1
      break

print(cnt)

  
# ----------강의 풀이----------#
# 1. 키 큰 순으로 정렬
# 2. 나보다 키가 큰 사람보다 몸무게가 무거워야함
# 3. 나보다 키가 작은 사람은 고려할 필요 X
# => 몸무게가 최댓값인 경우만 카운트

# n=int(input())
# body=[]
# for _ in range(n):
#   h, w=map(int, input().split())
#   body.append((h, w))

# body.sort(reverse=True)
# largest=0
# cnt=0
# for h, w in body:
#   if w > largest:
#     largest=w
#     cnt+=1

# print(cnt)