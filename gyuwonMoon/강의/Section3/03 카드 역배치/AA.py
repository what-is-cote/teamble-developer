import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
card=list(range(21))

for i in range(10): # i 필요 없음!
  a, b=map(int, input().split())
  card[a:b+1]=card[b:a-1:-1]
  
for i in range(1, 21):
  print(card[i], end=" ")
    
  
# ----------강의 풀이----------#
card=list(range(21))

for _ in range(10):
  a, b=map(int, input().split())
  for i in range((b-a+1)//2):
    card[a+i], card[b-i]=card[b-i], card[a+i]
  
card.pop(0) # 0번 인덱스 삭제
for c in card:
  print(c, end=" ")